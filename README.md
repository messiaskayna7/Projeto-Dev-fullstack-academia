Nome: Messias Kaynã Ferreira de Sozua

Diário de I.A: A i.a foi utilizada apenas na estilização do projeto

Levantamento de Requisitos — Academia Corpo em Movimento

Cliente: Renata Albuquerque, proprietária
Analista: Carlos Celestino


A. O fluxo

1. Passos do zero até a grade aparecer

1. Criar a pasta e o venv (`python -m venv venv`) e ativá-lo
2. Instalar o Django (`pip install django`)
3. Criar o projeto (`django-admin startproject config .`)
4. Criar o app (`python manage.py startapp academia`)
5. Adicionar `'academia'` em `INSTALLED_APPS` no `config/settings.py` e ajustar `LANGUAGE_CODE = 'pt-br'` e `TIME_ZONE = 'America/Recife'`
6. Escrever os models `Modalidade` e `Turma` em `academia/models.py`
7. Rodar `python manage.py makemigrations` (gerou `0001_initial.py`)
8. Rodar `python manage.py migrate`
9. Criar o superusuário (`python manage.py createsuperuser`)
10. Registrar os models em `academia/admin.py` com `list_display`, `list_filter` e `search_fields`
11. Cadastrar as 4 modalidades e as 6 turmas pelo painel `/admin/`
12. Escrever as views `inicio` e `turmas` em `academia/views.py`
13. Criar os templates `base.html`, `inicio.html` e `turmas.html`
14. Criar `academia/urls.py` e incluí-lo em `config/urls.py`
15. Rodar `python manage.py runserver` e abrir `/turmas/` no navegador

2. O caminho do pedido /turmas/

1. O navegador envia `GET /turmas/`.
2. Em `config/urls.py`, a linha `path('', include('academia.urls'))` repassa o pedido para as URLs do app.
3. Em `academia/urls.py`, a linha `path('turmas/', views.turmas, name='turmas')` chama a view `turmas`.
4. Em `academia/views.py`, a view executa `Turma.objects.filter(modalidade__ativa=True).select_related('modalidade')`. Essa consulta busca as turmas de modalidades ativas e já traz a modalidade junto, numa só consulta. A view também envia o dicionário `ACADEMIA` com nome, endereço e telefone.
5. Em `academia/models.py`, o `ordering = ['dia_semana', 'horario']` do `Meta` faz o banco devolver as turmas já ordenadas por dia e horário.
6. Os dados vêm do `db.sqlite3`, das tabelas `academia_turma` e `academia_modalidade`, que foram preenchidas pelo painel admin.
7. O template `turmas.html` estende o `base.html`, que tem o cabeçalho e o menu. Ele percorre as turmas com `{% for %}` e exibe `turma.modalidade.nome`, `turma.get_dia_semana_display`, `turma.horario|time:"H:i"`, `turma.instrutor` e `turma.vagas`.
8. O `render` devolve o HTML pronto e o navegador mostra a tabela.

B. O porquê

3. makemigrations e migrate

O `makemigrations` lê o `models.py` e gera um arquivo de migração descrevendo as tabelas e campos. No projeto, esse arquivo é o `academia/migrations/0001_initial.py`. Esse comando ainda não altera o banco.

O `migrate` executa as migrações no `db.sqlite3`, criando as tabelas `academia_modalidade` e `academia_turma`, além das tabelas do próprio Django (usuários, sessões, admin).

Se rodassem só o `makemigrations`, o arquivo existiria, mas as tabelas não. Ao abrir o admin ou `/turmas/`, daria o erro `no such table: academia_turma`.

4. Chave estrangeira em vez de texto

Com texto, cada turma teria o nome da modalidade digitado de novo. Exemplo com os dados da academia: as duas turmas de Pilates do Rafael (segunda e quarta, 07:30) poderiam ser cadastradas como "Pilates" e "pilates". O filtro por modalidade mostraria só uma delas, e a Renata, que quer ver "só as turmas de pilates", veria a grade incompleta.

Além disso, se a Natação voltar da reforma com outro nome, seria preciso editar turma por turma. Também não daria para aplicar a RN03 (impedir remover modalidade com turmas) nem a RN08 (esconder as turmas de modalidade inativa), porque não haveria uma modalidade de verdade ligada à turma. Com a FK, a modalidade existe em um só lugar e a turma só aponta para ela.

5. Excluir Musculação, que tem turmas

O Django impede a exclusão. No admin aparece uma página dizendo que não é possível excluir a modalidade "Musculação", porque isso exigiria apagar objetos protegidos. A página lista as duas turmas da Carla (segunda 19:00 e terça 18:00).

A decisão está em `academia/models.py`:

```python
modalidade = models.ForeignKey(Modalidade, on_delete=models.PROTECT, related_name='turmas')
```

Escolhemos `PROTECT` porque a RN03 exige isso e porque o `CASCADE` apagaria as turmas da Carla junto, sem aviso, e a grade publicada perderia horários. Com `PROTECT`, a proprietária precisa primeiro excluir ou mover as turmas. Se ela só quiser tirar a modalidade do site, pode desmarcar "ativa".

6. Dia da semana com lista fixa

O campo é `dia_semana = models.PositiveSmallIntegerField(choices=DIAS_SEMANA)`, com os valores de 1 (Segunda-feira) a 6 (Sábado), conforme a RN04.

A lista fixa garante que não existam "seg", "Segunda", "segunda " ou um domingo, porque só esses seis valores entram. Na prática, o filtro "dia da semana" do painel mostra exatamente os seis dias, e clicar em "Segunda-feira" traz todas as turmas de segunda.

Como o valor guardado é um número, o `ordering = ['dia_semana', 'horario']` ordena a grade na ordem da semana. Se o campo fosse texto, a ordem seria alfabética e "Quarta" apareceria antes de "Segunda".

7. Sem list_display, list_filter e search_fields

O painel continuaria funcionando, mas a lista de turmas mostraria apenas o texto do `__str__`, sem colunas separadas de modalidade, dia, horário, instrutor e vagas, que o RF03 pede. Também não haveria filtro por modalidade e dia nem busca por instrutor (RF04).

Isso vai contra o que a Renata disse na reunião: ela quer "achar rápido a turma de um instrutor ou só as turmas de pilates". O `search_fields = ['instrutor']` resolve a primeira parte: pesquisar "Carla" traz as duas turmas dela. O `list_filter = ['modalidade', 'dia_semana']` resolve a segunda: um clique em Pilates mostra só as turmas de pilates. No `ModalidadeAdmin`, o `list_filter = ['ativa']` permite separar as ativas das inativas (RF05).

8. Três modalidades na página inicial

A responsável é esta linha da view `inicio`, em `academia/views.py`:

```python
modalidades = Modalidade.objects.filter(ativa=True)
```

O filtro `ativa=True` traz só as modalidades com o campo "ativa" marcado. Há quatro cadastradas, mas a Natação está inativa por causa da reforma da piscina. Por isso aparecem só Funcional, Musculação e Pilates, em ordem alfabética pelo `ordering = ['nome']`. Isso cumpre a RN08: a Natação continua no painel, mas não aparece no site.

C. O processo

9. Trecho do Copilot corrigido ou rejeitado
O copilot não foi usado.

10. Decisão fora do documento de requisitos

A equipe tomou estas decisões que o documento não cobria:

- A grade `/turmas/` mostra só as turmas de modalidades ativas (`filter(modalidade__ativa=True)`). O RF07 fala em "todas as turmas", e a RN08 só trata da página inicial. Decidimos esconder da grade as turmas de modalidade inativa, para o aluno não ver aula de uma modalidade que não está funcionando. Hoje nenhuma turma é de Natação, então as seis aparecem.
- O dia da semana é guardado como número (1 = segunda a 6 = sábado) e não como texto, para a grade ficar na ordem da semana.
- O documento não informava endereço e telefone, então eles ficaram fixos na view, com "Caruaru - Centro" e "(81) 0000-0000" no lugar dos dados reais.

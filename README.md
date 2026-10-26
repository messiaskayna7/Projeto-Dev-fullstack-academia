Nome: Messias Kaynã Ferreira de Sozua

Diário de I.A: A i.a foi utilizada apenas na estilização do projeto

Levantamento de Requisitos — Academia Corpo em Movimento

Cliente: Renata Albuquerque, proprietária
Analista: Carlos Celestino




1. Contexto

1.1. A Academia Corpo em Movimento atua há seis anos em Caruaru e oferece aulas de musculação, pilates, natação e funcional.

1.2. Atualmente, a grade de horários fica em um quadro branco na recepção, e uma foto dele é enviada pelo WhatsApp.

1.3. Sempre que um horário muda ou um novo instrutor entra, a foto perde a validade e os alunos precisam ligar para confirmar.

1.4. Segundo a cliente, na reunião de levantamento: *"Eu quero duas coisas. Um lugar onde eu mesma cadastro as modalidades e as turmas, sem depender de ninguém, e que consiga achar rápido a turma de um instrutor ou só as turmas de pilates. E um site simples onde o aluno vê o que a academia oferece e a grade da semana, sempre certa, porque sai direto do que eu cadastrei."*

2. Objetivo

2.1. Desenvolver um sistema web com painel administrativo, no qual a proprietária gerencie modalidades e turmas.

2.2. Disponibilizar duas páginas públicas que apresentem essas informações aos alunos, buscando os dados diretamente no banco de dados.

3. Escopo

3.1. Incluído nesta versão:
1. Cadastro de modalidades e turmas pelo painel.
2. Página inicial com as modalidades.
3. Página com a grade de turmas.
4. Filtros e busca no painel.

3.2. Fora desta versão:
1. Matrícula de alunos.
2. Pagamento.
3. Login de aluno.
4. Aplicativo para celular.
5. Fotos.

4. Requisitos funcionais

4.1. RF01: O sistema deve permitir cadastrar, alterar, visualizar e remover modalidades pelo painel administrativo.

4.2. RF02: O sistema deve permitir cadastrar, alterar, visualizar e remover turmas pelo painel administrativo.

4.3. RF03: No painel, a listagem de turmas deve exibir, em colunas: modalidade, dia da semana, horário, instrutor e vagas.

4.4. RF04: No painel, deve ser possível filtrar as turmas por modalidade e por dia da semana, além de pesquisar turmas pelo nome do instrutor.

4.5. RF05: No painel, a listagem de modalidades deve exibir o nome e se ela está ativa, com filtro por ativa/inativa.

4.6. RF06: A página inicial (`/`) deve exibir o nome da academia, o endereço, o telefone e a relação de modalidades ativas, com a descrição de cada uma.

4.7. RF07: A página de grade (`/turmas/`) deve exibir todas as turmas em uma tabela com modalidade, dia, horário, instrutor e vagas, organizadas por dia da semana e horário.

4.8. RF08: As duas páginas devem possuir um menu com link para a outra.

5. Regras de negócio

5.1. RN01: Cada turma pertence a exatamente uma modalidade, e uma modalidade pode ter diversas turmas.

5.2. RN02: Não é permitido existir turma sem modalidade.

5.3. RN03: Não deve ser possível remover uma modalidade que ainda possua turmas cadastradas.

5.4. RN04: O dia da semana é selecionado em uma lista fixa, de segunda a sábado, e não pode ser digitado livremente.

5.5. RN05: O horário é registrado no formato 24h (ex.: `07:30`, `18:00`).

5.6. RN06: A quantidade de vagas é um número inteiro e nunca pode ser negativa.

5.7. RN07: Não podem existir duas modalidades com o mesmo nome.

5.8. RN08: Uma modalidade inativa permanece no painel, mas não é exibida na página inicial.

6. Dados

6.1. Modalidade
1. nome: texto curto, obrigatório e único (RN07).
2. descrição: texto longo, opcional; é exibida na página inicial.
3. ativa: sim/não, obrigatório; valor padrão: sim.

6.2. Turma
1. modalidade: referência a uma Modalidade, obrigatório (RN01, RN02, RN03).
2. dia da semana: lista fixa, obrigatório (RN04).
3. horário: hora, obrigatório (RN05).
4. instrutor: texto curto, obrigatório; nome da pessoa.
5. vagas: inteiro não negativo, obrigatório; valor padrão: 10 (RN06).

6.3. Em qualquer lugar onde uma turma for exibida, seja no painel ou nas páginas, ela deve aparecer de forma legível, por exemplo: **Pilates — Segunda 07:30**.

7. Dados iniciais

7.1. Para a entrega, o sistema deve conter os dados abaixo, cadastrados pelo painel.

7.2. Modalidades
1. Musculação: treino com pesos, acompanhamento individual. Ativa.
2. Pilates: solo e aparelhos, turmas pequenas. Ativa.
3. Funcional: circuito de alta intensidade. Ativa.
4. Natação: piscina aquecida (em reforma). Inativa.

7.3. Turmas
1. Pilates, Segunda, 07:30, Rafael, 8 vagas.
2. Musculação, Segunda, 19:00, Carla, 15 vagas.
3. Funcional, Terça, 06:30, Diego, 12 vagas.
4. Musculação, Terça, 18:00, Carla, 15 vagas.
5. Pilates, Quarta, 07:30, Rafael, 8 vagas.
6. Funcional, Sábado, 09:00, Diego, 20 vagas.

8. Requisitos não funcionais

8.1. RNF01: Utilizar Python 3 e Django, com o banco de dados padrão do Django (SQLite).

8.2. RNF02: O projeto deve ser novo, criado do zero e em um ambiente virtual próprio.

8.3. RNF03: O código deve ficar em um repositório no GitHub, com `.gitignore` (venv, `__pycache__`, `db.sqlite3`) e no mínimo três commits com mensagens que descrevam o que foi feito: projeto criado; modelos e painel; páginas.

8.4. RNF04: O `README.md` deve conter o nome da equipe, as instruções para rodar o projeto e o diário de IA do dia.

8.5. RNF05: Toda decisão não prevista neste documento deve ser tomada pela equipe e registrada no README, em uma seção "Decisões".

9. Critérios de aceite

9.1. A entrega será aprovada quando o analista, no computador da equipe, conseguir:
1. Acessar o painel e visualizar as duas listagens (modalidades e turmas) com as colunas solicitadas.
2. Filtrar as turmas por modalidade e por dia, e pesquisar por "Carla", encontrando as duas turmas dela.
3. Tentar remover a modalidade Musculação e ser impedido (RN03).
4. Abrir `/` e visualizar as três modalidades ativas com descrição, sem a Natação.
5. Abrir `/turmas/` e visualizar as seis turmas na ordem: segunda 07:30, segunda 19:00, terça 06:30, terça 18:00, quarta 07:30, sábado 09:00.
6. Navegar entre as páginas pelo menu.
7. Abrir o repositório no GitHub e visualizar os três commits e o README.

 10. Entrega

10.1. Prazo: até o fim do encontro de hoje.

10.2. Forma: link do repositório e demonstração de 5 minutos para o analista.

10.3. Após a entrega, haverá uma segunda etapa, que será apresentada no momento.

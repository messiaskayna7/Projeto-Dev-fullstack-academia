from django.db import models

# Create your models here.

class Modalidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField('descrição', blank=True)
    ativa = models.BooleanField(default=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Turma(models.Model):
    DIAS_SEMANA = [
        (1, 'Segunda-feira'),
        (2, 'Terça-feira'), 
        (3, 'Quarta-feira'),
        (4, 'Quinta-feira'),
        (5, 'Sexta-feira'),
        (6, 'Sábado'),
    ]

    modalidade = models.ForeignKey(Modalidade, on_delete=models.PROTECT, related_name='turmas')
    dia_semana = models.PositiveSmallIntegerField('dia da semana', choices=DIAS_SEMANA)
    horario = models.TimeField('horário')
    instrutor = models.CharField(max_length=100)
    vagas = models.PositiveSmallIntegerField(default=10)

    class Meta:
        ordering = ['dia_semana', 'horario']


    def __str__(self):
        dia = self.get_dia_semana_display()
        return f'{self.modalidade.nome} - {dia} - {self.horario.strftime("%H:%M")} - {self.instrutor}'


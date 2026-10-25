from django.contrib import admin
from .models import Modalidade, Turma
# Register your models here.

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativa']
    list_filter = ['ativa']


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['modalidade', 'dia_semana', 'horario', 'instrutor', 'vagas']
    list_filter = ['modalidade', 'dia_semana']
    search_fields = ['instrutor']
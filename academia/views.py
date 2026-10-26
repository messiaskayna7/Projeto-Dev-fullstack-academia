from django.shortcuts import render

from .models import Modalidade, Turma


ACADEMIA = {
    'nome': 'Academia Corpo',
    'endereco': 'Caruaru - Centro',
    'telefone': '(81) 0000-0000',
}


def inicio(request):
    modalidades = Modalidade.objects.filter(ativa=True)
    return render(request, 'academia/inicio.html', {
        'academia': ACADEMIA,
        'modalidades': modalidades,
    })


def turmas(request):
    turmas = Turma.objects.filter(modalidade__ativa=True).select_related('modalidade')
    return render(request, 'academia/turmas.html', {
        'academia': ACADEMIA,
        'turmas': turmas,
    })

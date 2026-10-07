from django.shortcuts import render


def inicio(request):
    # O contexto é um dicionário: suas chaves viram variáveis no template.
    contexto = {
        'nome': 'Cíntia',
        'curso': 'Introdução ao Django Templates',
        'topicos': [
            'Exibir variáveis enviadas pela view',
            'Reutilizar HTML com extends, block e include',
            'Percorrer listas com for e empty',
            'Mostrar conteúdo com if e else',
            'Formatar valores com filtros',
            'Criar links e carregar CSS com url e static',
        ],
    }
    return render(request, 'aulas/inicio.html', contexto)


def alunos(request):
    # Dados fictícios em memória para concentrar a aula nos templates.
    # Experimente trocar esta lista por [] para ver o bloco empty.
    lista_alunos = [
        {'nome': 'Ana Souza', 'nota': 9.0},
        {'nome': 'Bruno Lima', 'nota': 6.5},
        {'nome': 'Carla Santos', 'nota': 8.0},
    ]
    return render(request, 'aulas/alunos.html', {'alunos': lista_alunos})

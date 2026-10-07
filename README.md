# Django Templates para Cíntia

Projeto acadêmico preparado para a Cíntia, aquela que foi abandonada por um tal de Eduardo, usando Python,
Django 5.2 e HTML com Django Templates.

Cíntia, começando pela página inicial e depois explore o exemplo da turma.
A ideia é ler um trecho de código, fazer uma pequena mudança e conferir o resultado no navegador.
As páginas usam dados fictícios em memória para focar em URLs, views e templates.
O SQLite permanece na configuração padrão do Django; os exemplos não consultam o banco.

## Rodar no Windows (PowerShell)

O ambiente `.venv` já foi criado e as dependências já foram instaladas nesta pasta.

```powershell
.\.venv\Scripts\Activate.ps1
python manage.py runserver
```

Abra <http://127.0.0.1:8000/>. A página de alunos está em <http://127.0.0.1:8000/alunos/>.
Use `Ctrl+C` para parar o servidor e `deactivate` para sair do ambiente virtual.

Se o PowerShell bloquear a ativação, execute diretamente o Python do ambiente:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

Ao copiar o projeto para outro computador, instale Python 3.10 ou superior e recrie o ambiente:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

## Onde estudar

```text
manage.py                              Comandos do Django
config/settings.py                     Configurações (idioma, apps, templates)
config/urls.py                         Encaminha as URLs para o app aulas
aulas/urls.py                          Liga cada URL à sua view
aulas/views.py                         Prepara dados e renderiza o template
aulas/templates/aulas/base.html        Estrutura HTML compartilhada
aulas/templates/aulas/partials/menu.html  Menu reutilizável
aulas/templates/aulas/inicio.html      Variáveis, filtros e introdução
aulas/templates/aulas/alunos.html      Loop, condição e lista vazia
aulas/static/aulas/css/estilo.css       Estilos da página
```

Comece pelo caminho **URL → view → template → HTML**:

1. O navegador pede `/alunos/`.
2. `config/urls.py` encaminha para `aulas/urls.py`.
3. A rota chama a função `alunos` em `aulas/views.py`.
4. A view passa o dicionário de contexto para `render()`.
5. O Django processa `alunos.html`, que herda `base.html`, e devolve o HTML.

Com `APP_DIRS=True` e o app `aulas` registrado, o Django encontra os templates
na pasta `templates` do app. O caminho `aulas/alunos.html` evita confusão entre
templates de apps diferentes.

## Conceitos demonstrados

| Sintaxe | Uso no projeto |
| --- | --- |
| `{{ nome }}` | Exibe um valor do contexto |
| `{{ aluno.nome }}` | Acessa uma chave do dicionário |
| `{% extends 'aulas/base.html' %}` | Herda a estrutura de outra página |
| `{% block conteudo %}` | Define a região preenchida pela página filha |
| `{% include 'aulas/partials/menu.html' %}` | Reutiliza um trecho de HTML |
| `{% for aluno in alunos %}` | Percorre uma lista |
| `{% empty %}` | Mostra uma mensagem quando a lista está vazia |
| `{% if aluno.nota >= 7 %}` | Decide qual conteúdo exibir |
| `{{ forloop.counter }}` | Numera os itens do loop |
| `{{ nome\|capfirst }}` | Deixa a primeira letra maiúscula |
| `{{ alunos\|length }}` | Conta os alunos |
| `{{ aluno.nota\|floatformat:1 }}` | Formata a nota com uma casa decimal |
| `{% url 'aulas:alunos' %}` | Gera um link pelo nome da rota |
| `{% load static %}` e `{% static 'aulas/css/estilo.css' %}` | Carrega o CSS |
| `{# comentário #}` | Comenta sem incluir o texto no HTML final |
| `{% verbatim %}` | Mostra a sintaxe de templates sem processá-la |

Templates exibem dados; prepare cálculos e regras mais complexas na view.
O Django escapa valores HTML automaticamente. Mantenha esse comportamento
ao exibir conteúdo digitado por usuários.

## Sua primeira aula, Cíntia

1. Seu nome já está no contexto da view `inicio`. Troque `Cíntia` por um apelido e veja a saudação mudar.
2. Adicione um tópico à lista `topicos` e observe o loop na página inicial.
3. Adicione um aluno à lista `lista_alunos`, usando as mesmas chaves.
4. Mude uma nota de `6.5` para `8.0` e observe o `if / else`.
5. Troque `lista_alunos` por `[]` e observe a mensagem do bloco `empty`.
6. Adicione uma chave `curso` a cada aluno e uma coluna correspondente no template.
7. Altere o menu compartilhado e confira a mudança nas duas páginas.

## Verificar a configuração

```powershell
.\.venv\Scripts\python.exe manage.py check
```

As configurações são para desenvolvimento local (`DEBUG=True`).

Referências: [tutorial oficial sobre views e templates](https://docs.djangoproject.com/pt-br/5.2/intro/tutorial03/)
e [linguagem de templates](https://docs.djangoproject.com/pt-br/5.2/ref/templates/language/).

# Evitando o erro "Ops is not defined" nas páginas 1 e 2
filename = 'Reusables/Sidebars.py'
exec(open(filename, encoding="utf-8").read())

# Formatação dos números
locale_pt_BR = """d3.formatLocale({
  "decimal": ",",
  "thousands": ".",
  "grouping": [3],
  "currency": ["R$", ""],
  "thousands": "\u00a0",
})"""



numformat = {"function": f"{locale_pt_BR}.format(',.2f')(params.value)"}


clndef = [


    {'field': 'Alunos'},

    {'field': 'Gênero'},

    {'field': 'Etnia'},

    {'field': 'Escola'},

    {'field': 'Renda (R$)',
     'filter': 'agNumberColumnFilter'},

    {'field': 'Média aluno',
     'valueFormatter': numformat,
     'filter': 'agNumberColumnFilter'},

    {'field': 'Média turma',
     'valueFormatter': numformat,
     'filter': 'agNumberColumnFilter'},

    {'field': 'Frequência',
     'valueFormatter': numformat,
     'filter': 'agNumberColumnFilter'},

    {'field': 'Resultado'},

    {'field': 'Professor'}


]






dfclndef = {
    'headerClass': 'center-aligned-header',
    'cellClass': 'center-aligned-cell',
    'filter': True,
    'filterParams': {
        "alwaysShowBothConditions": True,
    },
    'floatingFilter': True,
    'suppressMenu': True,
}
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

    {'field': 'Sexo'},

    {'field': 'Etnia'},

    {'field': 'Escola'},

    {'field': 'Renda (R$)',
     'filter': 'agNumberColumnFilter'},

    {'field': 'Med aluno',
     'valueFormatter': numformat,
     'filter': 'agNumberColumnFilter'},

    {'field': 'Med turma',
     'valueFormatter': numformat,
     'filter': 'agNumberColumnFilter'},

    {'field': 'Freq',
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
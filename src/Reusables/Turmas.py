# Formatação dos números
locale_pt_BR = """d3.formatLocale({
  "decimal": ",",
  "thousands": ".",
  "grouping": [3],
  "currency": ["R$", ""],
  "thousands": "\u00a0",
})"""

gradeformat = {"function": f"{locale_pt_BR}.format(',.2f')(params.value)"}
numformat = {"function": f"{locale_pt_BR}.format(',.0f')(params.value)"}

clndef = [

    {'nameHeader': 'Código', 'field': 'Cod', "sortable": True},

    {'field': 'Disciplina', "sortable": True},

    {'field': 'Turma', "sortable": True, 'sort': 'asc',
     # "valueGetter": {"function": date_obj},
     # "valueFormatter": {"function": f"d3.timeFormat('%Y/%m/%d')({date_obj})"},
     # "filter": "agDateColumnFilter"
     },

    {'field': 'Professor', "sortable": True},

    {'field': 'Av Professor',
     'valueFormatter': gradeformat,
     'filter': 'agNumberColumnFilter'},

    {'headerName': 'Média turma',
     'field': 'Med turma',
     'valueFormatter': gradeformat,
     'filter': 'agNumberColumnFilter'},

    {'field': 'AP',
     'valueFormatter': numformat,
     'filter': 'agNumberColumnFilter'},

    {'field': 'RM',
     'valueFormatter': numformat,
     'filter': 'agNumberColumnFilter'},

    {'field': 'RF',
     'valueFormatter': numformat,
     'filter': 'agNumberColumnFilter'},

    {'field': 'RMF',
     'valueFormatter': numformat,
     'filter': 'agNumberColumnFilter'},

    {'field': 'Num Alunos',
     'valueFormatter': numformat,
     'filter': 'agNumberColumnFilter'}

]

dfclndef = {
    'headerClass': 'center-aligned-header',
    'cellClass': 'center-aligned-cell',
    'resizable': True,
    'filter': True,
    'filterParams': {
        "alwaysShowBothConditions": True,
    },
    'floatingFilter': True,
    'suppressMenu': True,
}


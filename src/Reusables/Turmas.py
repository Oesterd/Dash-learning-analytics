# Selecionando os dados a serem lidos
dft = pd.read_excel('https://github.com/Oesterd/Dash-learning-analytics/raw/master/Dados_turma.xlsx')

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
    {'field': 'Código', "sortable": True},
    {'field': 'Disciplina', "sortable": True},
    {'field': 'Ano e período', "sortable": True, 'sort': 'asc'},
    {'field': 'Professor', "sortable": True},
    {'field': 'Avaliação professor',
     'valueFormatter': gradeformat},
    {'field': 'Média turma',
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
    'filter': 'agMultiColumnFilter',
    'resizable': True
}


grid2 = dag.AgGrid(
    id='grid',
    rowData=dft.to_dict('records'),
    columnDefs=clndef,
    defaultColDef=dfclndef,
    dashGridOptions={'pagination': True},
)

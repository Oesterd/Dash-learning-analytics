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
     'valueFormatter': gradeformat},
    {'field': 'AP',
     'valueFormatter': numformat},
    {'field': 'RM',
     'valueFormatter': numformat},
    {'field': 'RF',
     'valueFormatter': numformat},
    {'field': 'RMF',
     'valueFormatter': numformat},
    {'field': 'Num Alunos',
     'valueFormatter': numformat}
]


dfclndef = {
    'headerClass': 'center-aligned-header',
    'cellClass': 'center-aligned-cell',
    'filter': 'agMultiColumnFilter',
    'resizable': True
}


grid = dag.AgGrid(
    id='grid',
    rowData=dft.to_dict('records'),
    columnDefs=clndef,
    defaultColDef=dfclndef,
    dashGridOptions={'pagination': True},
)

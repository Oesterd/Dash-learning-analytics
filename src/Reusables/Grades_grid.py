# Selecionando os dados a serem lidos
dfraw = pd.read_excel('https://github.com/Oesterd/Dash-learning-analytics/raw/master/dados_teste.xlsx')
df = dfraw.iloc[:, 0:10]



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
    {'field': 'Renda'},
    {'field': 'Média aluno',
     'valueFormatter': numformat},
    {'field': 'Média turma',
     'valueFormatter': numformat},
    {'field': 'Frequência',
     'valueFormatter': numformat},
    {'field': 'Situação'},
    {'field': 'Professor'}
]

dfclndef = {
    'headerClass': 'center-aligned-header',
    'cellClass': 'center-aligned-cell',
    'filter': 'agMultiColumnFilter',
    'resizable': True
}


grid = dag.AgGrid(
    id='grid',
    rowData=df.to_dict('records'),
    columnDefs=clndef,
    defaultColDef=dfclndef,
    dashGridOptions={'pagination': True},
)





# Opções do dropdown
nullop = 'Nenhuma'
op1 = df.columns[[4, 9]].tolist()  # Divisão por cores
op1.insert(0, nullop)
op2 = df.columns[1:4].tolist()  # Divisão por colunas
op2.insert(0, nullop)


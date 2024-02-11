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



# Opções do dropdown
nullop = 'Nenhuma'
op2 = df.columns[1:4].to_list()  # Divisão por colunas
op2.insert(0, nullop)


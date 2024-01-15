# Importando as bibliotecas
import dash
from dash import html, dcc, dash_table, Input, Output, callback
from dash.dash_table.Format import Format, Scheme


import plotly.express as px
import pandas as pd
import numpy as np






dash.register_page(__name__, name='Correlação')





# Selecionando os dados a serem lidos
dfraw = pd.read_excel('https://github.com/Oesterd/Dash123/raw/master/dados_teste.xlsx')
df = dfraw.iloc[:, 0:10]


# Formatação dos números
numformat = Format(precision=2, scheme=Scheme.fixed, decimal_delimiter=',')
renformat = Format(precision=0, scheme=Scheme.fixed, decimal_delimiter=',')



# Separando as colunas para os dicionários
dfmed = df.iloc[:, 5:8]
dftext = df.iloc[:, 1:4]
dfend = df.iloc[:, 8:10]







# Criando os dicionários
dictaln = [{'name': 'Alunos', 'id': 'Alunos', 'type': 'text'}]
dicttext = [{'name': i, 'id': i} for i in dftext]
dictren = [{'name': 'Renda (S.M)', 'id': 'Renda (S.M)', 'type': 'numeric', 'format': renformat}]
dictmed = [{'name': i, 'id': i, 'type': 'numeric', 'format': numformat} for i in dfmed]
# dictfrq = [{'name': 'Frequência', 'id': 'Frequência', 'type': 'numeric', 'format': numformat, 'selectable': True}]
dictend = [{'name': i, 'id': i} for i in dfend]


# Opções do dropdown
nullop = 'Nenhuma'
op1 = df.columns[np.r_[4,9]].tolist() # Divisão por cores
op1.insert(0, nullop)
op2 = df.columns[1:4].tolist() # Divisão por colunas
op2.insert(0, nullop)



Ops = {
   'Nenhuma': ['Nenhuma', 'Gênero', 'Escola'],
   'Gênero': ['Nenhuma', 'Escola'],
   'Escola': ['Nenhuma', 'Gênero'],
   'Etnia': ['Nenhuma', 'Gênero', 'Escola']
}





layout = \
html.Div([
    html.Div([
        dash_table.DataTable(  # Tabela de dados
            id='datatable_id',
            columns=dictaln + dicttext + dictren + dictmed + dictend,
            style_cell={'textAlign': 'center'},
            sort_action='native',
            sort_mode='single',
            filter_action='native',
            page_size=8,
            data=df.to_dict('records')
        )
    ]),



    # Menus de dropdown
    html.Div([
        html.Div([
            "Divisão por colunas:",
            dcc.Dropdown(
                list(Ops.keys()),
                'Nenhuma',
                id='dropdown',
                clearable=False
            ),
        ]),


        html.Div([
            "Divisão por linhas:",
            dcc.Dropdown(id='dropdown2', value='Nenhuma', options=['Nenhuma', 'Gênero', 'Escola'], clearable=False),
        ]),


        html.Div([
            "Regressão linear:",
            dcc.Dropdown(id='dropdown3', value='Nenhuma', options=[
                {'label': 'Nenhuma', 'value': 'Nenhuma'},
                {'label': 'Linear', 'value': 'ols'},
                {'label': 'Pesada', 'value': 'lowess'}
            ], clearable=False)
        ])
    ], style={'display': 'flex', 'flexDirection': 'row', 'gap': 50, 'flex': 1}),

    # Gráfico
    html.Div([
        dcc.Graph(id='scatter')
    ])
])




#-----------------------------------------------------
@callback(
    Output('dropdown2', 'options'),
    Input('dropdown', 'value')
)

def drop_chain(drop1value):
    return [{'label': i, 'value': i} for i in Ops[drop1value]]


@callback(
    Output('dropdown2', 'value'),
    Input('dropdown2', 'options'))

def drop2init(available_options):
    return available_options[0]['value']




@callback(
    Output(component_id='scatter', component_property='figure'),
    Input(component_id='dropdown', component_property='value'),
    Input(component_id='dropdown2', component_property='value'),
    Input(component_id='dropdown3', component_property='value'),
    Input(component_id='datatable_id', component_property='derived_virtual_data')
)


def scatter_plot(drop1, drop2, drop3, rows):


    ## Criando o gráfico

    # Modificando os dados conforme a filtragem do usuário
    dff = pd.DataFrame(rows)


    # Criando as opções nulas para os dropdowns 1 e 2
    if drop1 == 'Nenhuma':
        drop1 = None
    else:
        drop1 = f'{drop1}'

    if drop2 == 'Nenhuma':
        drop2 = None
    else:
        drop2 = f'{drop2}'

    if drop3 == 'Nenhuma':
        drop3 = None
    else:
        drop3 = f'{drop3}'



    fig = px.scatter(dff, x='Frequência', y='Média aluno', color='Professor', facet_col=drop1, facet_row=drop2, trendline=drop3)

    return fig
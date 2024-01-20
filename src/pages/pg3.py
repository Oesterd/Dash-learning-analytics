# Importando as bibliotecas
import dash, orjson
from dash import html, dcc, Input, Output, callback
import dash_ag_grid as dag


import plotly.express as px
import pandas as pd
import numpy as np






dash.register_page(__name__, name='Correlação')





filename = 'Reusables/Grades_grid.py'
exec(open(filename).read())



Ops = {
   'Nenhuma': ['Nenhuma', 'Gênero', 'Escola'],
   'Gênero': ['Nenhuma', 'Escola'],
   'Escola': ['Nenhuma', 'Gênero'],
   'Etnia': ['Nenhuma', 'Gênero', 'Escola']
}




layout = \
html.Div([
    html.Div([
        grid
    ]),



    # Menus de dropdown
    html.Div([
        html.Div([
            "Divisão por colunas:",
            dcc.Dropdown(
                list(Ops.keys()),
                'Nenhuma',
                id='dropdown31',
                clearable=False
            ),
        ]),


        html.Div([
            "Divisão por linhas:",
            dcc.Dropdown(id='dropdown32', value='Nenhuma', options=['Nenhuma', 'Gênero', 'Escola'], clearable=False),
        ]),


        html.Div([
            "Regressão linear:",
            dcc.Dropdown(id='dropdown33', value='Nenhuma', options=[
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




#--------------------------------------------------------------------------------------------
@callback(
    Output('dropdown32', 'options'),
    Input('dropdown31', 'value')
)

def drop_chain(drop1value):
    return [{'label': i, 'value': i} for i in Ops[drop1value]]


@callback(
    Output('dropdown32', 'value'),
    Input('dropdown32', 'options'))

def drop2init(available_options):
    return available_options[0]['value']







#---------------------------------------------------------------------------------
@callback(
    Output(component_id='scatter', component_property='figure'),
    Input(component_id='dropdown31', component_property='value'),
    Input(component_id='dropdown32', component_property='value'),
    Input(component_id='dropdown33', component_property='value'),
    Input(component_id='grid', component_property='virtualRowData')
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
# Importando as bibliotecas
import dash, orjson
from dash import html, dcc, Input, Output, callback
from dash.dash_table.Format import Format, Scheme
import dash_ag_grid as dag


import plotly.express as px
import pandas as pd
import numpy as np






dash.register_page(__name__, name='Turmas')




filename = 'Reusables/Turmas.py'
exec(open(filename).read())



Opcs = ['Média turma', 'AP', 'RM', 'RF', 'RMF']







layout = \
html.Div([
    html.Div([
        grid
    ]),


    html.Div([
        html.Div([
            "Escolha o eixo y:",
            dcc.Dropdown(id='dropdown51', value='Média turma', options=Opcs, clearable=False),
        ]),



        html.Div([
            "Regressão linear:",
            dcc.Dropdown(id='dropdown52', value='Nenhuma', options=[
                {'label': 'Nenhuma', 'value': 'Nenhuma'},
                {'label': 'Linear', 'value': 'ols'},
                {'label': 'Pesada', 'value': 'lowess'}
            ], clearable=False)
        ])
    ], style={'display': 'flex', 'flexDirection': 'row', 'gap': 50, 'flex': 1}),




    # Gráfico
    html.Div([
        dcc.Graph(id='scatter2')
    ])


])






#--------------------------------------------------------------------------------------------
@callback(
    Output(component_id='scatter2', component_property='figure'),
    Input(component_id='grid', component_property='virtualRowData'),
    Input(component_id='dropdown51', component_property='value'),
    Input(component_id='dropdown52', component_property='value'),
)








def scatter_plot(rows, drop1, drop2):

    # Modificando os dados conforme a filtragem do usuário
    dff2 = pd.DataFrame(rows)


    if drop2 == 'Nenhuma':
        drop2 = None

    # Criando o gráfico
    fig = px.scatter(dff2, x='Avaliação professor', y=f'{drop1}', color='Professor', trendline=drop2)

    return fig
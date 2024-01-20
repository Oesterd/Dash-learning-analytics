# Importando as bibliotecas
import dash, orjson
from dash import html, dcc, Input, Output, callback
import dash_ag_grid as dag


import plotly.express as px
import pandas as pd
import numpy as np

import datetime






dash.register_page(__name__, name='Linha do tempo')





filename = 'Reusables/Turmas.py'
exec(open(filename).read())



Opcs = ['Média turma', 'AP', 'RM', 'RF', 'RMF']




layout = \
html.Div([
    html.Div([
        grid
    ]),


    html.Br(),


    html.Div([
            "Escolha o eixo y:",
            dcc.Dropdown(id='dropdown41', value='Média turma', options=Opcs, clearable=False),
    ], style={'width': '10%'}),


    # Gráfico
    html.Div([
        dcc.Graph(id='timeseries')
    ])

])





@callback(
    Output(component_id='timeseries', component_property='figure'),
    Input(component_id='grid', component_property='virtualRowData'),
    Input(component_id='dropdown41', component_property='value')

)


def filterdata(rows, drop1):


    dffP4 = pd.DataFrame(rows)


    figpg4 = px.line(dffP4, x='Ano e período', y=f'{drop1}', color='Disciplina', symbol='Disciplina',
                     markers=True, hover_name='Disciplina',
                     hover_data={
                         'Disciplina': False,
                         'Professor': True,
                         'Ano e período': False,
                         'Aprovados': (':.0%', dffP4['AP']/dffP4['Num Alunos']),
                     })

    return figpg4
#---------------------------------------------------------------------------------



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



    # Transformando os dados no eixo y em uma razão ao invés de número absoluto
    if drop1 == 'Média turma':
        var = drop1
        drop1 = dffP4['Média turma']

    elif drop1 == 'AP':
        var = drop1
        var2 = 'Aprovados'
        drop1 = dffP4['AP']/dffP4['Num Alunos']

    elif drop1 == 'RM':
        var = drop1
        var2 = 'Reprovados por média'
        drop1 = dffP4['RM']/dffP4['Num Alunos']

    elif drop1 == 'RF':
        var = drop1
        var2 = 'Reprovados por falta'
        drop1 = dffP4['RF']/dffP4['Num Alunos']

    elif drop1 == 'RMF':
        var = drop1
        var2 = 'Reprovados por média e falta'
        drop1 = dffP4['RMF']/dffP4['Num Alunos']




    figpg4 = px.line(dffP4, x='Ano e período', y=drop1, color='Disciplina', symbol='Disciplina',
                     markers=True, hover_name='Disciplina',
                     hover_data={
                         'Disciplina': False,
                         'Professor': True,
                         'Ano e período': False,
                         'Aprovados': (':.0%', dffP4['AP']/dffP4['Num Alunos']),
                     })



    # Tornando os números do eixo y em formato de porcentagem

    if var != 'Média turma':
        figpg4.update_layout(
            yaxis_tickformat='.0%',
            yaxis_title=var2),


    if var == 'AP':
        figpg4.update_traces(
            hovertemplate='<br>'.join([
                'Avaliação professor: %{x}',
                'AP: %{y}',
            ])
        )

    elif var == 'RM':
        figpg4.update_traces(
            hovertemplate='<br>'.join([
                'Avaliação professor: %{x}',
                'RM: %{y}',
            ])
        )

    elif var == 'RF':
        figpg4.update_traces(
            hovertemplate='<br>'.join([
                'Avaliação professor: %{x}',
                'RF: %{y}',
            ])
        )

    elif var == 'RMF':
        figpg4.update_traces(
            hovertemplate='<br>'.join([
                'Avaliação professor: %{x}',
                'RMF: %{y}',
            ])
        )


    return figpg4
#---------------------------------------------------------------------------------



# Importando as bibliotecas
import dash, orjson
from dash import html, dcc, Input, Output, callback
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
    dffP5 = pd.DataFrame(rows)

    # Gerando a opção nula
    if drop2 == 'Nenhuma':
        drop2 = None



    # Transformando os dados no eixo y em uma razão ao invés de número absoluto
    if drop1 == 'Média turma':
        var = drop1
        drop1 = dffP5['Média turma']

    elif drop1 == 'AP':
        var = drop1
        var2 = 'Aprovados'
        drop1 = dffP5['AP']/dffP5['Num Alunos']

    elif drop1 == 'RM':
        var = drop1
        var2 = 'Reprovados por média'
        drop1 = dffP5['RM']/dffP5['Num Alunos']

    elif drop1 == 'RF':
        var = drop1
        var2 = 'Reprovados por falta'
        drop1 = dffP5['RF']/dffP5['Num Alunos']

    elif drop1 == 'RMF':
        var = drop1
        var2 = 'Reprovados por média e falta'
        drop1 = dffP5['RMF']/dffP5['Num Alunos']



    # Criando o gráfico
    figfigpg5 = px.scatter(dffP5, x='Avaliação professor', y=drop1, color='Professor', trendline=drop2,
                     hover_name='Professor',
                     hover_data={
                         'Disciplina': False,
                         'Professor': False,
                         'Avaliação professor': ':.2f',
                     },
                     )


    # Tornando os números do eixo y em formato de porcentagem

    if var != 'Média turma':
        figfigpg5.update_layout(
            yaxis_tickformat='.0%',
            yaxis_title=var2),


    if var == 'AP':
        figfigpg5.update_traces(
            hovertemplate='<br>'.join([
                'Avaliação professor: %{x}',
                'AP: %{y}',
            ])
        )

    elif var == 'RM':
        figfigpg5.update_traces(
            hovertemplate='<br>'.join([
                'Avaliação professor: %{x}',
                'RM: %{y}',
            ])
        )

    elif var == 'RF':
        figfigpg5.update_traces(
            hovertemplate='<br>'.join([
                'Avaliação professor: %{x}',
                'RF: %{y}',
            ])
        )

    elif var == 'RMF':
        figpg5.update_traces(
            hovertemplate='<br>'.join([
                'Avaliação professor: %{x}',
                'RMF: %{y}',
            ])
        )

    return figpg5
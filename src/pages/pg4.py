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
exec(open(filename, encoding="utf-8").read())







layout = \
html.Div([
    html.Div(id='pg4grid'),

    html.Br(),

    # Gráfico
    html.Div([
        dcc.Graph(id='timeseries')
    ])

])






#--------------------------------------------------------------------------
@callback(
    Output('pg4grid', 'children'),
    Input('Dados_turmas', 'data'),
)


def Grid_maker(Turmas_df):
    grid = dag.AgGrid(
        id='grid3',
        rowData=Turmas_df,
        columnDefs=clndef,
        defaultColDef=dfclndef,
        dashGridOptions={'pagination': True},
    )

    return grid





#--------------------------------------------------------------------------------
@callback(
    Output(component_id='timeseries', component_property='figure'),
    Input(component_id='grid3', component_property='virtualRowData'),
    Input(component_id='dropdown41', component_property='value'),
    prevent_initial_call=True
)


def filterdata(rows, drop1):


    dffP4 = pd.DataFrame(rows)



    # Transformando os dados no eixo y em uma razão ao invés de número absoluto
    if drop1 == 'Med turma':
        var = drop1
        drop1 = dffP4['Med turma']

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




    fig = px.line(dffP4, x='Turma', y=drop1, color='Disciplina', symbol='Disciplina',
                     markers=True, hover_name='Disciplina',
                     hover_data={
                         'Disciplina': False,
                         'Professor': True,
                         'Turma': False,
                         'Aprovados': (':.0%', dffP4['AP']/dffP4['Num Alunos']),
                     })


    fig.update_xaxes(rangeslider_visible=True)

    # Tornando os números do eixo y em formato de porcentagem

    if var != 'Med turma':
        fig.update_layout(
            yaxis_tickformat='.0%',
            yaxis_title=var2),


    if var == 'AP':
        fig.update_traces(
            hovertemplate='<br>'.join([
                'Aprovados: %{y}',
                'Turma: %{x}',
            ])
        )

    elif var == 'RM':
        fig.update_traces(
            hovertemplate='<br>'.join([
                'Reprovados por média: %{y}',
                'Turma: %{x}',
            ])
        )

    elif var == 'RF':
        fig.update_traces(
            hovertemplate='<br>'.join([
                'Reprovados por falta: %{y}',
                'Turma: %{x}',
            ])
        )

    elif var == 'RMF':
        fig.update_traces(
            hovertemplate='<br>'.join([
                'Reprovados por média e falta: %{y}',
                'Turma: %{x}',
            ])
        )


    return fig



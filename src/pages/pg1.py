# Importando as bibliotecas
import dash
from dash import html, dcc, Input, Output, callback
from dash.dash_table.Format import Format, Scheme
import dash_ag_grid as dag


import io
from io import BytesIO
import base64


import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff

import pandas as pd
import numpy as np
import openpyxl




# Iniciando o aplicativo
dash.register_page(__name__, name='Distribuição de notas', path='/')


filename = 'Reusables/Grid.py'
exec(open(filename).read())





# Layout da página

layout = \
    html.Div([
        html.Div([
            grid
        ]),

        # Menus de dropdown
        html.Div([
            html.Div([
                "Divisão por cores:",
                dcc.Dropdown(id='dropdown11', value='Nenhuma', options=op1, clearable=False),
            ]),

            html.Div([
                "Divisão por coluna:",
                dcc.Dropdown(id='dropdown12', value='Nenhuma', options=op2, clearable=False),
            ]),

            html.Div([
                "Tipo de gráfico:",
                dcc.Dropdown(id='dropdown13', value='kde', options=[
                    {'label': 'KDE', 'value': 'kde'},
                    {'label': 'Histograma', 'value': 'hist'},
                    {'label': 'Cumulativo', 'value': 'ecdf'}], clearable=False),
            ]),

            html.Div([
                "Tipo de agrupamento:",
                dcc.Dropdown(id='dropdown14', value='layer', options=[
                    {'label': 'Normal', 'value': 'layer'},
                    {'label': 'Empilhar', 'value': 'stack'}], clearable=False),
            ])
        ], style={'display': 'flex', 'flexDirection': 'row', 'gap': 50, 'flex': 1}),

        # Gráfico
        html.Div([
            html.Div([
                html.Img(id='matplot')
                # É necessário utilizar html.Img ao invés de dcc.Graph, pois o gráfico foi gerado pelo matplotlib e não pelo Plotly
            ])
        ])

    ])


# Layout do dash


# -------------------------------------------------------------------------------------
@callback(
    Output(component_id='matplot', component_property='src'),
    Output(component_id='dropdown14', component_property='disabled'),
    Input(component_id='grid', component_property='virtualRowData'),
    Input(component_id='dropdown11', component_property='value'),
    Input(component_id='dropdown12', component_property='value'),
    Input(component_id='dropdown13', component_property='value'),
    Input(component_id='dropdown14', component_property='value')
)



def matplot_html(rows, drop1, drop2, drop3, drop4):
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


    # Gerando o gráfico 1 de acordo com a escolha no dropdown 3
    if drop3 == 'ecdf':
        fig = sns.displot(data=dff, x='Média aluno', hue=drop1, col=drop2, kind=f'{drop3}')
        Disdrop4 = True
    else:
        fig = sns.displot(data=dff, x='Média aluno', hue=drop1, col=drop2, kind=f'{drop3}', multiple=f'{drop4}')
        Disdrop4 = False

    # Criando o buffer temporário para renderizar um gráfico do matplotlib no Dash
    buf = BytesIO()
    fig.savefig(buf, format='png')
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_matplot = f'data:image/png;base64,{fig_data}'

    # Retorno dos outputs para o callback
    return fig_matplot, Disdrop4

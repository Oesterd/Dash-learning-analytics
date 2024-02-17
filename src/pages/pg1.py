# Importando as bibliotecas
import dash, orjson
from dash import html, dcc, Input, Output, callback, clientside_callback
import dash_ag_grid as dag


import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import numpy as np
import openpyxl


# Iniciando o aplicativo
dash.register_page(__name__, name='Distribuição de notas', path='/')


filename = 'Reusables/Dist_notas.py'
exec(open(filename).read())




Ops = {
   'Nenhuma': ['Nenhuma', 'Sexo', 'Escola', 'Etnia'],
   'Sexo': ['Nenhuma', 'Escola', 'Etnia'],
   'Escola': ['Nenhuma', 'Sexo', 'Etnia'],
   'Etnia': ['Nenhuma', 'Sexo', 'Escola']
}



# Layout da página

layout = \
    html.Div([
        html.Div(id='pg1grid'),


        # Menus de dropdown
        html.Div([


            html.Div([
                'Escolha o eixo x:',
                dcc.Dropdown(id='dropdown11', value='Med aluno', options=['Med aluno', 'Resultado'], clearable=False)
            ]),


            html.Div([
                "Divisão por cores:",
                dcc.Dropdown(id='dropdown12', value='Nenhuma', options=['Nenhuma', 'Professor'], clearable=False),
            ]),


            html.Div([
                "Divisão por colunas:",
                dcc.Dropdown(list(Ops.keys()), 'Nenhuma', id='dropdown13', clearable=False),
            ]),


            html.Div([
                "Divisão por linhas:",
                dcc.Dropdown(id='dropdown14', value='Nenhuma', options=['Nenhuma', 'Sexo', 'Etnia', 'Escola'], clearable=False),
            ]),


            html.Div([
                "Tipo de gráfico:",
                dcc.Dropdown(id='dropdown15', value='Histograma', options=['Histograma', 'Cumulativo'], clearable=False),
            ]),


            html.Div([
                'Tipo de normalização:',
                dcc.Dropdown(id='dropdown16', value='Nenhuma', options=[
                    {'label': 'Nenhuma', 'value': 'Nenhuma'},
                    {'label': 'Porcentagem', 'value': 'percent'},
                    {'label': 'Densidade de probabilidade', 'value': 'probability density'},
                ], clearable=False)
            ], style={'width': '20%'}),

            # html.Div([
            #     "Tipo de agrupamento:",
            #     dcc.Dropdown(id='dropdown14', value='layer', options=[
            #         {'label': 'Normal', 'value': 'layer'},
            #         {'label': 'Empilhar', 'value': 'stack'}], clearable=False),
            # ])
        ], style={'display': 'flex', 'flexDirection': 'row', 'gap': 50, 'flex': 1}),

        # Gráfico
        html.Div([
                dcc.Graph(id='displot')
        ])

    ])



# -------------------------------------------------------------------------------------
# Chained callback
@callback(
    Output('dropdown14', 'options'),
    Input('dropdown13', 'value'),
    prevent_initial_call=True
)


def drop_chain(drop4value):
    return [{'label': i, 'value': i} for i in Ops[drop4value]]


@callback(
    Output('dropdown14', 'value'),
    Input('dropdown14', 'options'),
    prevent_initial_call = True
)

def drop4init(available_options):
    return available_options[0]['value']





# -------------------------------------------------------------------------------------
@callback(
    Output('pg1grid', 'children'),
    Input('Dados_notas', 'data'),
)


def Grid_maker(Notas_df):
    grid = dag.AgGrid(
        id='grid',
        rowData=Notas_df,
        columnDefs=clndef,
        defaultColDef=dfclndef,
        dashGridOptions={'pagination': True},
    )

    return grid






@callback(
    Output(component_id='displot', component_property='figure'),
    Output(component_id='dropdown15', component_property='options'),
    Input(component_id='grid', component_property='virtualRowData'),
    Input(component_id='dropdown11', component_property='value'),
    Input(component_id='dropdown12', component_property='value'),
    Input(component_id='dropdown13', component_property='value'),
    Input(component_id='dropdown14', component_property='value'),
    Input(component_id='dropdown15', component_property='value'),
    Input(component_id='dropdown16', component_property='value'),
    prevent_initial_call=True
)



def matplot_html(rows, drop1, drop2, drop3, drop4, drop5, drop6):

## Criando o gráfico

    # Modificando os dados conforme a filtragem do usuário
    dff = pd.DataFrame(rows)


    ## Automatizando os ifs (em teste)
    # for i in range(3):
    #
    #     if locals()[f'drop{i+2}'] == 'Nenhuma':
    #         locals()[f'drop2'] = 56
    #         test = f'IfTest{i+2}'
    #         print(locals()[f'drop{i+2}'], test)
    #     else:
    #         locals()[f'drop{i+2}'] = locals()[f'drop{i+2}']
    #         test = f'ElseTest{i + 2}'
    #         print(locals()[f'drop{i+2}'], test)
    #
    #
    # print(drop2,drop3,drop4, 'Direct vars', end='\n')


    if drop2 == 'Nenhuma':
        drop2 = None
    else:
        drop2 = f'{drop2}'


    if drop3 == 'Nenhuma':
        drop3 = None
    else:
        drop3 = f'{drop3}'


    if drop4 == 'Nenhuma':
        drop4 = None
    else:
        drop4 = f'{drop4}'

    if drop6 == 'Nenhuma':
        drop6 = None
    else:
        drop6 = f'{drop6}'


    if drop1 == 'Med aluno':
        drop5val = ['Histograma', 'Cumulativo']
    else:
        drop5val = ['Histograma']
        drop5 = 'Histograma'

    if drop5 == 'Cumulativo':
        drop5 = True
    else:
        drop5 = False




    fig = px.histogram(dff, x=drop1, color=drop2, facet_col=drop3, facet_row=drop4, cumulative=drop5, histnorm=drop6, barmode='group')


    return fig, drop5val

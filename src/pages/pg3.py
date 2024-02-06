# Importando as bibliotecas
import dash, orjson
from dash import html, dcc, Input, Output, callback
import dash_ag_grid as dag


import plotly.express as px
import pandas as pd
import numpy as np
import scipy.stats






dash.register_page(__name__, name='Correlação')





filename = 'Reusables/Dist_notas.py'
exec(open(filename).read())



Ops = {
   'Nenhuma': ['Nenhuma', 'Sexo', 'Escola'],
   'Sexo': ['Nenhuma', 'Escola'],
   'Escola': ['Nenhuma', 'Sexo'],
   'Etnia': ['Nenhuma', 'Sexo', 'Escola']
}




layout = \
html.Div([
    html.Div([
        grid
    ]),



    # Menus de dropdown
    html.Div([

        html.Div([
            "Escolha o eixo x:",
            dcc.Dropdown(
                id='dropdown30',
                value='Renda (R$)',
                options=['Renda (R$)', 'Freq'],
                clearable=False
            ),
        ]),


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
            dcc.Dropdown(id='dropdown32', value='Nenhuma', options=['Nenhuma', 'Sexo', 'Escola'], clearable=False),
        ]),


        html.Div([
            "Regressão linear:",
            dcc.Dropdown(id='dropdown33', value='Nenhuma', options=[
                {'label': 'Nenhuma', 'value': 'Nenhuma'},
                {'label': 'Linear', 'value': 'ols'},
                {'label': 'Pesada', 'value': 'lowess'}
            ], clearable=False)
        ]),


        html.Div([
            "Escopo da regressão linear:",
            dcc.Dropdown(id='dropdown34', value='Legenda', options=[
                {'label': 'Legenda', 'value': 'trace'},
                {'label': 'Geral', 'value': 'overall'},
            ], clearable=False)
        ])
    ], style={'display': 'flex', 'flexDirection': 'row', 'gap': 50, 'flex': 1}),

    html.Br(),


    html.Div([
        # Gráfico
        html.Div([
            dcc.Graph(id='scatter')
        ], style={'flex-basis': 800}),

        # Valores de correlação
        html.Div([
            dcc.Textarea(
                id='textpg3',
                disabled=True,
                className='textarea'
            )
        ], style={'position': 'relative', 'left': 75, 'top': 100}),

    ], style={'display': 'flex', 'flexDirection': 'row', 'gap': 20, 'flex': 1}),





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
    Output(component_id='textpg3', component_property='value'),
    Input(component_id='grid', component_property='virtualRowData'),
    Input(component_id='dropdown30', component_property='value'),
    Input(component_id='dropdown31', component_property='value'),
    Input(component_id='dropdown32', component_property='value'),
    Input(component_id='dropdown33', component_property='value'),
    Input(component_id='dropdown34', component_property='value'),
)


def scatter_plot(rows, drop0, drop1, drop2, drop3, drop4):


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



    fig = px.scatter(dff, x=f'{drop0}', y='Med aluno', color='Professor', facet_col=drop1, facet_row=drop2, trendline=drop3, trendline_scope=drop4)



    # Valores de correlação

    x = dff[drop0]
    y = dff['Med aluno']

    r = y.corr(x, method='pearson')
    r2 = y.corr(x, method='spearman')
    r3 = y.corr(x, method='kendall')

    result = scipy.stats.linregress(x, y)

    p = result.pvalue
    desp = result.stderr

    text = f'O valor do coeficiente de correlação é: \nPearson = {r:.3f} \nSpearman = {r2:.3f} \nKendall = {r3:.3f} \n\nO valor-p é: {p:.3f} \nO desvio padrão é: {desp:.3e}'

    return fig, text
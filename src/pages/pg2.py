# Importando as bibliotecas
import dash, orjson
from dash import html, dcc, Input, Output, State, callback, clientside_callback
import dash_ag_grid as dag


import plotly.express as px
import pandas as pd
import numpy as np
import scipy.stats






dash.register_page(__name__, name='Correlação')





filename = 'Reusables/Dist_notas.py'
exec(open(filename, encoding="utf-8").read())



# Não remover, é necessário para o callback em cadeia
Ops = {
   'Nenhuma': ['Nenhuma', 'Sexo', 'Escola', 'Etnia'],
   'Sexo': ['Nenhuma', 'Escola', 'Etnia'],
   'Escola': ['Nenhuma', 'Sexo', 'Etnia'],
   'Etnia': ['Nenhuma', 'Sexo', 'Escola']
}



layout = \
html.Div([
    html.Div(id='pg3grid'),

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
# Chained callback
@callback(
    Output('dropdown22', 'options'),
    Input('dropdown21', 'value'),
)


def drop_chain(drop21value):
    return [{'label': i, 'value': i} for i in Ops[drop21value]]


@callback(
    Output('dropdown22', 'value'),
    Input('dropdown22', 'options'),
)

def drop4init(available_options):
    return available_options[0]['value']









#---------------------------------------------------------------------------------
@callback(
    Output('pg3grid', 'children'),
    Input('Dados_notas', 'data'),
)


def Grid_maker(Notas_df):
    grid = dag.AgGrid(
        id='grid2',
        rowData=Notas_df,
        columnDefs=clndef,
        defaultColDef=dfclndef,
        dashGridOptions={'pagination': True},
    )

    return grid





@callback(
    Output(component_id='scatter', component_property='figure'),
    Output(component_id='textpg3', component_property='value'),
    Input(component_id='grid2', component_property='virtualRowData'),
    Input(component_id='dropdown20', component_property='value'),
    Input(component_id='dropdown21', component_property='value'),
    Input(component_id='dropdown22', component_property='value'),
    Input(component_id='dropdown23', component_property='value'),
    Input(component_id='dropdown24', component_property='value'),
    prevent_initial_call=True
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

    text = f'Coeficiente de correlação:\nPearson = {r:.3f} \nSpearman = {r2:.3f} \nKendall = {r3:.3f} \n\nValor-p: {p:.3f} \nDesvio padrão: {desp:.3e}'

    return fig, text
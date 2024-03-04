# Importando as bibliotecas
import dash
from dash import html, dcc, Input, Output, State, callback, clientside_callback, ctx
import dash_ag_grid as dag
from dash.exceptions import PreventUpdate


import plotly.express as px
import pandas as pd
import scipy.stats

import time



# Iniciando o aplicativo
dash.register_page(__name__, name='Correlação')


filename = 'Reusables/Dist_notas.py'
exec(open(filename, encoding="utf-8").read())




grid = dag.AgGrid(
    id='grid2',
    rowData=[],
    columnDefs=clndef,
    defaultColDef=dfclndef,
    dashGridOptions={'pagination': True},
    style={'height': '400px'}
)




# ----------------------------------- Layout da página ---------------------------------------------------
layout = \
    html.Div([

        html.Div([
            grid
        ]),

        html.Br(),



        html.Div([
            # Gráfico
            html.Div([
                dcc.Graph(id='scatter')
            ], style={'flex-basis': 800}),

            # Valores de correlação
            html.Div([
                dcc.Textarea(
                    id='textpg2',
                    disabled=True,
                    className='textarea'
                )
            ], style={'position': 'relative', 'left': 75, 'top': 100}),

        ], style={'display': 'flex', 'flexDirection': 'row', 'gap': 20, 'flex': 1}),

    ])







#--------------------------------------------------------------------------------------------
# Callback em cadeia
@callback(
    Output('dropdown22', 'data'),
    Input('dropdown21', 'value'),
    prevent_initial_call=True
)


def drop_chain(drop21value):
    print("Callback21:", ctx.triggered_id)
    return [{'label': i, 'value': i} for i in Ops[drop21value]]


@callback(
    Output('dropdown22', 'value'),
    Input('dropdown22', 'data'),
    prevent_initial_call=True
)

def drop4init(available_options):
    return available_options[0]['value']









#---------------------------------------------------------------------------------
@callback(
    Output('grid2', 'rowData'),
    Input('Dados_notas', 'data'),
)


def Grid_maker(data):
    return data





@callback(
    Output(component_id='scatter', component_property='figure'),
    Output(component_id='textpg2', component_property='value'),
    Input(component_id='Intervalo2', component_property='n_intervals'),
    Input(component_id='grid2', component_property='virtualRowData'),
    Input(component_id='dropdown20', component_property='value'),
    Input(component_id='dropdown21', component_property='value'),
    Input(component_id='dropdown22', component_property='value'),
    Input(component_id='dropdown23', component_property='value'),
    Input(component_id='dropdown24', component_property='value'),
    prevent_initial_call=True
)


def scatter_plot(n, rows, drop0, drop1, drop2, drop3, drop4):

    # Evitando que o Output seja atualizado enquanto os Inputs ainda não estão presente no layout
    if not rows:
        raise PreventUpdate



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



    fig = px.scatter(
        dff, x=f'{drop0}', y='Média aluno',
        color='Professor', facet_col=drop1, facet_row=drop2,
        trendline=drop3, trendline_scope=drop4
    )



    # Valores de correlação
    x = dff[drop0]
    y = dff['Média aluno']

    r = y.corr(x, method='pearson')
    r2 = y.corr(x, method='spearman')
    r3 = y.corr(x, method='kendall')

    result = scipy.stats.linregress(x, y)

    p = result.pvalue
    desp = result.stderr

    text = f'Coeficiente de correlação:\nPearson = {r:.3f} \nSpearman = {r2:.3f} \nKendall = {r3:.3f} \n\nValor-p: {p:.3f} \nDesvio padrão: {desp:.3e}'

    return fig, text
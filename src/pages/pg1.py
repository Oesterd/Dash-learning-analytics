# Importando as bibliotecas
import dash
from dash import html, dcc, Input, Output, State, callback, clientside_callback, ctx
import dash_ag_grid as dag
from dash.exceptions import PreventUpdate


import plotly.express as px
import pandas as pd





# Iniciando o aplicativo
dash.register_page(__name__, name='Distribuição de notas', path='/')


filename = 'Reusables/Dist_notas.py'
exec(open(filename, encoding="utf-8").read())




grid = dag.AgGrid(
    id='grid',
    rowData=[],
    columnDefs=clndef,
    defaultColDef=dfclndef,
    dashGridOptions={'pagination': True},
    style={'height': '400px'}
)




# ----------------------------------- Layout da página ---------------------------------------------------
layout = \
    html.Div([
        # Grid
        html.Div([
            grid
        ]),

        # Gráfico
        html.Div([
            dcc.Graph(id='displot')
        ])

    ])






# -------------------------------------------------------------------------------------
# Callback em cadeia
@callback(
    Output('dropdown14', 'data'),
    Output('dropdown15', 'data'),
    Input('dropdown13', 'value'),
    Input('dropdown11', 'value'),
)


def drop_chain(drop13value, drop11value):
    data14 = [{'label': i, 'value': i} for i in Ops[drop13value]]
    data15 = [{'label': i, 'value': i} for i in Ops2[drop11value]]
    return data14, data15


@callback(
    Output('dropdown14', 'value'),
    Output('dropdown15', 'value'),
    Input('dropdown14', 'data'),
    Input('dropdown15', 'data'),
)

def drop4init(options14, options15):
    value14 = options14[0]['value']
    value15 = options15[0]['value']
    return value14, value15




# -------------------------------------------------------------------------------------
@callback(
    Output('grid', 'rowData'),
    Input('Dados_notas', 'data'),
)


def Grid_maker(data):
    return data



#-------------------------------------------------------------------------
@callback(
    Output(component_id='displot', component_property='figure'),
    Input(component_id='Intervalo2', component_property='n_intervals'),
    Input(component_id='grid', component_property='virtualRowData'),
    Input(component_id='dropdown11', component_property='value'),
    Input(component_id='dropdown12', component_property='value'),
    Input(component_id='dropdown13', component_property='value'),
    Input(component_id='dropdown14', component_property='value'),
    Input(component_id='dropdown15', component_property='value'),
    Input(component_id='dropdown16', component_property='value'),
    prevent_initial_call=True
)



def matplot_html(n, rows, drop1, drop2, drop3, drop4, drop5, drop6):

    # Evitando que o Output seja atualizado enquanto os Inputs ainda não estão presente no layout
    if not rows:
        raise PreventUpdate

    # Modificando os dados conforme a filtragem do usuário
    dff = pd.DataFrame(rows)


    if drop3 == 'Nenhuma':
        drop3 = None
    else:
        drop3 = f'{drop3}'


    if drop4 == 'Nenhuma':
        drop4 = None
    else:
        drop4 = f'{drop4}'


    if drop5 == 'Cumulativo':
        drop5 = True
    else:
        drop5 = False




    fig = px.histogram(
        dff, x=drop1,
        color=drop2, facet_col=drop3, facet_row=drop4,
        cumulative=drop5, histnorm=drop6, barmode='group'
    )


    return fig
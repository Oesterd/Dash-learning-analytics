import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_ag_grid as dag


import plotly.express as px
import plotly.graph_objects as go


import pandas as pd



dash.register_page(__name__, name='DAG + Text (V.RowData)')


df = px.data.tips()






datatable = dash_table.DataTable(
        id='dashtable',
        columns=[{'name': i, 'id': i} for i in df.columns],
        page_size=8,
        data=df.to_dict('records')
)




grid = dag.AgGrid(
        id='daggrid',
        rowData=df.to_dict('records'),
        columnDefs=[{'field':i} for i in df.columns]
    )



layout = \
    html.Div([
        html.Div([
            grid
        ]),

        html.Button('Submit', id='button2', n_clicks=0),


        html.Div(id='plot-div2', children=[
            dcc.Textarea(id='dcctext',
                         style={'width': 800, 'height': 300})
        ]),

    ])


@callback(
    Output('dcctext', 'value'),
    Input('button2', 'n_clicks'),
    State('daggrid', 'virtualRowData'),
    prevent_initial_call=True
)

def filter_data(n, rows):


    dff = pd.DataFrame(rows)

    fig = px.line(dff, x='total_bill', y='tip')

    return f'The virtual rowData is:\n\n {rows}'

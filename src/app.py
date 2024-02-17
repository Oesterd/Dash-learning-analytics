import dash, orjson
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from flask_caching import Cache
import os
import pandas as pd


app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB], suppress_callback_exceptions=True)
server = app.server


Dados_notas = pd.read_excel('https://github.com/Oesterd/Dash-learning-analytics/raw/master/dados_teste.xlsx')
Notas_df = Dados_notas.iloc[:, 0:10]
Notas_df = Notas_df.to_dict('records')


Turmas_df = pd.read_excel('https://github.com/Oesterd/Dash-learning-analytics/raw/master/Dados_turma.xlsx')
Turmas_df = Turmas_df.to_dict('records')




cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

TIMEOUT = 60



sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div("Estatísticas acadêmicas",
                         style={'fontSize': 50, 'textAlign': 'center'}))
    ]),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    ),

    dcc.Store(id='Dados_notas', data=Notas_df),
    dcc.Store(id='Dados_turma', data=Turmas_df),
], fluid=True)


if __name__ == "__main__":
    app.run(debug=True)

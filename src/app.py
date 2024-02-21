import dash, orjson
from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify


import pandas as pd


app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)
server = app.server


Dados_notas = pd.read_excel('https://github.com/Oesterd/Dash-learning-analytics/raw/master/dados_teste.xlsx')
Notas_df = Dados_notas.iloc[:, 0:10]
Notas_df = Notas_df.to_dict('records')


Turmas_df = pd.read_excel('https://github.com/Oesterd/Dash-learning-analytics/raw/master/Dados_turma.xlsx')
Turmas_df = Turmas_df.to_dict('records')



pgheight = 40*len(dash.page_registry.values())

page = list(dash.page_registry.values())


menu1 = dmc.Menu(
    [
        dmc.MenuTarget(dmc.Button('Notas')),
        dmc.MenuDropdown(
            [
                dmc.MenuItem(
                    'Distribuição',
                    href=page[0]['path'],
                ),

                dmc.MenuItem(
                    'Correlação',
                    href=page[1]['path'],
                ),
            ]
        )
    ]
)



menu2 = dmc.Menu(
    [
        dmc.MenuTarget(dmc.Button('Turmas')),
        dmc.MenuDropdown(
            [
                dmc.MenuItem(
                    'Professores',
                    href=page[2]['path'],
                ),

                dmc.MenuItem(
                    'Linha do tempo',
                    href=page[3]['path'],
                ),

                dmc.MenuItem(
                    'Avaliação',
                    href=page[4]['path'],
                ),
            ]
        )
    ]
)



gitlink = dmc.Anchor(
    dmc.ActionIcon(
        DashIconify(icon='formkit:github', width=30, inline=False, color='black'),
        size=40,
    ),
    href='https://github.com/Oesterd/Dash-learning-analytics',
    target='_blank',
)







app.layout = dmc.Container([
    dmc.Grid(
        children=[
                dmc.Col(
                    html.Div(["Estatísticas acadêmicas"],
                                 style={'fontSize': 30, 'textAlign': 'left'}),
                    span='content'),

                dmc.Col(menu1, span='content', offset=3),
                dmc.Col(menu2, span='content'),
                dmc.Col(gitlink, span='content', offset=1),
            ]
    ),

    html.Hr(),

    dash.page_container,

    dcc.Store(id='Dados_notas', data=Notas_df),
    dcc.Store(id='Dados_turmas', data=Turmas_df),
], fluid=True)


if __name__ == "__main__":
    app.run(debug=True)

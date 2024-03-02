import dash
from dash import Dash, html, dcc, callback, Input, Output, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify


import pandas as pd


app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)
server = app.server


page = list(dash.page_registry.values())


menu1 = dmc.Menu(
    [
        dmc.MenuTarget(dmc.Button('Notas',
                                  variant='default',
                                  color='gray')
        ),

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
        dmc.MenuTarget(dmc.Button('Turmas',
                                  variant='default',
                                  color='gray')
        ),

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



navwidth = '0px'


#----------------------------------------------------------------------------------------------------
app.layout = html.Div(
    children=[

        html.Div([
            dmc.Grid(
                children=[
                    dmc.Col(
                        dmc.Burger(id='sidebar-button'),
                        span='content'
                    ),

                    dmc.Col(
                        html.Div(
                            children=[
                                "Estatísticas acadêmicas"
                            ],
                            style={'fontSize': 30, 'textAlign': 'left'}),
                        span='content', offset=2),

                    dmc.Col(menu1, span='content', offset=0),
                    dmc.Col(menu2, span='content'),
                    dmc.Col(gitlink,
                            span='content',
                            style={'position': 'fixed', 'right': 0, 'top': -5}),
                ],
                style={'background-color': '#20B2AA',
                       'height': '50px', 'width': '100vw'},
                id='Header'
            ),

            ],
        ),





        html.Div(
            children=[
                dmc.MantineProvider(
                    inherit=True,
                    theme={
                      'components': {
                          'Select': {
                              'styles': {
                                  'root': {'width': '95%'}
                              }
                          }
                      }
                    },
                    children=[
                        dmc.Navbar(
                            id='sidebar',
                            fixed=False,
                            hidden=True,
                            width={"base": navwidth},
                            position='right',
                            style={
                                "overflow": "hidden",
                                "transition": "width 0.3s ease-in-out",
                                "background-color": "#f4f6f9",
                            },
                        ),
                    ]
                ),

                html.Div(
                    children=[
                        dash.page_container
                    ],
                    id='dash-container',
                    style={
                        "width": "100vw",
                        "margin": "0",
                        "maxWidth": "100vw", "overflow": "hidden", 'flexShrink': '1', "maxHeight": "100%"
                    }
                ),
            ],
            style={"display": "flex", "gap": 10,
                   "maxWidth": "100vw", "overflow": "hidden", "maxHeight": "100%",
                   "position": "relative", "left": 0},
            id="Navbar+Content"
        ),

        dcc.Interval(id='Intervalo', interval=86400000*7, n_intervals=0),
        dcc.Store(id='Dados_notas', data={}),
        dcc.Store(id='Dados_turmas', data={}),
        dcc.Location(id='url', refresh=True),
    ],
    style={"display": "flex", "flexDirection": "column", "flexGrow": "1", "gap": 10,
           "overflow": "visible", "maxHeight": "100%", "maxWidth": "100%", "width": "100vw"},
    id="overall-container"
)







#---------------------------------------------------------------------------------------------------------
filename = 'Reusables/Sidebars.py'
exec(open(filename, encoding="utf-8").read())

@app.callback(
    Output('Dados_notas', 'data'),
    Output('Dados_turmas', 'data'),
    Input('Intervalo', 'n_intervals'),
)
def gather_data(n_intervals):

    Sheet_notas = '1v6EpUTIYBQF5Sv8lQrHKbK9IJh9mjiaXfUv3rLzliUE'
    Sheet_turmas = '1ZCvar1Hb82foVQHUOMPn7z4YHmvNXICIiF0HIF3Qurk'

    Dados_notas = pd.read_excel(f'https://docs.google.com/spreadsheets/d/{Sheet_notas}/export?format=xlsx')
    Notas_df = Dados_notas.iloc[:, 0:10]
    Notas_df = Notas_df.to_dict('records')

    Turmas_df = pd.read_excel(f'https://docs.google.com/spreadsheets/d/{Sheet_turmas}/export?format=xlsx')
    Turmas_df = Turmas_df.to_dict('records')

    print(Turmas_df)

    return Notas_df, Turmas_df




@callback(
    Output('sidebar', 'children'),
    Input('url', 'pathname'),
)
def nav_content(url):


    content = {
        '/': pg1(),
        '/pg2': pg2(),
        '/pg3': pg3(),
        '/pg4': pg4(),
        '/pg5': pg5(),
    }.get(url)


    return content







@app.callback(
    Output("sidebar", "width"),
    Input("sidebar-button", "opened"),
    State("sidebar", "width"),
    prevent_initial_call=True,
)
def drawer_demo(opened, width):

    if width["base"] == navwidth:
        return {"base": 250}
    else:
        return {"base": navwidth}


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")

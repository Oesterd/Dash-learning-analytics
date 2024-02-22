import dash, orjson
from dash import Dash, html, dcc, callback, Input, Output, State
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



navwidth = 1


#----------------------------------------------------------------------------------------------------
app.layout = dmc.Container(
    children=[
        html.Div(id='nav-div',
                 children=[
                     dmc.Navbar(
                         id='sidebar',
                         fixed=False,
                         hidden=True,
                         width={"base": navwidth},
                         position='right',
                         children=[],
                         style={
                             "overflow": "hidden",
                             "transition": "width 0.3s ease-in-out",
                             "background-color": "#f4f6f9",
                         },
                     ),
                 ]
        ),



        dmc.Container(
            children=[
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
                        dmc.Col(gitlink, span='content', offset=3),
                ]),



                html.Hr(),

                dmc.Container(
                    children=[
                        dash.page_container
                    ],
                    id='dash-container',
                    p=0,
                    fluid=True,
                    style={
                        "width": "100%",
                        "margin": "0",
                        "maxWidth": "100%", "overflow": "auto", 'flexShrink': '1', "maxHeight": "100%"
                    }
                ),
            ],
            size="100%",
            p=0,
            m=0,
            style={"display": "flex", "maxWidth": "100vw", "overflow": "hidden",
                   "flexGrow": "1", "maxHeight": "100%", "flexDirection": "column"},
            id="content-container"
        ),


        dcc.Store(id='Dados_notas', data=Notas_df),
        dcc.Store(id='Dados_turmas', data=Turmas_df),
        dcc.Location(id='url', refresh=True),
    ],
    size="100%",
    p=0,
    m=0,
    style={"display": "flex", "maxWidth": "100vw", "overflow": "hidden", "maxHeight": "100vh",
           "position": "absolute", "top": 0, "left": 0, "width": "100vw"},
    id="overall-container"
)



#--------------------------------------------------------------------
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





filename = 'Reusables/Sidebars.py'
exec(open(filename, encoding="utf-8").read())



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


if __name__ == "__main__":
    app.run(debug=True)

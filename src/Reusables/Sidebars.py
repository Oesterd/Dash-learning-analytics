Ops = {
   'Nenhuma': ['Nenhuma', 'Sexo', 'Escola', 'Etnia'],
   'Sexo': ['Nenhuma', 'Escola', 'Etnia'],
   'Escola': ['Nenhuma', 'Sexo', 'Etnia'],
   'Etnia': ['Nenhuma', 'Sexo', 'Escola']
}

Opcs = ['Med turma', 'AP', 'RM', 'RF', 'RMF']


def pg1():
    content = html.Div(
        children=[
            html.Div(
                [
                    html.H2("Opções", style={"color": "black"}),
                ],
                style={'text-align': 'center'}
            ),

            html.Div([
                'Escolha o eixo x:',
                dcc.Dropdown(id='dropdown11', value='Med aluno', options=['Med aluno', 'Resultado'],
                             clearable=False)
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
                dcc.Dropdown(id='dropdown14', value='Nenhuma', options=['Nenhuma', 'Sexo', 'Etnia', 'Escola'],
                             clearable=False),
            ]),

            html.Div([
                "Tipo de gráfico:",
                dcc.Dropdown(id='dropdown15', value='Histograma', options=['Histograma', 'Cumulativo'],
                             clearable=False),
            ]),

            html.Div([
                'Tipo de normalização:',
                dcc.Dropdown(id='dropdown16', value='Contagem', options=[
                    {'label': 'Contagem', 'value': 'Contagem'},
                    {'label': 'Porcentagem', 'value': 'percent'},
                ], clearable=False)
            ]),

        ],
        style={'display': 'flex', 'flexDirection': 'column', 'gap': 20, 'flex': 1},
    )
    return content


def pg2():
    content = html.Div([
        html.Div(
            [
                html.H2("Opções", style={"color": "black"}),
            ],
            style={'text-align': 'center'}
        ),

        html.Div([
            "Escolha o eixo x:",
            dcc.Dropdown(
                id='dropdown20',
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
                id='dropdown21',
                clearable=False
            ),
        ]),

        html.Div([
            "Divisão por linhas:",
            dcc.Dropdown(id='dropdown22', value='Nenhuma', options=['Nenhuma', 'Sexo', 'Escola'], clearable=False),
        ]),

        html.Div([
            "Regressão linear:",
            dcc.Dropdown(id='dropdown23', value='Nenhuma', options=[
                {'label': 'Nenhuma', 'value': 'Nenhuma'},
                {'label': 'Linear', 'value': 'ols'},
                {'label': 'Pesada', 'value': 'lowess'}
            ], clearable=False)
        ]),

        html.Div([
            "Escopo da regressão linear:",
            dcc.Dropdown(id='dropdown24', value='Legenda',
                options=[
                    {'label': 'Legenda', 'value': 'trace'},
                    {'label': 'Geral', 'value': 'overall'},
                ],
                clearable=False
            )
        ])
        ],
        style={'display': 'flex', 'flexDirection': 'column', 'gap': 20, 'flex': 1}
    ),

    return content


def pg3():
    content = html.Div([
        html.Div(
            [
                html.H2("Opções", style={"color": "black"}),
            ],
            style={'text-align': 'center'}
        ),

    html.Div([
        "Tipo de gráfico:",
        dcc.Dropdown(id='dropdown31', value='stpf', options=
            [
                {'label': 'Situação por professor', 'value': 'stpf'},
                {'label': 'Professor por situação', 'value': 'pfst'}
            ],
            clearable=False
            ),
        ]),
    ])

    return content



def pg4():
    content = html.Div([
        html.Div(
            [
                html.H2("Opções", style={"color": "black"}),
            ],
            style={'text-align': 'center'}
        ),

    html.Div([
            "Escolha o eixo y:",
            dcc.Dropdown(id='dropdown41', value='Med turma', options=Opcs, clearable=False),
    ]),

    ])

    return content



def pg5():
    content = html.Div([
        html.Div(
            [
                html.H2("Opções", style={"color": "black"}),
            ],
            style={'text-align': 'center'}
        ),



    html.Div([
        html.Div([
            "Escolha o eixo y:",
            dcc.Dropdown(id='dropdown51', value='Med turma', options=Opcs, clearable=False),
        ]),



        html.Div([
            "Regressão linear:",
            dcc.Dropdown(id='dropdown52', value='Nenhuma', options=[
                {'label': 'Nenhuma', 'value': 'Nenhuma'},
                {'label': 'Linear', 'value': 'ols'},
                {'label': 'Pesada', 'value': 'lowess'}
            ], clearable=False)
        ]),


        html.Div([
            "Escopo da regressão linear:",
            dcc.Dropdown(id='dropdown53', value='Legenda', options=[
                {'label': 'Legenda', 'value': 'trace'},
                {'label': 'Geral', 'value': 'overall'},
            ], clearable=False)
        ])
    ], style={'display': 'flex', 'flexDirection': 'column', 'gap': 20, 'flex': 1}),

    ])

    return content



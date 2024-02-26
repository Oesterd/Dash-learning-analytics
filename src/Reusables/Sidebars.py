Ops = {
   'Nenhuma': ['Nenhuma', 'Sexo', 'Escola', 'Etnia'],
   'Sexo': ['Nenhuma', 'Escola', 'Etnia'],
   'Escola': ['Nenhuma', 'Sexo', 'Etnia'],
   'Etnia': ['Nenhuma', 'Sexo', 'Escola']
}

Ops2 = {
    'Med aluno': ['Histograma', 'Cumulativo'],
    'Resultado': ['Histograma'],
}



def pg1():
    content = \
        html.Div([
                html.Div(
                    [
                        html.H2("Opções", style={"color": "black"}),
                    ],
                    style={'text-align': 'center'}
                ),

                html.Div([
                    dmc.Select(id='dropdown11', label='Escolha o eixo x', value='Med aluno',
                               data=list(Ops2.keys()), clearable=False),
                    ]
                ),

                html.Div([

                    dmc.Select(id='dropdown12', label='Divisão por cores:', value=None,
                               data=[
                                   {'label': 'Nenhuma', 'value': None},
                                   {'label': 'Professor', 'value': 'Professor'}
                               ], clearable=False),
                    ]
                ),

                html.Div([
                    dmc.Select(data=list(Ops.keys()), label='Divisão por colunas:',  value='Nenhuma',
                               id='dropdown13', clearable=False),
                    ]
                ),

                html.Div([
                    dmc.Select(id='dropdown14', label='Divisão por linhas:',  value='Nenhuma',
                               data=['Nenhuma', 'Sexo', 'Etnia', 'Escola'],
                               clearable=False),
                    ]
                ),

                html.Div([
                    dmc.Select(id='dropdown15', label='Tipo de gráfico:',  value='Histograma',
                               data=['Histograma', 'Cumulativo'],
                                 clearable=False),
                    ]
                ),

                html.Div([
                    dmc.Select(
                        id='dropdown16', label='Tipo de normalização:', value=None,
                        data=[
                        {'label': 'Contagem', 'value': None},
                        {'label': 'Porcentagem', 'value': 'percent'},
                        ],
                        clearable=False
                    )
                ]),
        ],
        style={'display': 'flex', 'flexDirection': 'column', 'gap': 20, 'flex': 1},
        )

    return content


def pg2():
    content = \
        html.Div([
            html.Div(
                [
                    html.H2("Opções", style={"color": "black"}),
                ],
                style={'text-align': 'center'}
            ),

            html.Div([
                html.Div([
                    dmc.Select(id='dropdown20', label='Escolha o eixo x', value='Renda (R$)',
                               data=['Renda (R$)', 'Freq'], clearable=False)
                ]),
            ]),

            html.Div([
                dmc.Select(data=list(Ops.keys()), label='Divisão por colunas:', value='Nenhuma', id='dropdown21', clearable=False),
            ]),

            html.Div([
                dmc.Select(id='dropdown22', label='Divisão por linhas:',  value='Nenhuma', data=['Nenhuma', 'Sexo', 'Escola'], clearable=False),
            ]),

            html.Div([
                dmc.Select(id='dropdown23', label='Regressão linear:', value=None,
                    data=[
                        {'label': 'Nenhuma', 'value': None},
                        {'label': 'Linear', 'value': 'ols'},
                        {'label': 'Pesada', 'value': 'lowess'}
                    ],
                    clearable=False
                )
            ]),

            html.Div([
                dmc.Select(
                    id='dropdown24', label='Escopo da regressão linear:',  value='overall',
                    data=[
                        {'label': 'Geral', 'value': 'overall'},
                        {'label': 'Legenda', 'value': 'trace'},
                    ],
                    clearable=False
                )
            ])
        ],
        style={'display': 'flex', 'flexDirection': 'column', 'gap': 20, 'flex': 1}
        )

    return content


def pg3():
    content = \
        html.Div([
            html.Div(
                [
                    html.H2("Opções", style={"color": "black"}),
                ],
                style={'text-align': 'center'}
            ),

            html.Div([
                dmc.Select(
                    id='dropdown31', label='Tipo de gráfico:',  value='stpf',
                    data=[
                        {'label': 'Situação por professor', 'value': 'stpf'},
                        {'label': 'Professor por situação', 'value': 'pfst'}
                    ],
                    clearable=False
                ),
            ]),
        ])

    return content



def pg4():
    content = \
        html.Div([
            html.Div(
                [
                    html.H2("Opções", style={"color": "black"}),
                ],
                style={'text-align': 'center'}
            ),

            html.Div([
                    dmc.Select(id='dropdown41', label='Escolha o eixo y:',  value='Med turma',
                               data=['Med turma', 'AP', 'RM', 'RF', 'RMF'], clearable=False),
            ]),
            ]
        )

    return content



def pg5():
    content = \
        html.Div([
            html.Div(
                [
                    html.H2("Opções", style={"color": "black"}),
                ],
                style={'text-align': 'center'}
            ),



            html.Div([
                html.Div([
                    dmc.Select(id='dropdown51', label='Escolha o eixo y:', value='Med turma',
                               data=['Med turma', 'AP', 'RM', 'RF', 'RMF'], clearable=False),
                ]),
            ]),



            html.Div([
                dmc.Select(id='dropdown52', label='Regressão linear:',  value=None,
                    data=[
                        {'label': 'Nenhuma', 'value': None},
                        {'label': 'Linear', 'value': 'ols'},
                        {'label': 'Pesada', 'value': 'lowess'}
                    ],
                    clearable=False)
            ]),


            html.Div([
                dmc.Select(id='dropdown53', label='Escopo da regressão linear:', value='overall',
                    data=[
                        {'label': 'Geral', 'value': 'overall'},
                        {'label': 'Legenda', 'value': 'trace'},
                    ],
                    clearable=False
                )
            ])

            ],
            style={'display': 'flex', 'flexDirection': 'column', 'gap': 20, 'flex': 1}
        ),

    return content



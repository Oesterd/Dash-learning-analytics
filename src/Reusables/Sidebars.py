Ops = {
   'Nenhuma': ['Nenhuma', 'Gênero', 'Escola', 'Etnia'],
   'Gênero': ['Nenhuma', 'Escola', 'Etnia'],
   'Escola': ['Nenhuma', 'Gênero', 'Etnia'],
   'Etnia': ['Nenhuma', 'Gênero', 'Escola']
}

Ops2 = {
    'Média aluno': ['Histograma', 'Cumulativo'],
    'Resultado': ['Histograma'],
}



def pg1():
    content = \
        html.Div([
            html.Div([
                dmc.MultiSelect(id='Mdropdown11', label='Escolha o(s) professor(es):', value=[],
                           data=Prof_Notas, searchable=True, clearable=True),
                ]
            ),

            html.Div([
                dmc.Select(id='dropdown11', label='Escolha o eixo x:', value='Média aluno',
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
                           data=['Nenhuma', 'Gênero', 'Etnia', 'Escola'],
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
            html.Div([
                dmc.MultiSelect(id='Mdropdown21', label='Escolha o(s) professor(es):', value=[],
                           data=Prof_Notas, searchable=True, clearable=True),
                ]
            ),

            html.Div([
                dmc.Select(id='dropdown21', label='Escolha o eixo x:', value='Renda (R$)',
                           data=['Renda (R$)', 'Frequência'], clearable=False)
            ]),

            html.Div([
                dmc.Select(data=list(Ops.keys()), label='Divisão por colunas:', value='Nenhuma', id='dropdown22', clearable=False),
            ]),

            html.Div([
                dmc.Select(id='dropdown23', label='Divisão por linhas:',  value='Nenhuma', data=['Nenhuma', 'Gênero', 'Escola'], clearable=False),
            ]),

            html.Div([
                dmc.Select(id='dropdown24', label='Linha de tendência:', value=None,
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
                    id='dropdown25', label='Escopo da linha de tendência:',  value='overall',
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
            html.Div([
                dmc.MultiSelect(id='Mdropdown41', label='Escolha a(s) disciplina(s)', value=[],
                                data=Disc, searchable=True, clearable=True)
            ]),

            html.Div([
                dmc.MultiSelect(id='Mdropdown42', label='Escolha o(s) professor(es)', value=[],
                                data=Prof_turmas, searchable=True, clearable=True)
            ]),


            html.Div([
                    dmc.Select(id='dropdown41', label='Escolha o eixo y:',  value='Média turma',
                               data=['Média turma', 'AP', 'RM', 'RF', 'RMF'], clearable=False),
            ]),
            ],
            style={'display': 'flex', 'flexDirection': 'column', 'gap': 20, 'flex': 1}
        )

    return content




def pg5():
    content = \
        html.Div([
            html.Div([
                dmc.MultiSelect(id='Mdropdown51', label='Escolha a(s) disciplina(s)', value=[],
                                data=Disc, searchable=True, clearable=True)
            ]),


            html.Div([
                dmc.MultiSelect(id='Mdropdown52', label='Escolha o(s) professor(es)', value=[],
                                data=Prof_turmas, searchable=True, clearable=True)
            ]),


            html.Div([
                dmc.Select(id='dropdown51', label='Escolha o eixo y:', value='Média turma',
                           data=['Média turma', 'AP', 'RM', 'RF', 'RMF'], clearable=False),
            ]),


            html.Div([
                dmc.Select(id='dropdown52', label='Linha de tendência:',  value=None,
                    data=[
                        {'label': 'Nenhuma', 'value': None},
                        {'label': 'Linear', 'value': 'ols'},
                        {'label': 'Pesada', 'value': 'lowess'}
                    ],
                    clearable=False)
            ]),


            html.Div([
                dmc.Select(id='dropdown53', label='Escopo da linha de tendência:', value='overall',
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


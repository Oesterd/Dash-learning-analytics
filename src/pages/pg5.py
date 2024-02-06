# Importando as bibliotecas
import dash, orjson
from dash import html, dcc, Input, Output, callback
import dash_ag_grid as dag


import plotly.express as px
import pandas as pd
import numpy as np
import scipy.stats






dash.register_page(__name__, name='Turmas')





filename = 'Reusables/Turmas.py'
exec(open(filename).read())



Opcs = ['Med turma', 'AP', 'RM', 'RF', 'RMF']







layout = \
html.Div([
    html.Div([
        grid
    ]),


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
    ], style={'display': 'flex', 'flexDirection': 'row', 'gap': 50, 'flex': 1}),


    html.Br(),


    html.Div([
        # Gráfico
        html.Div([
            dcc.Graph(id='scatter2')
        ], style={'flex-basis': 800}),

        # Valores de correlação
        html.Div([
            dcc.Textarea(
                id='textpg5',
                disabled=True,
                className='textarea'
            )
        ], style={'position': 'relative', 'left': 75, 'top': 100}),

    ], style={'display': 'flex', 'flexDirection': 'row', 'gap': 20, 'flex': 1}),


])






#--------------------------------------------------------------------------------------------
@callback(
    Output(component_id='scatter2', component_property='figure'),
    Output(component_id='textpg5', component_property='value'),
    Input(component_id='grid', component_property='virtualRowData'),
    Input(component_id='dropdown51', component_property='value'),
    Input(component_id='dropdown52', component_property='value'),
    Input(component_id='dropdown53', component_property='value'),
)








def scatter_plot(rows, drop1, drop2, drop3):

    # Modificando os dados conforme a filtragem do usuário
    dff = pd.DataFrame(rows)




    # Gerando a opção nula
    if drop2 == 'Nenhuma':
         drop2 = None



    # Transformando os dados no eixo y em uma razão ao invés de número absoluto
    if drop1 == 'Med turma':
        var = drop1
        drop1 = dff['Med turma']

    elif drop1 == 'AP':
        var = drop1
        var2 = 'Aprovados'
        drop1 = dff['AP']/dff['Num Alunos']

    elif drop1 == 'RM':
        var = drop1
        var2 = 'Reprovados por média'
        drop1 = dff['RM']/dff['Num Alunos']

    elif drop1 == 'RF':
        var = drop1
        var2 = 'Reprovados por falta'
        drop1 = dff['RF']/dff['Num Alunos']

    elif drop1 == 'RMF':
        var = drop1
        var2 = 'Reprovados por média e falta'
        drop1 = dff['RMF']/dff['Num Alunos']





    # Valores de correlação

    x = dff['Av Professor']
    y = dff[var]

    r = y.corr(x, method='pearson')
    r2 = y.corr(x, method='spearman')
    r3 = y.corr(x, method='kendall')

    result = scipy.stats.linregress(x, y)

    p = result.pvalue
    desp = result.stderr


    text = f'O valor do coeficiente de correlação é: \nPearson = {r:.3f} \nSpearman = {r2:.3f} \nKendall = {r3:.3f} \n\nO valor-p é: {p:.3f} \nO desvio padrão é: {desp:.3e}'



    # Criando o gráfico
    figpg5 = px.scatter(dff, x='Av Professor', y=drop1, color='Professor', trendline=drop2, trendline_scope=drop3,
                     hover_name='Professor',
                     hover_data={
                         'Disciplina': False,
                         'Professor': False,
                         'Av Professor': ':.2f',
                     },
                     )


    # Tornando os números do eixo y em formato de porcentagem

    if var != 'Med turma':
        figpg5.update_layout(
            yaxis_tickformat='.0%',
            yaxis_title=var2),


    if var == 'AP':
        figpg5.update_traces(
            hovertemplate='<br>'.join([
                'Avaliação professor: %{x:.2f}',
                'Aprovados: %{y}',
            ])
        )

    elif var == 'RM':
        figpg5.update_traces(
            hovertemplate='<br>'.join([
                'Avaliação professor: %{x:.2f}',
                'Reprovados por média: %{y}',
            ])
        )

    elif var == 'RF':
        figpg5.update_traces(
            hovertemplate='<br>'.join([
                'Avaliação professor: %{x:.2f}',
                'Reprovados por falta: %{y}',
            ])
        )

    elif var == 'RMF':
        figpg5.update_traces(
            hovertemplate='<br>'.join([
                'Avaliação professor: %{x:.2f}',
                'Reprovados por média e falta: %{y}',
            ])
        )

    return figpg5, text
# Importando as bibliotecas
import dash
from dash import html, dcc, Input, Output, State, callback
import dash_ag_grid as dag
from dash.exceptions import PreventUpdate


import plotly.express as px
import pandas as pd
import scipy.stats






dash.register_page(__name__, name='Turmas')





filename = 'Reusables/Turmas.py'
exec(open(filename, encoding="utf-8").read())








grid = dag.AgGrid(
    id='grid4',
    rowData=[],
    columnDefs=clndef,
    defaultColDef=dfclndef,
    dashGridOptions={'pagination': True},
    style={'height': '400px'}
)



#--------------------------------------------------------------------------
layout = \
html.Div([
    html.Div([
        grid
    ]),

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







#-----------------------------------------------------------------------------------------------------
@callback(
    Output('grid4', 'rowData'),
    Input('Dados_turmas', 'data'),
)


def Grid_maker(data):
    return data





@callback(
    Output(component_id='scatter2', component_property='figure'),
    Output(component_id='textpg5', component_property='value'),
    Input(component_id='Intervalo', component_property='n_intervals'),
    Input(component_id='grid4', component_property='virtualRowData'),
    Input(component_id='dropdown51', component_property='value'),
    Input(component_id='dropdown52', component_property='value'),
    Input(component_id='dropdown53', component_property='value'),
    prevent_initial_call=True
)








def scatter_plot(n, rows, drop1, drop2, drop3):

    # Evitando que o Output seja atualizado enquanto os Inputs ainda não estão presente no layout
    if not rows:
        raise PreventUpdate


    # Modificando os dados conforme a filtragem do usuário
    dff = pd.DataFrame(rows)



    # Transformando os dados no eixo y em uma razão ao invés de número absoluto
    if drop1 == 'Média turma':
        var = drop1
        drop1 = dff['Média turma']

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

    text = f'Coeficiente de correlação:\nPearson = {r:.3f} \nSpearman = {r2:.3f} \nKendall = {r3:.3f} \n\nValor-p: {p:.3f} \nDesvio padrão: {desp:.3e}'


    # Criando o gráfico
    figpg5 = px.scatter(
        dff, x='Av Professor', y=drop1,
        color='Professor', trendline=drop2, trendline_scope=drop3,
        hover_name='Professor',
        hover_data={
            'Disciplina': False,
            'Professor': False,
            'Av Professor': ':.2f',
        },
    )


    # Tornando os números do eixo y em formato de porcentagem
    if var != 'Média turma':
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
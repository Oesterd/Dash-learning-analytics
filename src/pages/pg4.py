# Importando as bibliotecas
import dash
from dash import html, dcc, Input, Output, State, callback
import dash_ag_grid as dag
from dash.exceptions import PreventUpdate

import plotly.express as px
import pandas as pd







dash.register_page(__name__, name='Linha do tempo')



filename = 'Reusables/Turmas.py'
exec(open(filename, encoding="utf-8").read())





grid = dag.AgGrid(
    id='grid3',
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

    # Gráfico
    html.Div([
        dcc.Graph(id='timeseries')
    ])

])






#--------------------------------------------------------------------------
@callback(
    Output('grid3', 'rowData'),
    Input(component_id='Intervalo', component_property='n_intervals'),
    Input('Dados_turmas', 'data'),
    Input(component_id='Mdropdown41', component_property='value'),
    Input(component_id='Mdropdown42', component_property='value'),
)


def Grid_maker(n, data, mdrop1, mdrop2):
    dff = pd.DataFrame(data)


    if mdrop1:
        dff = dff[dff['Disciplina'].isin(mdrop1)]

    if mdrop2:
        dff = dff[dff['Professor'].isin(mdrop2)]


    data = dff.to_dict('records')

    return data




#--------------------------------------------------------------------------------
@callback(
    Output(component_id='timeseries', component_property='figure'),
    Input(component_id='Intervalo', component_property='n_intervals'),
    Input(component_id='grid3', component_property='virtualRowData'),
    Input(component_id='dropdown41', component_property='value'),
    prevent_initial_call=True
)


def filterdata(n, rows, drop1):

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




    fig = px.line(
        dff, x='Turma', y=drop1,
        color='Disciplina', symbol='Disciplina', markers=True,
        hover_name='Disciplina',
        hover_data={
         'Disciplina': False,
         'Professor': True,
         'Turma': False,
         'Aprovados': (':.0%', dff['AP']/dff['Num Alunos']),
         }
    )


    fig.update_xaxes(rangeslider_visible=True)

    # Tornando os números do eixo y em formato de porcentagem

    if var != 'Média turma':
        fig.update_layout(
            yaxis_tickformat='.0%',
            yaxis_title=var2),


    if var == 'AP':
        fig.update_traces(
            hovertemplate='<br>'.join([
                'Aprovados: %{y}',
                'Turma: %{x}',
            ])
        )

    elif var == 'RM':
        fig.update_traces(
            hovertemplate='<br>'.join([
                'Reprovados por média: %{y}',
                'Turma: %{x}',
            ])
        )

    elif var == 'RF':
        fig.update_traces(
            hovertemplate='<br>'.join([
                'Reprovados por falta: %{y}',
                'Turma: %{x}',
            ])
        )

    elif var == 'RMF':
        fig.update_traces(
            hovertemplate='<br>'.join([
                'Reprovados por média e falta: %{y}',
                'Turma: %{x}',
            ])
        )


    return fig

# Importando as bibliotecas
import io
from io import BytesIO
import base64

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff

import pandas as pd
import numpy as np
import openpyxl

from dash import Dash, html, dcc, dash_table, Input, Output, callback
from dash.dash_table.Format import Format, Scheme


# Iniciando o aplicativo
app = Dash(__name__)
server = app.server

# Selecionando os dados a serem lidos
dfraw = pd.read_excel('https://github.com/Oesterd/Dash123/raw/master/dados_teste.xlsx')
df = dfraw.iloc[:, 0:10]
df



## Procedimento para gerar um dashboard interativo e customizável utilizando plotly ao invés de seaborn

# # Criando uma lista de todos os professores
# df_prof = pd.Series(df0['Professor'].unique()).sort_values().to_list()
# df_prof
#
# # Criando grupo de dados por professores
# for i,j in zip(range(len(df_prof)+1), df_prof):
#     globals()[f'dfg{i+1}']=df0[df0['Professor'] == j]
#
# # Teste
# dfg1
# table = pd.pivot_table(dfg1, values='Média aluno', columns='Professor', index='Alunos')
# table.index.dtype






# Formatação dos números
numformat = Format(precision=2, scheme=Scheme.fixed, decimal_delimiter=',')
renformat = Format(precision=0, scheme=Scheme.fixed, decimal_delimiter=',')



# Separando as colunas para os dicionários
dfmed = df.iloc[:, 5:8]
dftext = df.iloc[:, 1:4]
dfend = df.iloc[:, 8:10]







# Criando os dicionários
dictaln = [{'name': 'Alunos', 'id': 'Alunos', 'type': 'text'}]
dicttext = [{'name': i, 'id': i, 'selectable': True} for i in dftext]
dictren = [{'name': 'Renda (S.M)', 'id': 'Renda (S.M)', 'type': 'numeric', 'format': renformat, 'selectable': True}]
dictmed = [{'name': i, 'id': i, 'type': 'numeric', 'format': numformat} for i in dfmed]
# dictfrq = [{'name': 'Frequência', 'id': 'Frequência', 'type': 'numeric', 'format': numformat, 'selectable': True}]
dictend = [{'name': i, 'id': i, 'selectable': True} for i in dfend]


# Opções do dropdown
nullop = 'Nenhuma'
op1 = df.columns[np.r_[4,9]].tolist() # Divisão por cores
op1.insert(0, nullop)
op2 = df.columns[1:4].tolist() # Divisão por colunas
op2.insert(0, nullop)




# Layout do dash
app.layout = \
html.Div([
    html.Div([
        dash_table.DataTable(  # Tabela de dados
            id='datatable_id',
            columns=dictaln + dicttext + dictren + dictmed + dictend,
            style_cell={'textAlign': 'center'},
            sort_action='native',
            sort_mode='single',
            filter_action='native',
            page_size=8,
            data=df.to_dict('records')
        )
    ]),

    # Menus de dropdown
    html.Div([
        html.Div([
            "Divisão por cores:",
            dcc.Dropdown(id='dropdown', value='Nenhuma', options=op1, clearable=False),
        ]),

        html.Div([
            "Divisão por coluna:",
            dcc.Dropdown(id='dropdown2', value='Nenhuma', options=op2, clearable=False),
        ]),

        html.Div([
            "Tipo de gráfico:",
            dcc.Dropdown(id='dropdown3', value='kde', options=[
                {'label': 'KDE', 'value': 'kde'},
                {'label': 'Histograma', 'value': 'hist'},
                {'label': 'Cumulativo', 'value': 'ecdf'}], clearable=False),
        ]),

        html.Div([
            "Tipo de agrupamento:",
            dcc.Dropdown(id='dropdown4', value='layer', options=[
                {'label': 'Normal', 'value': 'layer'},
                {'label': 'Empilhar', 'value': 'stack'}], clearable=False),
        ])
    ], style={'display': 'flex', 'flexDirection': 'row', 'gap':50, 'flex':1}),

    # Gráfico
    html.Div([
        html.Img(id='matplot') # É necessário utilizar html.Img ao invés de dcc.Graph, pois o gráfico foi gerado pelo matplotlib e não pelo Plotly
    ])



])




#-------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='matplot', component_property='src'),
    Output(component_id='dropdown4', component_property='disabled'),
    Input(component_id='dropdown', component_property='value'),
    Input(component_id='dropdown2', component_property='value'),
    Input(component_id='dropdown3', component_property='value'),
    Input(component_id='dropdown4', component_property='value'),
    Input(component_id='datatable_id', component_property='derived_virtual_data')
)



def matplot_html(drop1, drop2, drop3, drop4, rows):

## Criando o gráfico

    # Modificando os dados de acordo com a filtragem do usuário
    dff = pd.DataFrame(rows)


    # Criando as opções nulas para os dropdowns 1 e 2
    if drop1 == 'Nenhuma':
        drop1 = None
    else:
        drop1 = f'{drop1}'

    if drop2 == 'Nenhuma':
        drop2 = None
    else:
        drop2 = f'{drop2}'


    # Gerando o gráfico de acordo com a escolha no dropdown 3
    if drop3 == 'ecdf':
      fig = sns.displot(data=dff, x='Média aluno', hue=drop1, col=drop2, kind= f'{drop3}')
      Disdrop4 = True
    else:
      fig = sns.displot(data=dff, x='Média aluno', hue=drop1, col=drop2, kind= f'{drop3}', multiple=f'{drop4}')
      Disdrop4 = False




    # Criando o buffer temporário para renderizar um gráfico do matplotlib no Dash
    buf = BytesIO()
    fig.savefig(buf, format='png')
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_matplot = f'data:image/png;base64,{fig_data}'

    # Retorno dos outputs para o callback
    return fig_matplot, Disdrop4




# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)

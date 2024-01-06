# Importando as bibliotecas
from io import BytesIO
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import base64


import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff

import pandas as pd
import numpy as np

from dash import Dash, html, dcc, dash_table, Input, Output, callback
from dash.dash_table.Format import Format, Scheme

# Iniciando o aplicativo
app = Dash(__name__)
server = app.server

# Selecionando os dados a serem lidos
dfraw = pd.read_excel('https://github.com/Oesterd/Dash123/raw/master/dados_teste.xlsx')
df = dfraw.iloc[:, 0:10]
df



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




# Layout do dash
app.layout = html.Div([
    dash_table.DataTable( #Tabela de dados
        id='datatable_id',
        columns=dictaln + dicttext + dictren + dictmed + dictend,
        style_cell={'textAlign': 'center'},
        sort_action='native',
        sort_mode='single',
        column_selectable='multi',
        filter_action='native',
        page_size=8,
        data=df.to_dict('records')
    ),
    # html.Div([ #Bloco de input
    #     "Escolha a propriedade 1: ",
    #     dcc.Dropdown(id='dropdown', value='Professor', options=df.columns[np.r_[1:5, 8,9]], clearable=False),
    # ]),
    # html.Div([ #Bloco de input
    #     "Escolha a propriedade 2: ",
    #     dcc.Dropdown(id='dropdown2', value='Gẽnero', options=df.columns[np.r_[1:4, 8,9]], clearable=False),
    # ]),
    html.Img(id='matplot') #Imagem
])


#-------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='matplot', component_property='src'),
    Input(component_id='datatable_id', component_property='selected_columns')
)



def matplot_html(selcol):

    # Criando o gráfico
    sns.displot(data=df, x='Média aluno', hue=f'{selcol[0]}', col=f'{selcol[1]}', kind= 'kde')
    print(selcol)

    # Criando o buffer temporário
    buf = BytesIO()
    plt.savefig(buf, format='png')
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_matplot = f'data:image/png;base64,{fig_data}'

    return fig_matplot




# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)

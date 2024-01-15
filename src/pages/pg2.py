# Importando as bibliotecas
import datetime
import dash
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output, callback, dash_table
from plotly.subplots import make_subplots


import plotly.express as px

import pandas as pd
import numpy as np
import openpyxl




dash.register_page(__name__, name='Lista de professores')


# Fotos
foto_luis = 'https://files.cercomp.ufg.br/weby/up/3/o/luiz1.jpg'
foto_rildo = 'https://files.cercomp.ufg.br/weby/up/3/o/joseRildo1.jpg'
foto_paulo = 'https://files.cercomp.ufg.br/weby/up/3/o/paulo1.jpg'



# Datas
date1 = datetime.date(2011, 7, 21)
date2 = datetime.date(2012, 2, 13)
date3 = datetime.date(2012, 4, 7)



# Dicionário
data_dict = {
    'name': ['Prof. Dr. Luiz Gonzaga Roversi Genovese', 'Prof. Dr. José Rildo de Oliveira Queiroz', 'Prof. Dr. Paulo Celso Ferrari'],
    'img': [foto_luis, foto_rildo, foto_paulo],
    'turmas': [25, 22, 21],
    'ativo': [date1, date2, date3],
    'Tot_AP': [106, 97, 90],
    'Tot_RM': [23, 18, 15],
    'Tot_RF': [11, 10, 8],
    'Tot_RMF': [6, 4, 4],
    'Total': [146, 129, 117]
}




# Colunas
clndef = [
    {
        "headerName": "Foto",
        "field": "img",
        "cellRenderer": "ImgThumbnail",
        "width": 100,
    },
    {
        "headerName": "Nome",
        "field": "name",
        "resizable": True,
    },
    {
        "headerName": "AP",
        "field": "Tot_AP",
        "width": 100,
        "cellClass": 'center-aligned-cell'
    },
    {
        "headerName": "RM",
        "field": "Tot_RM",
        "width": 100,
        "cellClass": 'center-aligned-cell'
    },
    {
        "headerName": "RF",
        "field": "Tot_RF",
        "width": 100,
        "cellClass": 'center-aligned-cell'
    },
    {
        "headerName": "RMF",
        "field": "Tot_RMF",
        "width": 100,
        "cellClass": 'center-aligned-cell'
    },
    {
        "headerName": "Total de alunos",
        "field": "Total",
        "width": 150,
        "cellClass": 'center-aligned-cell'
    },
    {
        "headerName": "Turmas",
        "field": "turmas",
        "width": 100,
        "cellClass": 'center-aligned-cell'
    },
    {"headerName": "Ativo desde",
        "field": "ativo",
        "width": 150,
        "cellClass": 'center-aligned-cell'
    }
]

dfclndef = {
    "headerClass": 'center-aligned-header',
}



# Dataframe
data = pd.DataFrame(data_dict)



## Plots
specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}]]
fig = make_subplots(rows=1, cols=4, specs=specs, subplot_titles=["AP", "RM", "RF", "RMF"])



AP_chart = go.Pie(
    values=data_dict['Tot_AP'],
    labels=data_dict['name'],
)

RM_chart = go.Pie(
    values=data_dict['Tot_RM'],
    labels=data_dict['name'],
)

RF_chart = go.Pie(
    values=data_dict['Tot_RF'],
    labels=data_dict['name'],
)

RMF_chart = go.Pie(
    values=data_dict['Tot_RMF'],
    labels=data_dict['name'],
)


# Criando os gráficos
fig.add_trace(AP_chart, row=1, col=1)
fig.add_trace(RM_chart, row=1, col=2)
fig.add_trace(RF_chart, row=1, col=3)
fig.add_trace(RMF_chart, row=1, col=4)






# Layout da página
layout = \
html.Div([
    html.Div([
        dag.AgGrid(  # Tabela de dados
            id='AgGrid',
            rowData=data.to_dict('records'),
            columnDefs=clndef,
            defaultColDef=dfclndef,
            dashGridOptions={"rowHeight": 100},
            style={"height": 351, "width": 1105},
        )
    ]),

    html.Div([
        dcc.Graph(id='Perc', figure=fig)
    ], style={'position': 'relative', 'right': 100})

], style={"margin": 20}
)


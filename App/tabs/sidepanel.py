import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
import pandas
from dash.dependencies import Input, Output

from app import app

from tabs import tab1, tab2, tab3
from database import transforms


layout = html.Div([
    
    dbc.Row(

        [  
           # dbc.Collapse(
                dbc.Col(
                    html.Div([
                     html.H2('Filters'),
                     html.Div([html.H5('Controls')])
                    ], style={'marginBottom': 50, 'marginTop': 25, 'marginLeft':15, 'marginRight':15}),
                width=1),
           # id="collapse",
           # ),

         dbc.Col(
            html.Div([
                    dcc.Tabs(id="tabs", value='tab-1', children=[
                        dcc.Tab(label='Exploratory Data Analysis 1', value='tab-1'),
                        dcc.Tab(label='Exploratory Data Analysis 2', value='tab-2'),
                        dcc.Tab(label='Mapa Prioridad por municipio', value='tab-3'),
                        ]),
            html.Div(id='tabs-content')
                    ]), 
        width=11)
        ])
    
    ])

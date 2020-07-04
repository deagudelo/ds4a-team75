import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
import pandas
from dash.dependencies import Input, Output

from app import app

from tabs import tab1, tab2
from database import transforms


layout = html.Div([
    
 



    dbc.Row([dbc.Col(
        html.Div([
         html.H2('Filters'),
         html.Div([html.H5('Controls')
            
                        
        ])
    
        ], style={'marginBottom': 50, 'marginTop': 25, 'marginLeft':15, 'marginRight':15})
    , width=3)

    ,dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                    dcc.Tab(label='Datos uno', value='tab-1'),
                    dcc.Tab(label='Datos dos', value='tab-2'),
                ])
            , html.Div(id='tabs-content')
        ]), width=9)])
    
    ])

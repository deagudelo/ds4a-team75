import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

from app import app 
from database import transforms

#df = transforms.df
figpie = transforms.figpie

PAGE_SIZE = 50
#  html.Div([
#         dbc.Row([dbc.Col(html.Div(html.P("A single, half-width column")),style = {'padding':'50px'})
#                 ,dbc.Col(
layout =html.Div(  #html.H1('Tab uno contenido'),
				dcc.Graph(figure=figpie, id='pie_grap2')
		
                        )
            #             , width=9)
            #     ])
            # ])
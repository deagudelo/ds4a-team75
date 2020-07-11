import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
#import dash_table
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

from app import app
from database import transforms

#df = transforms.df
figpie = transforms.figpie
fig = transforms.fig
fig2 = transforms.fig2
fig1 = transforms.fig1

#PAGE_SIZE = 50
#  html.Div([
#         dbc.Row([dbc.Col(html.Div(html.P("A single, half-width column")),style = {'padding':'50px'})
#                 ,dbc.Col(
layout =html.Div([

 			#html.H3('Tab content 1'),
            #html.H3('Tab content 3'),

            #html.Div(id='my-output')
				  #html.H1('Tab uno contenido'),
				#html.H1(children='Hello Dash'),
			dcc.Graph(figure=fig2, id='g1'),
			dcc.Graph(figure=fig1, id='g2'),
			dcc.Graph(figure=fig, id='g3')
				#html.Div([dcc.Graph(figure=fig1, id='pie_gr')])
		
                        
])

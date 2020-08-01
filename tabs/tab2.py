import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from database import transforms


figpie_comp = transforms.figpie_comp
fig_mapbox = transforms.fig_mapbox

layout = html.Div([

dbc.Row([
	dbc.Col([dcc.Graph(figure=fig_mapbox, id='unmapa')]),
	dbc.Col([dbc.Row([dcc.Graph(id='2graph_time')]),
			dbc.Row([dcc.Graph(id='graph_circuits')]),
			]),
		]),
dbc.Row([dcc.Graph(figure=figpie_comp, id='pie_grap2')]),

])
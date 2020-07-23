import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from application import application
from database import transforms


figpie_comp = transforms.figpie_comp
fig_mapbox = transforms.fig_mapbox

layout = html.Div([

			dcc.Graph(figure=fig_mapbox, id='unmapa'),

			dcc.Graph(id='graph_circuits'),
            dcc.Graph(figure=figpie_comp, id='pie_grap2')
#            html.H1('Tab dos contenido'),
#            id='table-paging-with-graph-container',
#            className="five columns"
        ])

#@app.callback(Output('table-paging-with-graph-container', "children"),
#[Input('rating-95', 'value')
#, Input('price-slider', 'value')
#])

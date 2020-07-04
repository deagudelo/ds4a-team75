import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from app import app
from database import transforms

df = transforms.df

layout = html.Div(
            html.H1('Tab dos contenido'),
            id='table-paging-with-graph-container',
            className="five columns"
        )

#@app.callback(Output('table-paging-with-graph-container', "children"),
#[Input('rating-95', 'value')
#, Input('price-slider', 'value')
#])




   
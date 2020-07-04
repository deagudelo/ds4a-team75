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


ti = html.Div([
    
    html.Div([
    html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("logoepm.png"),
                    id="epm-image",
                ),
            ],
    className="two columns"),
    html.Div([
    html.H1('Electricity Distribution Failure Model') 

    ], className="ten columns"),
    ], className="row")
])

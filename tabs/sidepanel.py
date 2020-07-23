import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas
from dash.dependencies import Input, Output

from application import application

from tabs import tab1, tab2, tab3
from database import transforms

listaTechLocation = ['Transformador', 'Salida Circuito',
                     'Aisladero', 'Reconectador', 'Salida_Circuito']

layout = html.Div(
    [
        html.H2('Filters'),
        html.H4('Technical location:'),
        html.Br(),
        dcc.Dropdown(
            id='techlocation',
            options=[{'label': i, 'value': i} for i in listaTechLocation],
            value='Transformador'
        ),
        html.Div([html.H5('Controls')])
    ],
    style={'marginBottom': 50, 'marginTop': 25,
           'marginLeft': 15, 'marginRight': 15}
)

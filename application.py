import os
import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from flask_caching import Cache

#import sqlite3

import pandas as pd

from tabs import sidepanel, title, tabs, navbar
from database import transforms
df = transforms.df


external_scripts = [
    {
        'src': 'https://code.jquery.com/jquery-3.3.1.slim.min.js',
        'integrity': 'sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js',
        'integrity': 'sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js',
        'integrity': 'sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://kit.fontawesome.com/c96da4d2be.js',
        'crossorigin': 'anonymous'
    }

]
external_stylesheets = [
    {
        'rel': 'stylesheet',
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        'crossorigin': 'anonymous',
        'integrity': 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T'
    },
    # {
    #     'href': 'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
    #     'rel': 'stylesheet',
    #     'integrity': 'sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf',
    #     'crossorigin': 'anonymous'
    # },
    {
        'rel': 'stylesheet',
        'href': 'https://kit-free.fontawesome.com/releases/latest/css/free-v4-shims.min.css',
        'media': 'all'
    },
    {
        'rel': 'stylesheet',
        'href': 'https://kit-free.fontawesome.com/releases/latest/css/free-v4-font-face.min.css',
        'media': 'all'
    },
    {
        'rel': 'stylesheet',
        'href': 'https://kit-free.fontawesome.com/releases/latest/css/free.min.css',
        'media': 'all'
    },
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    dbc.themes.BOOTSTRAP
]
application = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts
)

server = application.server
application.config.suppress_callback_exceptions = True

df = transforms.df
application.layout = html.Div([
    navbar.Navbar(application),
    #            title.layout(application),
    # sidepanel.layout,



    html.Div(
        className="container-fluid",
        children=[
            html.Div(
                className='row py-2',
                children=[
                    html.Div(
                        className="col-xs-4 col-md-2 collapse m-0 p-0 h-100",
                        id="collapseExample",
                        children=[
                            sidepanel.layout
                        ], style={'backgroundColor': '#FFFFFF'}
                    ),
                    html.Div(
                        className='col-xs-8 col-md-10 mx-auto',
                        children=[
                            tabs.layout(application)
                        ]
                    )

                ]
            ),
            html.Div(
                className="fab-container",
                children=[
                    html.Div(
                        className="fab fab-icon-holder",
                        children=[
                            html.A(
                                **{
                                    'data-toggle': 'collapse',
                                },
                                href="#collapseExample",
                                role="button",
                                children=[
                                    html.I(
                                        className="fas fa-filter",
                                    )
                                ]
                            )
                        ]
                    )
                ]
            ),

        ]
    )

])


@application.callback(
    [
        Output('graph_circuits', 'figure'),
        Output('2graph_time', 'figure'),
    ],
    [
        Input('techlocation', 'value'),
        Input('town', 'value')
    ])
def update_figure(tech, town):
    if town is None:
        town = ['TURBO']
    dff = df[df['year'] == '2019']
    dff = dff[dff['town'].isin(town)]
    return transforms.create_g1(tech, town), transforms.create_g2(tech, town, dff)


if __name__ == '__main__':
    application.run_server(debug=True)  # , host='0.0.0.0', port=80)
    # app.run_server(host='0.0.0.0',port='8050',debug=True)

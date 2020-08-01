import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_html_components as html
import dash_core_components as dcc
from flask_caching import Cache

from database import map_priority, map_expected

TIMEOUT = 172800


def layout(application):
    cache = Cache(application.server, config={
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_URL': "redis://default:5MoVUbdErZIK@ec2-3-18-108-50.us-east-2.compute.amazonaws.com:6379"
    })

    @cache.memoize(timeout=TIMEOUT)
    def get_figure1(zoom, colorScale, provider):
        return map_priority.map(zoom, colorScale, provider)

    @cache.memoize(timeout=TIMEOUT)
    def get_figure2(zoom, colorScale, provider):
        return map_expected.map(zoom, colorScale, provider)

    return html.Div(
        className="my-2 row",
        children=[
            html.Div(
                className="col-xs-10 col-md-6 mx-auto",
                children=[
                    html.H2("Expected failures by town", id='title1',
                            className="mx-auto my-4 text-center"),  # Creates the title of the app
                    html.Div(className='container', children=[
                        dcc.Graph(
                            figure=get_figure2(7, "Viridis_r", "go"),
                            config=dict(responsive=True),
                            style={'width': '100%'}
                        )
                    ])
                ]
            ),
            html.Div(
                className="col-xs-10 col-md-6 mx-auto",
                children=[
                    html.H2("Priority of past failures by town", id='title2',
                            className="mx-auto my-4 text-center"),  # Creates the title of the app
                    html.Div(className='container', children=[
                        dcc.Graph(
                            figure=get_figure1(7, "Viridis_r", "go"),
                            config=dict(responsive=True),
                            style={'width': '100%'}
                        )
                    ])
                ]
            )
        ]
    )

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
    def get_figure1():
        return map_priority.Map_Fig

    @cache.memoize(timeout=TIMEOUT)
    def get_figure2():
        return map_expected.Map_Fig

    return html.Div(
        className="my-2",
        children=[
            html.H2("Mapa de fallas esperadas por municipio", id='title1',
                    className="mx-auto my-2 text-center"),  # Creates the title of the app
            html.Div(className='container', children=[
                dcc.Graph(
                    figure=get_figure2(),
                    config=dict(responsive=True),
                    style={'height': '100%'}
                )
            ]),
            html.H2("Mapa de prioridades por municipio", id='title2',
                    className="mx-auto my-2 text-center"),  # Creates the title of the app
            html.Div(className='container', children=[
                dcc.Graph(
                    figure=get_figure1(),
                    config=dict(responsive=True),
                    style={'height': '100%'}
                )
            ]),
        ]
    )

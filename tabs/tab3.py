import os
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_html_components as html
import dash_core_components as dcc
from flask_caching import Cache

from database import map_data

TIMEOUT = 600


def layout(application):
    cache = Cache(application.server, config={
        'CACHE_TYPE': 'filesystem',
        'CACHE_DIR': os.path.join(os.getcwd(), 'cache-directory')
    })

    @cache.memoize(timeout=TIMEOUT)
    def get_figure():
        return map_data.Map_Fig

    return html.Div([
        html.H2("Mapita de prioridades por municipio", id='title',
                className="mx-auto text-center"),  # Creates the title of the app
        html.Div(className='container', children=[
            dcc.Loading(id="loading-1", children=[
                dcc.Graph(figure=get_figure(), id='main-figure')
            ], type="circle"),

        ]),

    ])

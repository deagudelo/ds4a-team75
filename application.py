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


external_scripts = [
    {
        'src': 'https://code.jquery.com/jquery-3.3.1.slim.min.js',
        'integrity' : 'sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo',
        'crossorigin' : 'anonymous'
    },
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js',
        'integrity' : 'sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1',
        'crossorigin' : 'anonymous'
    },
    {
        'src': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js',
        'integrity' : 'sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM',
        'crossorigin' : 'anonymous'
    }
]
external_stylesheets = [
    {
        'rel': 'stylesheet',
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        'crossorigin': 'anonymous',
        'integrity': 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T'
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

cache = Cache(application.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': os.path.join(os.getcwd(), 'cache-directory')
})

timeout = 600

application.layout = html.Div([
            navbar.Navbar(), 
            title.layout(application),
            html.Div(
                className="container-fluid",
                children=[
                    html.Div(
                        className='row',
                        children=[
                            html.Div(
                                className='col-xs-4 col-md-2',
                                children=[
                                    sidepanel.layout
                                ]
                            ),
                            html.Div(
                                className='col-xs-8 col-md-10',
                                children=[
                                    tabs.layout(application)
                                ]
                            )

                        ]
                    )
                ]
            )

            ])

@application.callback(
    Output('graph_circuits', 'figure'),
    [Input('techlocation', 'value')])  # in seconds
def update_figure(filtro):
        dff= df[df['LocationDescription'] == filtro]
        dfg= dff.groupby(df['Circuit'])['NumberOT'].count().reset_index()
        dfg.sort_values(by=['NumberOT'], inplace=True, ascending=False)
        fig = px.bar(dfg, x='Circuit', y='NumberOT', title='Total of Work Orders by Circuit')
        fig.update_layout(transition_duration=500)
        return fig

if __name__ == '__main__':
    application.run_server(debug = False)#, host='0.0.0.0', port=80)
    #app.run_server(host='0.0.0.0',port='8050',debug=True)

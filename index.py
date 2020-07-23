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

from application import application
from tabs import sidepanel, title, tabs, navbar
from database import transforms


df = transforms.df

cache = Cache(application.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

timeout = 600

application.layout = html.Div([
            navbar.Navbar(), 
            title.ti,
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
                                    tabs.layout
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
#@app.callback(
#    Output(component_id='my-output', component_property='children'),
#    [Input('techlocation','value')]
#)
#def update_outpuadasast_div(input_value):
#    return 'aqui: {}'.format(input_value)




if __name__ == '__main__':
    application.run_server(debug = False)#, host='0.0.0.0', port=80)
    #app.run_server(host='0.0.0.0',port='8050',debug=True)

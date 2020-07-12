import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

#import sqlite3

import pandas as pd

from app import app
from tabs import sidepanel, title, tab1, tab2, tab3, navbar
from database import transforms

df = transforms.df


app.layout = html.Div([
            navbar.Navbar(), 
            title.ti,
            #dcc.Graph(id='graph_circuits'),
            sidepanel.layout,
            #html.Br()

            ])
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return tab1.layout
    elif tab == 'tab-2':
        return tab2.layout
    elif tab == 'tab-3':
        return tab3.layout

@app.callback(
    Output('graph_circuits', 'figure'),
    [Input('techlocation', 'value')])
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
    app.run_server(debug = False)
    #app.run_server(host='0.0.0.0',port='8050',debug=True)

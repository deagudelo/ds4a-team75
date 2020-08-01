import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from database import transforms


figpie_comp = transforms.figpie_comp
fig_mapbox = transforms.fig_mapbox
fig2 = transforms.fig2

layout = html.Div(
    className='my-2',
    children=[
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="col-xs-12 col-md-6",
                    children=[
                        dcc.Graph(figure=fig_mapbox, id='unmapa')
                    ]
                ),
                html.Div(
                    className="col-xs-12 col-md-6",
                    children=[
                        html.Div(
                            className="row",
                            children=[
                                html.Div(
                                    className="col-xs-10 mx-auto",
                                    children=[
                                        dcc.Graph(id='2graph_time')
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className="row",
                            children=[
                                html.Div(
                                    className="col-xs-10 mx-auto",
                                    children=[
                                        dcc.Graph(id='graph_circuits')
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
		html.Div(
            className="row",
            children=[
				html.Div(
					className="col-xs-12",
					children=[
						dcc.Graph(figure=figpie_comp, id='pie_grap2')
					]
				)
            ]
        ),
		html.Div(
            className="row",
            children=[
				html.Div(
					className="col-xs-12",
					children=[
						dcc.Graph(figure=fig2, id='g1')
					]
				)
            ]
        ),
		



    ]
)

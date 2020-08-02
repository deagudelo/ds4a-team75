import dash_core_components as dcc
import dash_html_components as html
from database import transforms


figpie_comp = transforms.figpie_comp
fig_mapbox = transforms.fig_mapbox
fig2 = transforms.fig2

layout = html.Div(
    className='my-2',
    children=[
        html.Div(
            className="row my-2",
            children=[
                html.Div(
                    className="col-xs-12 col-md-6",
                    children=[
                        dcc.Graph(
                            figure=fig_mapbox,
                            id='unmapa',
                            config=dict(responsive=True),
                            style={'width': '100%'}
                        )
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
                                        dcc.Graph(
                                            id='2graph_time',
                                            config=dict(responsive=True),
                                            style={'width': '100%'}
                                        )
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
                                        dcc.Graph(
                                            id='graph_circuits',
                                            config=dict(responsive=True),
                                            style={'width': '100%'}
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
        html.Div(
            className="row my-2",
            children=[
                html.Div(
                    className="col-xs-10 mx-auto",
                    children=[
                        dcc.Graph(
                            className="mx-auto",
                            figure=figpie_comp,
                            id='pie_grap2',
                            config=dict(responsive=True),
                            style={'width': '100%'}
                        )
                    ]
                )
            ]
        ),
        html.Div(
            className="row my-2",
            children=[
                html.Div(
                    className="col-xs-10 mx-auto",
                    children=[
                        dcc.Graph(
                            figure=fig2,
                            className="mx-auto",
                            id='g1',
                            config=dict(responsive=True),
                            style={'width': '100%'}
                        )
                    ]
                )
            ]
        ),
    ]
)

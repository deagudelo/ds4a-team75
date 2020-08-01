# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_html_components as html


def Navbar(application):
    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.Div(
                    className="col-xs-12 col-sm-6 col-lg-3 px-0 text-center",
                    children=[
                        html.Img(
                            className="my-auto", src="https://team75.s3.amazonaws.com/electridash-logo.png", height="35px")
                    ]
                ),
                html.Div(
                    className="col-md-6 text-center d-none d-lg-block px-0",
                    children=[
                        html.H2("Electricity Distribution Failure Model",
                                className="my-auto", style={'color': '#FFF'})
                    ]
                ),
                html.Div(
                    className="col-sm-6 col-lg-3 text-center d-none d-sm-block px-0",
                    children=[
                        html.H2("DS4A",  style={
                            'color': '#FFF'}, className="my-auto")
                    ]
                )
            ]
        ),
        color="#83ac07"
    )
    return navbar

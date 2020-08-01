import os
import dash
import dash_html_components as html

pipol = [
    {
        "nombre": "Andres Salazar",
        "desc": "Hi, I'm Andrés",
        "img": "https://team75.s3.amazonaws.com/sandres.jpg"
    },
    {
        "nombre": "Carlos Parra",
        "desc": "Hi, I'm Carlos",
        "img": "https://team75.s3.amazonaws.com/scarlos.jpg"
    },
    {
        "nombre": "Christian Umaña",
        "desc": "Hi, I'm Christian",
        "img": "https://team75.s3.amazonaws.com/schristian.jpeg"
    },
    {
        "nombre": "Daniel Agudelo",
        "desc": "Hi I'm Daniel",
        "img": "https://team75.s3.amazonaws.com/sdaniel.jpg"
    },

]


def card(nombre, img, desc):
    return html.Div(
        className="col-xs-12 col-sm-6 col-md-4 col-lg-3 py-2",
        children=[
            html.Div(
                className="card mx-auto",
                style={
                    "width": 200
                },
                children=[
                    html.Img(
                        src=img,
                        className="card-img-top",
                        alt=nombre,
                        width=200,
                        height=200
                    ),
                    html.Div(
                        className="card-body",
                        children=[
                            html.H5(
                                className="card-title",
                                children=[
                                    nombre
                                ]
                            ),
                            html.P(
                                className="card-text",
                                children=[
                                    desc
                                ]

                            )
                        ]
                    )
                ]
            )

        ]
    )


def layout():
    return html.Div(
        className="my-2 row",
        children=[
            card(man['nombre'], man['img'], man['desc']) for man in pipol
        ]
    )

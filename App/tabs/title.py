import dash_html_components as html
from app import app


ti = html.Div(
    className='row justify-content-center',
    children=[
        html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("logoepm.png"),
                    id="epm-image",
                    className='mx-auto my-auto'
                ),
            ],
            className="col-xs-10 col-md-2 px-0 text-center"),
        html.Div(
            children=[
                html.H1(
                    'Electricity Distribution Failure Model',
                    className="mx-auto my-auto text-center"
                )
            ], className="col-xs-10 col-md-10 jumbotron vertical-center")
    ]
)

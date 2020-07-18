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
                ),
            ],
            className="col-xs-10 col-md-2"),
        html.Div(
            children=[
                html.H1(
                    'Electricity Distribution Failure Model',
                    className="mx-auto text-center"
                )
            ], className="col-xs-10")
    ]
)

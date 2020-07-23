import dash_html_components as html
import dash_core_components as dcc

listaTechLocation = ['Transformador', 'Salida Circuito',
                     'Aisladero', 'Reconectador', 'Salida_Circuito']

layout = html.Div(
    [
        html.H2('Filters'),
        html.H4('Technical location:'),
        html.Br(),
        dcc.Dropdown(
            id='techlocation',
            options=[{'label': i, 'value': i} for i in listaTechLocation],
            value='Transformador'
        ),
        html.Div([html.H5('Controls')])
    ],
    style={'marginBottom': 50, 'marginTop': 25,
           'marginLeft': 15, 'marginRight': 15}
)

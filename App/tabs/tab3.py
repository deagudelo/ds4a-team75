import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_html_components as html
import dash_core_components as dcc
from database import map_data

Map_Fig = map_data.Map_Fig

layout = html.Div([
    html.H2("Mapa de prioridades por municipio", id='title', className="mx-auto text-center"), #Creates the title of the app
    html.Div(className='container', children=[
        dcc.Graph(figure=Map_Fig,id='main-figure'),
        
    ]),
    
])

#@app.callback(Output('table-paging-with-graph-container', "children"),
#[Input('rating-95', 'value')
#, Input('price-slider', 'value')
#])




   
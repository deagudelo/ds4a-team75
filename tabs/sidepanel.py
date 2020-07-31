import dash_html_components as html
import dash_core_components as dcc
from database import transforms
import dash_bootstrap_components as dbc

listaTechLocation = ['Transformador', 'Salida Circuito',
                     'Aisladero', 'Reconectador', 'Salida_Circuito']
#df = transforms.df
df_localidad = transforms.df_localidad

layout = html.Div( 
    [
          
        
        html.H3('Dashboard filters:'),
        html.H4('Technical Location:'),
        #html.Br(),
        dcc.Dropdown(
            id='techlocation',
            options=[{'label': i, 'value': i} for i in listaTechLocation],
            value='Transformador'
        ),
           html.H4('Town:'),
                                html.Div(
                                    className="div-for-dropdown",
                                    children=[
                                        dcc.Dropdown(
                                            id='town',
                                            options=[{'label': town, 'value': town} for town in df_localidad],
                                            multi=True,
                                            placeholder='Localidad',
                                        )
                                    ]
                                ),          





        html.Div([html.H5('Controls')]) 
    ],  

    
    style={'marginBottom': 50, 'marginTop': 25,
           'marginLeft': 15, 'marginRight': 15,
           }
)
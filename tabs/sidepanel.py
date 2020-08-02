import dash_html_components as html
import dash_core_components as dcc
from database import transforms

listaTechLocation = ['AISLADERO', 'SALIDA CIRCUITO', 'TRANSFORMADOR', 'SEGMENTO','TRAMO', 'NO ESPECIFICADO', 'RECONECTADOR', 'NODO','ALIMENTADOR PRINCIPAL', 'RAMAL']

listLoc=['TURBO','NECOCLÍ','APARTADÓ','CAREPA','SAN PEDRO DE URABÁ','CHIGORODÓ','ARBOLETES','SAN JUAN DE URABÁ','MUTATÁ','CURRULAO','NUEVA COLONIA','BELEN DE BAJIRA','LA ATOYOSA','RIOSUCIO']
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
            multi=True,
            placeholder='Network Type',
            value=[]
        ),
           html.H4('Town:'),
                                html.Div(
                                    className="div-for-dropdown",
                                    children=[
                                        dcc.Dropdown(
                                            id='townlocation',
                                            options=[{'label': o, 'value': o} for o in listLoc],
                                            multi=True,
                                            placeholder='Localidad',
                                            #value=[]
                                        )
                                    ]
                                ),          
    ],  

    
    style={'marginBottom': 50, 'marginTop': 25,
           'marginLeft': 15, 'marginRight': 15,
           }
)
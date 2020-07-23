import unicodedata
import pandas as pd
import json
import plotly.express as px
import os
from application import application
from database import transforms

df = transforms.df

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
##################################################################################################
#Load the data and create the map
##################################################################################################
#df = pd.read_excel('database//uraba_all.xlsx')
with open(os.path.join(os.getcwd(), 'database', 'GeoData', 'munis-noaccents.geojson'), encoding='utf-8') as geo:
#     print(type(geo.read()))
    geojson = json.loads(geo.read())

df['town_upper'] = df.town.apply(lambda x: remove_accents(str(x).upper()))
dff = df.groupby('town_upper').mean().reset_index()
Map_Fig = px.choropleth_mapbox(dff,                          #Data
        locations='town_upper',                    #Column containing the identifiers used in the GeoJSON file
        color='Priority',                          #Column giving the color intensity of the region
        geojson=geojson,                           #The GeoJSON file
        featureidkey="properties.MPIO_CNMBR",      #Id in properties
        zoom=5,                                    #Zoom
        mapbox_style="carto-positron",             #Mapbox style, for different maps you need a Mapbox account and a token
        center={"lat": 7.88299, "lon": -76.62587}, #Center
        color_continuous_scale="Viridis",          #Color Scheme
        opacity=0.5,                               #Opacity of the map
        )

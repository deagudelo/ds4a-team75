import unicodedata
import pandas as pd
import json
import plotly.graph_objects as go
import os
from database import transforms

df = transforms.df


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


##################################################################################################
# Load the data and create the map
##################################################################################################
#df = pd.read_excel('database//uraba_all.xlsx')
with open(os.path.join(os.getcwd(), 'database', 'GeoData', 'mapasolourabaeditado.geojson'), encoding='utf-8') as geo:
    #     print(type(geo.read()))
    geojson = json.loads(geo.read())

df['town_upper'] = df.town.apply(lambda x: remove_accents(str(x).upper()))
dff = df.groupby('town_upper').mean().reset_index()


def map(zoom, colorScale, provider):
    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=geojson,
            locations=df['town_upper'],
            z=df['Priority'],
            colorscale=colorScale,
            featureidkey="properties.MPIO_CNMBR",  # Id in properties
            marker_opacity=0.5,
            marker_line_width=0,
        )
    )
    fig.update_layout(mapbox_style="carto-positron", mapbox_zoom=zoom,
                      mapbox_center={"lat": 7.88299, "lon": -76.62587})
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

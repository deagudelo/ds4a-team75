import os
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_table
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from random import randint
from pprint import pprint as pp
import re
import geopy
from geopy.geocoders import Nominatim
from assets import colors

#############################
# Load  data
#############################
path = os.path.join(os.getcwd(), 'database', 'uraba_all.xlsx')
df = pd.read_excel(path)

path2 = os.path.join(os.getcwd(), 'database', 'centrarmapa.xlsx')
dfcenter = pd.read_excel(path2)

#############
# data transformation
######################


# fill na
df.IncompleteReason = df.IncompleteReason.fillna(df.Status.apply(lambda x: 'NO APLICA'
                                                                 if x == 'Realizada' else 'NO ESPECIFICADO'))
df.RepairCode = df.RepairCode.fillna(df.Status.apply(
    lambda x: 'NO APLICA' if x == 'No Realizada' else 'NO ESPECIFICADO'))
df.town = df.town.fillna('PEQUENO CORREGIMIENTO/VEREDA')
df.CrewGeneralComments = df.CrewGeneralComments.fillna('NO ESPECIFICADO')

# Some missings can be fill with a pattern "ddd-dd.." in LocationDescription

df.Circuit = df.Circuit.fillna(df.LocationDescription.apply(lambda x: re.findall(r'\d\d\d-\d\d', x)[0]
                                                            if len(re.findall(r'\d\d\d-\d\d', x)) > 0
                                                            else 'NO ESPECIFICADO'))

df.LocationID = df.LocationID.fillna(df.LocationDescription.apply(lambda x: re.findall(r'\w?\w?\d\d\d\d?\d?\d?', x)[0]
                                                                  if len(re.findall(r'\w?\w?\d\d\d\d?\d?\d?', x)) > 0
                                                                  else 'NO ESPECIFICADO'))

df.LocationID = df.LocationID.str.replace(
    r'\d\d\d-\d\d', 'NO ESPECIFICADO', regex=True)

# location Description

location_d = df.LocationDescription.str.upper()
location_d[location_d.str.contains(
    'ALIMENTADOR PRINCIPAL')] = 'ALIMENTADOR PRINCIPAL'
location_d[location_d == 'SALIDA_CIRCUITO'] = 'SALIDA CIRCUITO'
location_d[(location_d.str.contains('RAMAL')) | (
    location_d.str.contains('RAMALES'))] = 'RAMAL'
location_d[location_d.str.contains('TRAMO')] = 'TRAMO'
location_d[location_d.str.contains('SEGMENTO')] = 'SEGMENTO'
location_d[location_d.str.contains('NODO')] = 'NODO'
location_d[location_d.str.contains('TRANSFORMADORES')] = 'TRANSFORMADOR'

location_d[~location_d.isin(
    ['TRANSFORMADOR', 'SALIDA CIRCUITO', 'AISLADERO',
     'SEGMENTO', 'TRAMO', 'RECONECTADOR', 'ALIMENTADOR PRINCIPAL',
                 'NODO', 'RAMAL'])] = 'NO ESPECIFICADO'

# *********** New variables
df['LocationResume'] = location_d
df['year'] = pd.to_datetime(df['RepairDate']).dt.to_period('Y')
df['month'] = pd.to_datetime(df['RepairDate']).dt.to_period('M')
df['year'] = df['year'].astype(str)
df['month'] = df['month'].astype(str)

# drop rows 2018 2027
df = df.drop(df[df['year'] == '2018'].index)
df = df.drop(df[df['year'] == '2027'].index)


# latitud longitud fix
df.Latitude = df.Latitude/1000000
df.Longitude = df.Longitude/1000000
df['coordenada'] = df['Latitude'].round(8).astype(
    str)+str(', ')+df['Longitude'].round(8).astype(str)

# Location fix


temp_df = df.town.value_counts().rename_axis('unique_values').to_frame('counts')
temp_df = temp_df[temp_df['counts'] < 50].index
temp_ind = df[df['town'].isin(temp_df)].index
locator = Nominatim(user_agent='myGeocoder', timeout=10)

# df['town'][2]=locator.reverse(df['coordenada'][2]).raw["address"].get("county")
# for i in temp_ind:
#					df['town'][i]=locator.reverse(df['coordenada'][i]).raw["address"].get("county")

df.town = df.town.str.replace(
    'San Pedro de Urabá', 'San pedro de urabá', regex=True)
df.town = df.town.str.replace(
    'San Juan de Urabá', 'San juan de urabá', regex=True)
df["town"] = df["town"].str.upper().astype(str)

###################
# GRAPHS
###################

num_service_type = df["ServiceType"].value_counts().reset_index()
figpie = px.pie(num_service_type, values='ServiceType',
                names='index', title='Service Type Distribution')

locres_wo = pd.read_csv(os.path.join(os.getcwd(), 'database', 'locres_wo.csv'))
figpie_comp = px.pie(locres_wo, values='LocationResume',
                     names='index', color_discrete_sequence=colors.paleta1)
figpie_comp.update_layout(
    autosize=True,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=34,
        pad=4
    )
)
figpie_comp.update_layout(
    title_text='Failure components ditribution', title_x=0.5)


num_repar_ot = df["NumberOT"].value_counts().reset_index()
fig = px.box(num_repar_ot, y="NumberOT", notched=True,
             title="Box plot of Number of reparations per Work order")

#
num_calls_ot_pri = df[["CallID", "NumberOT", "Priority"]].groupby(
    ["NumberOT", "Priority"]).count().reset_index()
fig1 = px.box(num_calls_ot_pri, x="Priority", y="CallID", color="Priority",
              notched=True, title="Box plot of Number of reparations per CallID", color_discrete_sequence=colors.paleta1)


fig2 = px.bar(num_service_type, y='ServiceType', x='index', color_discrete_sequence=colors.paleta1, labels={
              'ServiceType': 'Count', 'index': 'Type of service'})
fig2.update_layout(
    autosize=True,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=34,
        pad=4
    )
)
fig2.update_layout(title_text='Repairs by type of service', title_x=0.5)


mapbox_access_token = "pk.eyJ1IjoiY2hyaXN0aWFuYXV6IiwiYSI6ImNrY2lhMzh1cDBkMmUyc28ycTEwejQxZG8ifQ.ANShECn8rBOHPkiB04LOeA"
px.set_mapbox_access_token(mapbox_access_token)
fig_mapbox = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name='town',    color="ServiceType",  # size= 'DuratioMin',
                               color_discrete_sequence=colors.paleta1, size_max=15, mapbox_style="open-street-map")  # opacity=0.5)

fig_mapbox.update_layout(mapbox_center={"lat": 8.119863, "lon": -76.58538})
fig_mapbox.update_layout(mapbox_zoom=8)
fig_mapbox.update_layout(showlegend=False)
fig_mapbox.update_layout(
    autosize=True,
    # width=500,
    # height=500,
    margin=dict(
        l=1,
        r=1,
        b=1,
        t=33,
        pad=4
    ),
    paper_bgcolor="white",
)
fig_mapbox.update_layout(title_text="Failures Location", title_x=0.5)


# drop downs data

df_localidad = df['town'].unique()
# df_localidad.append('All')
#df_localidad = np.append (df_localidad, 'All Towns')

##########################
# graphs dinamic
########################
listaTechLocation = ['AISLADERO', 'SALIDA CIRCUITO', 'TRANSFORMADOR', 'SEGMENTO',
                     'TRAMO', 'NO ESPECIFICADO', 'RECONECTADOR', 'NODO', 'ALIMENTADOR PRINCIPAL', 'RAMAL']

listLoc = ['TURBO', 'NECOCLÍ', 'APARTADÓ', 'CAREPA', 'SAN PEDRO DE URABÁ', 'CHIGORODÓ', 'ARBOLETES',
           'SAN JUAN DE URABÁ', 'MUTATÁ', 'CURRULAO', 'NUEVA COLONIA', 'BELEN DE BAJIRA', 'LA ATOYOSA', 'RIOSUCIO']

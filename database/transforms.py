import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
#import sqlite3

from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_table
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
#from datetime import datetime as dt
#import json
from random import randint
from pprint import pprint as pp
import re
import geopy
from geopy.geocoders import Nominatim


#conn = sqlite3.connect(r"")
#c = conn.cursor()
#df = pd.read_sql("select * from ", conn)
#df = df[['country','']]
#############################
# Load  data
#############################
print("cwd:")
print(os.getcwd())
# pp(vars(app))
path = os.path.join(os.getcwd(), 'database', 'uraba_all.xlsx')
print(path)
df = pd.read_excel(path)

#############
#data transformation
######################



#fill na
df.IncompleteReason = df.IncompleteReason.fillna(df.Status.apply(lambda x: 'NO APLICA'
                                                                 if x=='Realizada' else 'NO ESPECIFICADO'))
df.RepairCode = df.RepairCode.fillna(df.Status.apply(lambda x: 'NO APLICA' if x=='No Realizada' else 'NO ESPECIFICADO'))
df.town = df.town.fillna('PEQUENO CORREGIMIENTO/VEREDA')
df.CrewGeneralComments = df.CrewGeneralComments.fillna('NO ESPECIFICADO')

# Some missings can be fill with a pattern "ddd-dd.." in LocationDescription

df.Circuit = df.Circuit.fillna(df.LocationDescription.apply(lambda x: re.findall(r'\d\d\d-\d\d', x)[0]
                                     if len(re.findall(r'\d\d\d-\d\d', x)) > 0
                                     else 'NO ESPECIFICADO' ))

df.LocationID = df.LocationID.fillna(df.LocationDescription.apply(lambda x: re.findall(r'\w?\w?\d\d\d\d?\d?\d?', x)[0]
                                     if len(re.findall(r'\w?\w?\d\d\d\d?\d?\d?', x)) > 0
                                     else 'NO ESPECIFICADO'))

df.LocationID = df.LocationID.str.replace(r'\d\d\d-\d\d', 'NO ESPECIFICADO',regex=True)

#location Description

location_d = df.LocationDescription.str.upper()
# To add Alimentador principal
location_d[location_d.str.contains('ALIMENTADOR PRINCIPAL')] = 'ALIMENTADOR PRINCIPAL'
# To unify Salida circuito
location_d[location_d=='SALIDA_CIRCUITO'] = 'SALIDA CIRCUITO'
# To add Ramal
location_d[(location_d.str.contains('RAMAL')) | (location_d.str.contains('RAMALES'))] = 'RAMAL'
# To add Tramo
location_d[location_d.str.contains('TRAMO')] = 'TRAMO'
# To add Segmento
location_d[location_d.str.contains('SEGMENTO')] = 'SEGMENTO'
# To add Nodo
location_d[location_d.str.contains('NODO')] = 'NODO'
# Plural Transformador
location_d[location_d.str.contains('TRANSFORMADORES')] = 'TRANSFORMADOR'

location_d[~location_d.isin(
                ['TRANSFORMADOR', 'SALIDA CIRCUITO', 'AISLADERO',
                 'SEGMENTO', 'TRAMO', 'RECONECTADOR', 'ALIMENTADOR PRINCIPAL',
                 'NODO', 'RAMAL'] ) ] = 'NO ESPECIFICADO'

#*********** New variables
df['LocationResume'] = location_d
df['year'] = pd.to_datetime(df['RepairDate']).dt.to_period('Y')
df['month'] = pd.to_datetime(df['RepairDate']).dt.to_period('M')
df['year']=df['year'].astype(str)
df['month']=df['month'].astype(str)

#drop rows 2018 2027
df = df.drop(df[df['year']=='2018'].index)
df = df.drop(df[df['year']=='2027'].index)


#latitud longitud fix
df.Latitude = df.Latitude/1000000
df.Longitude = df.Longitude/1000000
df['coordenada']=df['Latitude'].round(8).astype(str)+str(', ')+df['Longitude'].round(8).astype(str)

#Location fix #commented because is not workig, this code only runs in jupyter notebook?


temp_df=df.town.value_counts().rename_axis('unique_values').to_frame('counts')
temp_df=temp_df[temp_df['counts']<50].index
temp_ind=df[df['town'].isin(temp_df)].index
locator = Nominatim( user_agent='myGeocoder', timeout=10 )

#df['town'][2]=locator.reverse(df['coordenada'][2]).raw["address"].get("county")
for i in temp_ind:
					df['town'][i]=locator.reverse(df['coordenada'][i]).raw["address"].get("county")

df.town = df.town.str.replace('San Pedro de Urabá', 'San pedro de urabá',regex=True)
df.town = df.town.str.replace('San Juan de Urabá', 'San juan de urabá',regex=True)
df["town"] = df["town"].str.upper().astype(str)

###################
#GRAPHS
###################

num_service_type=df["ServiceType"].value_counts().reset_index()
figpie= px.pie(num_service_type, values='ServiceType', names='index', title='Service Type Distribution')

locres_wo = pd.read_csv('locres_wo.csv')
figpie_comp = px.pie(locres_wo, values='LocationResume', names='index', title='Failure components ditribution')

num_repar_ot=df["NumberOT"].value_counts().reset_index()
fig = px.box(num_repar_ot, y="NumberOT",notched=True, title="Box plot of Number of reparations per Work order")

#
num_calls_ot_pri=df[["CallID", "NumberOT","Priority"]].groupby(["NumberOT","Priority"]).count().reset_index()
fig1 = px.box(num_calls_ot_pri, x="Priority", y="CallID",color="Priority",notched=True, title="Box plot of Number of reparations per CallID")


fig2 = px.pie(num_service_type, values='ServiceType', names='index', title='Pie chart of the number of reparations by type of service')
fig2.update_traces(textinfo='percent+label')

mapbox_access_token = "pk.eyJ1IjoiY2hyaXN0aWFuYXV6IiwiYSI6ImNrY2lhMzh1cDBkMmUyc28ycTEwejQxZG8ifQ.ANShECn8rBOHPkiB04LOeA"
px.set_mapbox_access_token(mapbox_access_token)
fig_mapbox = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name='town',   color="ServiceType", #size= 'DuratioMin',
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,opacity=0.5)
fig_mapbox.update_layout(mapbox_style="open-street-map")
#Se podría cambiar esto por un diccionario por municipios
fig_mapbox.update_layout(mapbox_center ={"lat": 8.202578, "lon": -76.58468})
fig_mapbox.update_layout(mapbox_zoom=8)

# drop downs data

df_localidad=df['town'].unique()

##########################
#graphs dinamic
########################

def create_g1(tech,town):
        dff= df[df['LocationDescription'] == tech]
        dfg= dff.groupby(df['Circuit'])['NumberOT'].count().reset_index()
        dfg.sort_values(by=['NumberOT'], inplace=True, ascending=False)
        fig = px.bar(dfg, x='Circuit', y='NumberOT', title='Total of Work Orders by Circuit')
        fig.update_layout(transition_duration=500)
        #fig2=fig
        return fig

def create_g2(tech,town):
		dff= df[df['year'] == '2019']
		dfg= dff.groupby(['month','town'])['NumberOT'].count().reset_index()
		fig2 = px.line(dfg, x="month", y="NumberOT", color='town')
		return fig2

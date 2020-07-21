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
#import matplotlib.pyplot as plt
#import seaborn as sns
#import folium
#from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#from app import app




#conn = sqlite3.connect(r"")
#c = conn.cursor()
#df = pd.read_sql("select * from ", conn)
#df = df[['country','']]
#############################
# Load  data
#############################
df = pd.read_excel('uraba_all.xlsx')
df.Latitude = df.Latitude/1000000
df.Longitude = df.Longitude/1000000

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
fig_mapbox = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",    color="ServiceType", #size= 'DuratioMin',
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,opacity=0.5)
fig_mapbox.update_layout(mapbox_style="open-street-map")
#Se podría cambiar esto por un diccionario por municipios
fig_mapbox.update_layout(mapbox_center ={"lat": 8.202578, "lon": -76.58468})
fig_mapbox.update_layout(mapbox_zoom=8)

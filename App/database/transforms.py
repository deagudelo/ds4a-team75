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
df = pd.read_excel('database//Muestra de datos_20200505.xlsx', sheet_name='Hoja1')
df.Latitude = df.Latitude/1000000
df.Longitude = df.Longitude/1000000

df.Priority.unique()
priority_colors = ['#%02x%02x%02x' % (255, 0+(i*30), 0) for i in range(len(df.Priority.unique()))]
priority_colors = list(reversed(priority_colors))
priority_col_dict = dict(zip(df.Priority.unique(),priority_colors[-1::-1]))

num_service_type=df["ServiceType"].value_counts().reset_index()
figpie= px.pie(num_service_type, values='ServiceType', names='index', title='Service Type Distribution')

locres_wo = pd.read_csv('database//locres_wo.csv')
figpie_comp = px.pie(locres_wo, values='LocationResume', names='index', title='Failure components ditribution')

num_repar_ot=df["NumberOT"].value_counts().reset_index() 
fig = px.box(num_repar_ot, y="NumberOT",notched=True, title="Box plot of Number of reparations per Work order")

#
num_calls_ot_pri=df[["CallID", "NumberOT","Priority"]].groupby(["NumberOT","Priority"]).count().reset_index()
fig1 = px.box(num_calls_ot_pri, x="Priority", y="CallID",color="Priority",notched=True, title="Box plot of Number of reparations per CallID")


fig2 = px.pie(num_service_type, values='ServiceType', names='index', title='Pie chart of the number of reparations by type of service')
fig2.update_traces(textinfo='percent+label')



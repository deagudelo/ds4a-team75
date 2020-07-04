import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import sqlite3

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
regions = df.Region.unique()
regions_colors = ['#%06X' % randint(0, 0xFFFFFF) for i in range(len(regions))]
regions_col_dict = dict(zip(regions,regions_colors))
regions_col_dict

df.Priority.unique()
priority_colors = ['#%02x%02x%02x' % (255, 0+(i*30), 0) for i in range(len(df.Priority.unique()))]
priority_colors = list(reversed(priority_colors))
priority_col_dict = dict(zip(df.Priority.unique(),priority_colors[-1::-1]))

num_service_type=df["ServiceType"].value_counts().reset_index()
figpie= px.pie(num_service_type, values='ServiceType', names='index', title='Service Type Distribution')

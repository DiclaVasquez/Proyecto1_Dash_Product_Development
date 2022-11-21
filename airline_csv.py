import dash
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sqlalchemy
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html

import dataorigen
import styles
from app import app, server

df = dataorigen.cant_vuelos_df
print(df)

carrier_vuelo = df['carrier'].unique()

content = html.Div([html.H1("Vuelos_por_carrier"),
                    html.Br(),
                    html.Hr(),
                    dcc.Dropdown(id='carrierss', options=carrier_vuelo, value='UA'),
                    dcc.Graph(id='serie_temporal2')])

@app.callback(Output("serie_temporal2","figure"),
              Input("carrierss", "value"))

def set_vuelos_por_carrier(carrierf):
    df['carrier'] = df['carrier'].astype(str)
    df['time_hour'] = pd.to_datetime(df['time_hour'], infer_datetime_format=True) #format= '%Y%m%d')
    df_filtrado = df[df['carrier'] == carrierf]
    df_filtrado.sort_values(by='time_hour',inplace=True)  # type: ignore
    df_final = df_filtrado.groupby(pd.Grouper(key='time_hour', freq='1D')).sum()
    df_final.reset_index(inplace=True)
    #print(df_final)
    #Zeta = np.random.poisson(size=(len('carrier'), len('flight')))
    fig = go.Figure(data=go.Heatmap(
                   z=df['CounV'],
                   x=df['carrier'],
                   y=df['time_hour'],
                   hoverongaps = False))
    #fig = px.line(df_final, x='time_hour', y='flight')
    #fig.update_traces(line_color='#78c2ad')
    return fig
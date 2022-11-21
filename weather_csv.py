import dash
import dash_bootstrap_components as dbc
#import dash_core_components as dcc
#import dash_html_components as html
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

df2 = dataorigen.dim_weather
df=df2.assign(CounV=1)
print(df)

origen_vuelo_dos = df['origin'].unique()

content = html.Div([html.H1("Condiciones Climaticas"),
                    html.Br(),
                    html.Hr(),
                    dcc.Dropdown(id='climas', options=origen_vuelo_dos, value='EWR'),
                    dcc.Graph(id='serie_temporal_dos')])

@app.callback(Output("serie_temporal_dos","figure"),
              Input("climas", "value"))

def set_clima(origin_filtro):
    df['origin'] = df['origin'].astype(str)
    df['time_hour'] = pd.to_datetime(df['time_hour'], infer_datetime_format=True) #format= '%Y%m%d')
    df_filtrado = df[df['origin'] == origin_filtro]
    df_filtrado.sort_values(by='time_hour',inplace=True)  # type: ignore
    df_final = df_filtrado.groupby(pd.Grouper(key='time_hour', freq='1D')).sum()
    df_final.reset_index(inplace=True)
    print(df_final)
    trace0 = go.Scatter(
        x= df_final.time_hour,
        y= df_final.temp,
        mode='markers',
        name='Tempratura'        
    )
    trace1 = go.Scatter(
        x= df_final.time_hour,
        y= df_final.humid,
        mode='lines',
        name='Humedad relativa'        
    )
    trace2 = go.Scatter(
        x= df_final.time_hour,
        y= df_final.wind_speed,
        mode='lines',
        name='Velocidad del viento'        
    )
    trazos = [trace0,trace1,trace2]
    layout= go.Layout(title="Indicadores")
    fig= go.Figure(data=trazos, layout=layout)
    # fig = px.line(df_final, x='time_hour', y='temp')
    # fig.update_traces(line_color='#78c2ad')
    return fig

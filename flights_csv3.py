import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import styles
from dash.dependencies import Input, Output, State
import sqlalchemy
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from datetime import datetime

from app import app
from app import server
import data                
from dash import Dash, dcc, html, Input, Output
import plotly.express as px


content = html.Div([
    html.H1('Stock price analysis2'),
    dcc.Graph(id="time-series-chart2"),
    html.P("Select stock2:"),
    dcc.Dropdown(
        id="url",
        options=["EWR", "JFK", "LGA"],
        value="EWR",
        clearable=False,
    ),
])


@app.callback(
    Output("time-series-chart2", "fig"), 
    Input("url", "value"))
def display_time_series2(origin2):
    df = data.cant_vuelos_df
    df = df.sort_values(by='month')
    #df = px.data.stocks() # replace with your own data source
    fig = px.line(df, x='month', y='origin', title='Sorted Input')
    
    return fig
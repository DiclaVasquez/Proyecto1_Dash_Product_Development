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
    html.H1('Stock price analysis'),
    dcc.Graph(id="time-series-chart"),
    html.P("Select stock:"),
    dcc.Dropdown(
        id="ticker",
        options=["AMZN", "FB", "NFLX"],
        value="AMZN",
        clearable=False,
    ),
])


@app.callback(
    Output("time-series-chart", "figure"), 
    Input("ticker", "value"))
def display_time_series(ticker):
    df = px.data.stocks() # replace with your own data source
    fig = px.line(df, x='date', y=ticker)
    return fig




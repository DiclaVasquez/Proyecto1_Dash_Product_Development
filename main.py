import dash
#import dash_core_components as dcc
#import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from flask import Flask, request
import flask
import requests
import styles
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash import dcc
from dash import html

#llamada a paginas externas
import pages.flights_csv as flights_csv
import pages.airline_csv as airline_csv
import pages.airplanes_csv as airplanes_csv
import pages.weather_csv as weather_csv
import pages.error as error

#admin123
from app import app
from app import server
import dataorigen

sidebare = html.Div(children=[
    html.H1("Dashboard"),
    html.Hr(),
    dbc.Nav([
        dbc.NavLink('Cantidad de Vuelos', href="/flights_csv", active="exact"),
        dbc.NavLink('Vuelos por Carrier', href="/airline_csv", active="exact"),
        dbc.NavLink('Estadistica de Vuelos', href="/airplanes_csv", active="exact"),
        dbc.NavLink('Clima por origen', href="/weather_csv", active="exact"),
    ],
    vertical=True,
    pills=True),
    ],style=styles.SIDEBAR_STYLE
)

content = html.Div(id="page-content", style=styles.CONTENT_STYLE)

app.layout = html.Div(children=[dcc.Location(id="url"), sidebare, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == '/flights_csv':
        return flights_csv.content
    elif pathname == '/airline_csv':
        return airline_csv.content
    elif pathname == '/airplanes_csv':
        return airplanes_csv.content
    elif pathname == '/weather_csv':
        return weather_csv.content
    else:
        return error.content
    
    
if __name__ == '__main__':
    app.run_server(port=4050)


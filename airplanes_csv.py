import dash
from dash import dcc
from dash import html
# import dash_html_components as html
# import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dataorigen
import styles
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

from app import app
from app import server


import pandas as pd
est3_df = pd.merge(dataorigen.dim_flights, dataorigen.dim_planes,left_on='tailnum', right_on='tailnum',how='left')
opc_tail = est3_df['tailnum'].unique()

content = html.Div([
                    html.H1("Airplanes"), 
                    html.Hr(),
                    html.H3("Selecciona un numero de avión"),
                    dcc.Dropdown(id='paises', options=opc_tail, value='N14228'),
                    html.Hr(),
                    html.H3("Selecciona variables de analisis"),
                    dbc.RadioItems(
                       options=[
                            {"label": "Tiempo en el aire", "value": 1},
                            {"label": "Distancia", "value": 2},
                        ], value=1,id="radioitems-input"),
                    dcc.Graph(id='airtime')
                    ])


# @app.callback(
#               Output("airtime", "figure"),
#             [  
#               Input("paises", "value"),
#               Input("radioitems-input", "value")
#             ] 
#               )



# def set_sales_by_country(origin_filtro, value_items):
#     est3_df['tailnum'] = est3_df['tailnum'].astype(str)
    
#     aire = est3_df[est3_df['tailnum']==origin_filtro].groupby(by=['tailnum', 'month']).agg({'air_time': ['mean', 'median', 'max', 'min', 'std']}).reset_index()
#     distancia = est3_df[est3_df['tailnum']==origin_filtro].groupby(by=['tailnum', 'month']).agg({'distance': ['mean', 'median', 'max', 'min', 'std']}).reset_index()
#     aire.columns = aire.columns.droplevel()
#     encabezados = aire.columns.to_list()
    
#     encabezados[0]='Avion'
#     encabezados[1]='Mes'
#     aire.columns = encabezados
#     distancia.columns = distancia.columns.droplevel()
#     distancia.columns = encabezados
    
#     aire = aire.set_index(['Avion', 'Mes']).stack().reset_index()
#     aire.columns = ['avion', 'num', 'estadistica', 'calculo']
#     dict_mes = {
#     1:'ene', 2:'feb', 3:'mar', 4:'abr', 5:'may', 6:'jun', 
#     7:'jul', 8:'ago', 9:'sep', 10:'oct', 11:'nov', 12:'dic'}
#     aire['meses'] = aire['num'].map(dict_mes)

#     distancia = distancia.set_index(['Avion', 'Mes']).stack().reset_index()
#     distancia.columns = ['avion', 'num', 'estadistica', 'calculo']
#     dict_mes = {
#     1:'ene', 2:'feb', 3:'mar', 4:'abr', 5:'may', 6:'jun', 
#     7:'jul', 8:'ago', 9:'sep', 10:'oct', 11:'nov', 12:'dic'}
#     distancia['meses'] = distancia['num'].map(dict_mes)
#     if value_items==1:
#         fig = px.bar(aire, x="meses", y="calculo", color="estadistica", text_auto=True, barmode='group')
#     elif value_items==2:
#         fig = px.bar(distancia, x="meses", y="calculo", color="estadistica", text_auto=True, barmode='group')
#     return fig
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime


dim_flights = pd.read_csv('C:/Users/Usuario/Documents/Carlos/01 Data Product Development/Lab_1/flights.csv')
dim_airlines = pd.read_csv('C:/Users/Usuario/Documents/Carlos/01 Data Product Development/Lab_1/airlines.csv')
dim_airports = pd.read_csv('C:/Users/Usuario/Documents/Carlos/01 Data Product Development/Lab_1/airports.csv')
dim_planes = pd.read_csv('C:/Users/Usuario/Documents/Carlos/01 Data Product Development/Lab_1/planes.csv')
dim_weather = pd.read_csv('C:/Users/Usuario/Documents/Carlos/01 Data Product Development/Lab_1/weather.csv')
cant_vuelos_df = pd.merge(dim_flights,dim_airlines,left_on='carrier', right_on='carrier',how='left')
cant_vuelos_df=cant_vuelos_df.assign(CounV=1)




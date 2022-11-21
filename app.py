import dash
import dash_bootstrap_components as dbc
import dash_auth

app = dash.Dash(suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.MINTY])
server = app.server

auth = dash_auth.BasicAuth(
    app,
    { 'admin': 'admin123',
     'laboratorio1': 'contrasena'}
)
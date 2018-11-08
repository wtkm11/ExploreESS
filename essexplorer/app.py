"""
Set up the Dash application
"""
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("European Social Survey",),
])

"""
Set up the Dash application
"""
import dash
import dash_core_components as dcc
import dash_html_components as html

from essexplorer.features.summary import summary_table

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("European Social Survey",),
    html.H2("Summary statistics",),
    summary_table,
    html.P(
        (
            "The data displayed has not been weighted to account for "
            "differences in the likelihood that a respondent was a part of "
            "the sample."
        ),
        id="weights-note"
    )
])

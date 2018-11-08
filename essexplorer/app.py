"""
Set up the Dash application
"""
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from essexplorer.layout.summary import summary_table
from essexplorer.layout.histogram import (
    hist, hist_get_figure, hist_variable_selection
)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    # Title
    html.H1("European Social Survey",),

    # Summary statistics
    html.H2("Summary statistics",),
    summary_table,

    # Distributions
    html.H2("Histograms",),
    hist_variable_selection,  # Dropdown
    hist,  # Graph

    # Weights note
    html.P(
        (
            "The data displayed has not been weighted to account for "
            "differences in the likelihood that a respondent was a part of "
            "the sample."
        ),
        id="weights-note"
    )
])

# Apply callbacks
app.callback(
    Output(component_id="hist", component_property="figure"),
    [Input(component_id="hist_variable_selection", component_property="value")]
)(hist_get_figure)

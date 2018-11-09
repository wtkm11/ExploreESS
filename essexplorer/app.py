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
from essexplorer.layout.correlations import (
    correlations, descriptions_table
)
from essexplorer.layout.prediction import fitdescription, model

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    # Title
    html.H1("European Social Survey: Exploring trust"),

    # Summary statistics
    html.Section(
        children=[
            html.H2("Summary statistics"),
            summary_table
        ],
        className="summary-stats"
    ),

    # Distributions
    html.Section(
        children=[
            html.H2("Histograms",),
            html.Div(
                children=[
                    html.Span("Select a variable: ", id="varselect_label"),
                    hist_variable_selection,  # Dropdown
                ],
                className="histogram-selection"
            ),
            hist  # Graph
        ],
        className="histograms"
    ),

    # Correlations
    html.Section(
        children=[
            html.H2("Pearson's correlation coefficients",),
            correlations,
            descriptions_table,
        ],
        className="correlations"
    ),

    # Prediction
    html.Section(
        children=[
            html.H2("Predicting the public's trust in politicians"),
            html.P(
                "We can use multivariate least squares to develop a model that "
                "can predict trust in politicians based on responses to other "
                "questions."
            ),
            model,
            fitdescription,
        ],
        className="prediction"
    ),

    # Weights note
    html.Section(
        html.P(
            (
                "The data displayed has not been weighted to account for "
                "differences in the likelihood that a respondent was a part of "
                "the sample."
            ),
            id="weights-note"
        )
    )
])

# Apply callbacks
app.callback(
    Output(component_id="hist", component_property="figure"),
    [Input(component_id="hist_variable_selection", component_property="value")]
)(hist_get_figure)

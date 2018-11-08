"""
Display a histogram
"""
import dash_core_components as dcc
import numpy as np
import plotly.graph_objs as go

from essexplorer.config import DEFAULT_HIST_SELECTION
from essexplorer.dataframes import trust
from essexplorer.data.variable_descriptions import TRUST_VARS

hist_variable_selection = dcc.Dropdown(
    options=[
        {"label": description, "value": varname}
        for varname, description in TRUST_VARS.items()
    ],
    value=trust.columns[0],
    id="hist_variable_selection"
)

def hist_get_figure(varname: str) -> go.Figure:
    """
    Compute a histogram

    Parameters
    ----------
    varname : str
        The variable for which to generate the histogram figure

    Returns
    -------
    go.Figure
        The histogram figure
    """
    description = TRUST_VARS.get(varname, "?")
    hist_data, bin_edges = np.histogram(trust[varname].dropna())
    return go.Figure(
        data=[
            go.Bar(
                y=hist_data,
                x=bin_edges,
                name=description,
                marker=go.bar.Marker(color='rgb(55, 83, 109)')
            ),
        ],
        layout=go.Layout(
            title="{} histogram".format(description),
            showlegend=True,
            legend=go.layout.Legend(x=0,y=1.0),
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
        )
    )

hist = dcc.Graph(
    figure=hist_get_figure(DEFAULT_HIST_SELECTION),
    style={"height": 300},
    id="hist"
)

"""
Pearson correlation coefficients
"""
import base64
import io

import dash_html_components as html
import dash_table
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from essexplorer.dataframes import trust_corr
from essexplorer.data.variable_descriptions import TRUST_VARS

# Build a heatmap showing the Pearson's correlation coefficients
figure = plt.figure()
plt.imshow(trust_corr)
axis = plt.gca()  # Get the current axis

# Show ticks and labels
labels = [
    "{}...".format(TRUST_VARS.get(col, "?")[:20]) for col in trust_corr.columns
]
axis.set_xticks(np.arange(trust_corr.shape[1]))
axis.set_yticks(np.arange(trust_corr.shape[0]))
axis.set_xticklabels(trust_corr.columns, fontdict={"fontsize": 8})
axis.set_yticklabels(trust_corr.columns, fontdict={"fontsize": 8})

# Rotate the x-labels so that they're easier to read
plt.setp(
    axis.get_xticklabels(),
    rotation=45,
    ha="right",
    rotation_mode="anchor"
)
plt.tight_layout()  # Make space for axis labels

plt.colorbar()  # Add a colorbar

# Output the figure as a string encoded in base64
bytes_file = io.BytesIO()
figure.savefig(bytes_file, dpi=figure.dpi, format="png")
encoded_figure = base64.b64encode(bytes_file.getvalue()).decode("UTF-8")

# Create an HTML image tag to display the image data
correlations = html.Img(
    src='data:image/png;base64,{fig}'.format(fig=encoded_figure)
)

descriptions_table = html.Table(
    # Header
    [html.Tr([html.Th(col) for col in ["Variable name", "Description"]])] +

    # Body
    [html.Tr([html.Td(var), html.Td(desc)]) for var, desc in TRUST_VARS.items()]
)

"""
Predict trust in politicians using multivariate least squares regression
"""
import dash_html_components as html
import numpy as np

from essexplorer.dataframes import trust

trust = trust.dropna()
trstplt = trust["trstplt"]
del trust["trstplt"]
x, residuals, rank, s = np.linalg.lstsq(trust, trstplt, rcond=None)

r2 = (1 - residuals / (trstplt.size * trstplt.var()))[0]

model = html.Div(
    "trstplt = " + " + ".join(
        "{:.2f} * {}".format(coef, varname)
        for coef, varname in zip(x, trust.columns)
    ),
    id="model"
)
fitdescription = html.Div(
    "Respondents' answers to the other questions explain {0:.2f}% of the "
    "variation in trstplt.".format(100*r2),
)

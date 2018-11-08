"""
Display summary statistics
"""
import dash_html_components as html
import dash_table

from essexplorer.dataframes import trust
from essexplorer.data.variable_descriptions import TRUST_VARS

trust_summary = trust.describe().T
trust_summary["variable"] = trust_summary.index
trust_summary["question"] = [
    TRUST_VARS.get(var, "?")
    for var in trust_summary.variable
]
trust_summary = trust_summary[
    [
        "question",
        "mean",
        "std",
        "min",
        "25%",
        "50%",
        "75%",
        "max"
    ]
].round(2)

summary_table = dash_table.DataTable(
    id="summary",
    columns=[{"name": col, "id": col} for col in trust_summary.columns],
    data=trust_summary.to_dict("rows"),
)

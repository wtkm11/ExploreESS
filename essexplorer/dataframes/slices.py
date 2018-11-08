"""
Slices of the ESS dataframe
"""
from essexplorer.dataframes import ess
from essexplorer.data.variable_descriptions import TRUST_VARS

trust = ess[list(TRUST_VARS.keys())]

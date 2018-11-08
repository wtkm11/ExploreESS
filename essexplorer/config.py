"""
Configuration settings
"""
from pkg_resources import resource_filename

# File paths
ESS_DATA = resource_filename('essexplorer.data', "ESS8e02.csv")
MISSING_VALUES = resource_filename('essexplorer.data', "missing_values.txt")

# Defaults
DEFAULT_HIST_SELECTION = "ppltrst"

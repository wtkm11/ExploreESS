"""
The ESS dataframe
"""
from collections import namedtuple
from typing import List, Tuple

import numpy as np
import pandas as pd

from essexplorer.config import ESS_DATA, MISSING_VALUES

def parse_missing_values_line(line: str) -> Tuple[str, List[str]]:
    """
    Parse a line of the missing values file

    Parameters
    ----------
    line : str
        The line to parse

    Returns
    -------
    Tuple[str, List[str]]
        A tuple containing the variable name and a list of values that should be
        treated as "missing" or null
    """
    split_line = line.strip().split(" ")
    return split_line[0], list(map(int, split_line[1:]))

# Parse the missing values file and create a lookup dictionary
with open(MISSING_VALUES) as f:
    missing_vals = dict(list(map(parse_missing_values_line, f.readlines())))

# Load the raw ESS data
ess = pd.read_csv(ESS_DATA, usecols=list(missing_vals.keys()))

# Replace missing values with `np.nan`
for varname, values in missing_vals.items():
    if values:
        ess[varname].replace(values, np.nan, inplace=True)

"""
Pearson correlation coefficients
"""
from essexplorer.dataframes import trust

trust_corr = trust.corr(method="pearson").round(3)

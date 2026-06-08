import pandas as pd

def cross_tab(data, row_col, col_col):
    """
    Returns: nested dict {col_value: {row_value: frequency}}
    """
    df = pd.DataFrame(data)

    result = pd.crosstab(df[row_col], df[col_col])

    return result.to_dict()
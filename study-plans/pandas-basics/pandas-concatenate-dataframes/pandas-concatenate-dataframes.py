import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    df = [pd.DataFrame(df) for df in dfs]
    result = pd.concat(df)

    return [result.shape, result.to_dict('list')]

    
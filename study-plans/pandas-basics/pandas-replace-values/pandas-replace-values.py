import pandas as pd

def replace_values(data, column, old_val, new_val):
    """
    Returns: dict with 'data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)

    new_df = df.copy()

    new_df[column] = new_df[column].replace(old_val, new_val)

    compare = df.compare(new_df)

    return {
        'data': new_df.to_dict('list'),
        'count': compare.shape[0]
    }

    
    
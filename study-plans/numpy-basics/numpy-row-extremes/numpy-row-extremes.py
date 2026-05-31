import numpy as np

def row_extremes(data):
    """Returns: np.ndarray of shape (4, m), rows are max_val, max_col, min_val, min_col"""
    arr = np.array(data, dtype=np.float64)

    row_min = arr.min(axis=1)
    row_max = arr.max(axis=1)

    col_min = arr.argmin(axis=1)
    col_max = arr.argmax(axis=1)

    return [row_max, col_max, row_min, col_min]
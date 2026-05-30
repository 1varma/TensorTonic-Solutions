import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    arr = np.asarray(data, dtype=np.float64)

    arr = arr[row_idx]

    m1 = np.where(arr > lo, arr, lo)
    m2 = np.where(arr < hi, m1, hi)

    return [arr, m2]
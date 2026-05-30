import numpy as np

def norm_diff(a, b, lo, hi):
    """Returns: np.ndarray of absolute differences after clipping and rescaling to [0, 1]"""
    arr_a = np.array(a, dtype = np.float64)
    arr_b = np.array(b, dtype = np.float64)

    a = np.clip(arr_a, lo, hi)
    b = np.clip(arr_b, lo, hi)

    a_norm = (a - lo) / (hi - lo)
    b_norm = (b - lo) / (hi - lo)

    return np.abs(a_norm - b_norm)
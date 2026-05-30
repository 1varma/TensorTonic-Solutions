import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    
    arr = np.array(data, dtype=np.float64)

    mask = arr > threshold

    any_mask = np.any(arr > threshold, axis = 1, keepdims = True)
    all_mask = np.all(arr > threshold, axis = 1, keepdims = True)

    row_any_arr = np.where(any_mask, arr, 0.0)
    row_all_arr = np.where(all_mask, arr, 0.0)

    return [mask, row_any_arr, row_all_arr]
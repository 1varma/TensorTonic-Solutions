import numpy as np

def winsorize(data, lo_q, hi_q):
    """Returns: np.ndarray of shape (3, m, n), stacked clipped values, lo_mask, hi_mask"""
    arr = np.asarray(data, dtype=np.float64)
    
    lo_bounds = np.percentile(arr, lo_q, axis=0)
    hi_bounds = np.percentile(arr, hi_q, axis=0)
    
    clipped_data = np.clip(arr, lo_bounds, hi_bounds)
    
    low_mask = (arr < lo_bounds).astype(np.float64)
    high_mask = (arr > hi_bounds).astype(np.float64)
    
    return np.stack([clipped_data, low_mask, high_mask])
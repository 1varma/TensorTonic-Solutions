import numpy as np

def summarize(data, axis):
    """Returns: np.ndarray of shape (4, k), rows are mean, std, min, max"""    
    arr = np.array(data, dtype=np.float64)

    return [np.mean(arr, axis), np.std(arr, axis), np.min(arr, axis), np.max(arr, axis)]
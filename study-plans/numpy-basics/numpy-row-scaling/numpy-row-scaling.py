import numpy as np

def scale_rows(data, weights):
    """Returns: np.ndarray of shape (m, n), each row scaled by corresponding weight"""
    #return np.diag(np.array(weights)) @ np.array(data)
    #return np.array(data) * np.array(weights)[:, None]

    a = np.array(data)
    w = np.array(weights)

    return a*w[:, np.newaxis]
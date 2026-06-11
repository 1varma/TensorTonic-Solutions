import numpy as np

def outer_product(u, v):
    """
    Returns: float64 matrix of shape (m, n), the outer product u v^T.
    """
    return np.outer((np.asarray(u, dtype=float)),(np.asarray(v, dtype=float))).tolist()
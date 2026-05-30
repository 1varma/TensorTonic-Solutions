import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""
    x = np.array(X, dtype=np.float64)
    w = np.array(W, dtype=np.float64)

    z = x@w

    norms = np.linalg.norm(z, axis=1)

    return np.where(norms[:, np.newaxis] >= threshold, z, 0.0)

    
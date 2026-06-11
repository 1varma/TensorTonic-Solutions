import numpy as np

def vector_norms(v):
    """
    Returns: float64 array of shape (3,) containing [L1, L2, L-inf] norms.
    """
    v = np.asarray(v, dtype=float)

    l1 = float(np.linalg.norm(v, ord=1))
    l2 = float(np.linalg.norm(v))
    l = float(np.linalg.norm(v, ord=np.inf))

    return [l1, l2, l]
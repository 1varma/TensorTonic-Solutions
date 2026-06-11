import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    x = np.array(x,dtype=float)
    y = np.array(y,dtype=float)

    return float(np.linalg.norm(x-y))
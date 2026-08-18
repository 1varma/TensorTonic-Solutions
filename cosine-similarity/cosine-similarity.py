import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.array(a)
    b = np.array(b)

    num = a@b
    denom = np.linalg.norm(a)*np.linalg.norm(b)

    if num > 0:
        return num/denom
    elif num == 0:
        return 0
    else:
        return num/denom
import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mode = Counter(x)
    x = np.asarray(x)

    return (np.mean(x), np.median(x), mode.most_common(1)[0][0])
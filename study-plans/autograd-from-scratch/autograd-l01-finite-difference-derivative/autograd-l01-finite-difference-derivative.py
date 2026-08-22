import numpy as np

def finite_difference_derivative(coefficients, x, h):
    """
    Returns: the polynomial value at x, the value at x plus h, and the forward-difference slope
    """
    coefficients = np.asarray(coefficients, dtype=float)
    
    # Initialize at 0.0 instead of None
    polynomial = 0.0
    for i in range(len(coefficients)):
        polynomial += coefficients[i] * (x ** i)

    forward_difference = 0.0
    for i in range(len(coefficients)):
        forward_difference += coefficients[i] * ((x + h) ** i)

    # Compute the forward-difference slope
    slope = (forward_difference - polynomial) / h

    return (polynomial, forward_difference, slope)
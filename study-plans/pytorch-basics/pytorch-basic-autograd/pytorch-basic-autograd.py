import torch

def compute_gradient(values):
    """
    Returns: list of float gradient values dy/dx
    """
    values = torch.tensor(values)

    result = values.pow(2) *3 + 2

    return result.tolist()
import torch

def create_tensor(method, shape, value=0.0):
    """
    Returns: list
    """
    if method == 'zeros':
        return torch.zeros(shape)
    if method == 'ones':
        return torch.ones(shape)
    if method == 'full':
        return torch.full(shape, value)
    if method == 'eye':
        return torch.eye(value)
    if method == 'arange':
        return torch.arange(shape)
    if method == 'linspace':
        return torch.linspace(shape)
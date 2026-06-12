import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    x = torch.tensor(x).float()

    if op == 'flatten':
        return torch.flatten(x)
    if op == 'squeeze':
        return torch.squeeze(x)
    if op == 'transpose':
        return torch.transpose(x, 0, 1)
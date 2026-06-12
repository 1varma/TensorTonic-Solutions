import torch
import torch.nn.functional as F

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    x = torch.tensor(x, dtype=torch.float32)

    if method == 'tanh':
        return torch.tanh(x).tolist()
    if method == 'sigmoid':
        return torch.sigmoid(x).tolist()
    if method == 'leaky_relu':
        # Use the functional version of leaky_relu
        return F.leaky_relu(x).tolist()
        
    return torch.relu(x).tolist()
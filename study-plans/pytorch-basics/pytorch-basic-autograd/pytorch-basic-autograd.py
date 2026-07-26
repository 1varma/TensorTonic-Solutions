import torch

def compute_gradient(values):
    """
    Returns: list of float gradient values dy/dx
    """
    def f(x):
        return (x**3 + 2 * x).sum()

    x = torch.tensor(values, dtype=torch.float32)
    
    # torch.func.grad returns a new function that computes the gradient
    df = torch.func.grad(f)
    
    return df(x).tolist()
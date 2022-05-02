import torch
# define custom losses

def my_loss(output, target):
    return torch.mean((output - target) ** 2)

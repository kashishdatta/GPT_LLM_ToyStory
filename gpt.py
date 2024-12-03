import torch
import torch.nn as nn
from torch.nn import functional as F

batch_size = 32
block_size = 128
max_iters = 5000
eval_interval = 300
learning_rate = 1e-4
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 200
n_embd = 128
n_head = 6
n_layer = 6
dropout = 0.2


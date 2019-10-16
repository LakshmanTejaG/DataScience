#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: lakshmanteja

%reset -f
%clear -f

"""

import torch

torch.manual_seed(1)
from torch.nn import Linear

model = Linear(in_features=1, out_features=1, bias=True)
print(model.bias, model.weight)
x = torch.tensor([[2.0],[3.0]])
print(model(x))

##########################################################

import torch
import torch.nn as nn

class LR(nn.Module):
    def __init__(self,input_size, output_size):
        super().__init__()
        self.linear = nn.Linear(input_size,output_size)
    def forward(self,x):
        pred = self.linear(x)
        return pred

torch.manual_seed(1)

model = LR(1,1)

x = torch.tensor([2.0])
print(model.forward(x))

#######################################################

# Importing the required libraries
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

x= torch.randn(100,1)*10
print(x)
y= x + 3*torch.randn(100,1)

plt.plot(x.numpy(), y.numpy(), 'o')
plt.xlabel('X')
plt.ylabel('Y')

# Initialize the class 
class LR(nn.Module):
  def __init__(self, input_size, output_size):
    super().__init__()
    self.linear = nn.Linear(input_size, output_size)
  def forward(self, x):
    pred = self.linear(x)
    return pred

torch.manual_seed(1)
model = LR(1, 1)
print(model)

[w, b] = model.parameters()
def get_params():
  return (w[0][0].item(), b[0].item())

# Plotting the datasets
def plot_fit(title):
  plt.title = title
  w1, b1 = get_params()
  x1 = np.array([-30, 30])
  y1 = w1*x1 + b1
  plt.plot(x1, y1, 'r')
  plt.scatter(x, y)
  plt.show()
  
plot_fit('Initial Model')
  
# Specifying Loss and Optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

#Training Model
epochs = 100
losses = []
for i in range(epochs):
  y_pred = model.forward(x)
  loss = criterion(y_pred, y)
  print("epoch:", i, "loss:", loss.item())
  
  losses.append(loss)
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
  
# Plotting Loss at Various Epochs
plt.plot(range(epochs), losses)
plt.ylabel('Loss')
plt.xlabel('epoch')

#Plotting Trained Model
plot_fit("Trained Model") 

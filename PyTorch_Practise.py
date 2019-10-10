#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:43:01 2019

@author: lakshmanteja
"""

import torch
import numpy as np
import matplotlib.pyplot as plt

teja = torch.tensor([1,2,3,4,5,6])
teja
teja[0].dtype
lakshman = torch.FloatTensor([1,2,3,4,5,6])
lakshman.size()
teja.view(3,2)
lakshman.view(6,1)

#Creating numpy array
ganta = np.array([1,2,3,4,5,6])
ganta

#Converting Numpy array to tensor array
ganta_tensor = torch.from_numpy(ganta)
ganta_tensor

#Converting Tensor array to Numpy array
ganta_numpy = ganta_tensor.numpy()
ganta_numpy

sampath = torch.tensor([1,2,3])
ramteja = torch.tensor([1,2,3])
sampath + ramteja
sampath * 5

dot_vector = torch.dot(sampath,ramteja) # it multipy the two vectors
dot_vector

lin_space_x = torch.linspace(0,10,5)

lin_space_y = torch.exp(lin_space_x)

plt.plot(lin_space_x,lin_space_y)
plt.show()
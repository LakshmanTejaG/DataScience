#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:14:29 2019

@author: lakshmanteja
"""

%reset -f 
%clear -f

# Importing the required package libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the dataset
wine = pd.read_csv('Wine.csv')
wine.head()
wine_IV = wine.iloc[:,0:13].values
wine_DV = wine.iloc[:,13]

# Splitting the dataset into training and test datasets
from sklearn.model_selection import train_test_split
wine_IV_train, wine_IV_test, wine_DV_train, wine_DV_test = train_test_split(wine_IV,wine_DV, test_size=0.2, random_state=0)

# Feature Scalling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
wine_IV_train = sc.fit_transform(wine_IV_train)
wine_IV_test = sc.transform(wine_IV_test)

# Applying PCA
from sklearn.decomposition import PCA
# Initially you have to set n_components=None , then check the variance ratio and select top two variables based on %
pca = PCA(n_components= 2)
wine_IV_train = pca.fit_transform(wine_IV_train)
wine_IV_test = pca.transform(wine_IV_test)
explained_variance = pca.explained_variance_ratio_

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 18:54:48 2019

@author: lakshmanteja
"""
%reset -f

# Artificial Neural Network
# Installing Newral Network Libraries from Spyder ipython console
# =============================================================================
# !pip3 install Theano
# !pip3 install tensorflow
# !pip3 install keras
# =============================================================================

# Part 1: Data Pre-processing
# Importing the libraries for data pre-processing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
Y = dataset.iloc[:, 13].values

# Encoding the categorical variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
LabelEncode = LabelEncoder()
X[:,1] = LabelEncode.fit_transform(X[:,1])
X[:,2] = LabelEncode.fit_transform(X[:,2])

onehothandler = OneHotEncoder(categorical_features=[1])
X = onehothandler.fit_transform(X).toarray()

X= X[:,1:]

# Splitting the data into training and test datasets
from sklearn.model_selection import train_test_split
X_train,X_test, Y_train,Y_test = train_test_split(X,Y, test_size = 0.2, random_state=0)

# Feature Scalling 
from sklearn.preprocessing import StandardScaler
SC = StandardScaler()
X_train = SC.fit_transform(X_train)
X_test = SC.transform(X_test)

# Part 2: Building ANN
# importing keras libraries
import keras
from keras.models import Sequential
from keras.layers import Dense

ANN = Sequential()

# Adding input and the first hidden layer
ANN.add(Dense(units=6, kernel_initializer='uniform', activation='relu', input_dim= 11))
# Adding secound hidden layer
ANN.add(Dense(units=6, kernel_initializer='uniform',activation='relu'))
# Adding output layer
ANN.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))
#Adding compiler to ANN
ANN.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
# Fit the ANN to datasets
ANN.fit(X_train,Y_train,batch_size=10, epochs=100)

# Predicting the test datasets using the model
Y_Pred = ANN.predict(X_test)
Y_Pred = (Y_Pred > 0.5)

# Confusion matrixs
from sklearn.metrics import confusion_matrix
CM = confusion_matrix(Y_test,Y_Pred)

## End of the code for ANN
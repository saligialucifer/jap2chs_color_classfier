
# coding: utf-8
# 画数据集点时使用

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from mpl_toolkits.mplot3d import Axes3D
from read import *
from tf_utils import random_mini_batches
import time

# %matplotlib inline


# In[2]:


X_train, Y_train, X_test, Y_test = load_data_set()
Y_train = Y_train.T
Y_test = Y_test.T


# Y_train.shape
# X_train[:,0]


# In[4]:


Y_train.shape


# In[22]:

plt.figure(1)
ax1=plt.axes(projection='3d')
plt.figure(2)
ax2=plt.axes(projection='3d')


for i in range(X_train.shape[1]):
    if Y_train[0,i]==1:
        ax1.scatter3D(X_train[0,i], X_train[1,i], X_train[2,i],c='b');
    else:
        ax1.scatter3D(X_train[0,i], X_train[1,i], X_train[2,i],c='y');

plt.show()



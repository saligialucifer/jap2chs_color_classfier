import math
import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from read import *
X_train, Y_train, X_test, Y_test = load_data_set()

#3,700    700,1    3,76    76,1
X = np.concatenate((X_train,X_test), axis=1)#3,776
Y = np.concatenate((Y_train,Y_test), axis=0)#776,1

n_m = X.shape[1]

mu = np.sum(X,1,keepdims=True)/n_m
X_j = X - mu

sigma = (1/n_m) * np.dot(X_j , X_j.T)

u,s,vt = la.svd(sigma)
ureduce = u[:,:2]
Z = np.dot(ureduce.T,X)

ax = plt.axes()
ax.scatter(Z[0,:],Z[1,:],100,Y)
ax2 = plt.axes(projection='3d')
x = X_train[0,:]
y = X_train[1,:]
z = X_train[2,:]

ax2.scatter3D(x,y,z, c=Y_train,cmap='Greens')
plt.show()

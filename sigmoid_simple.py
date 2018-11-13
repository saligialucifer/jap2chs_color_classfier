import math
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python.framework import ops
from read import *

%matplotlib inline
X_train_orig, Y_train_orig, X_test_orig, Y_test_orig = load_data_set()
ax = plt.axes(projection='3d')
x = X_train_orig[:,1]
y = X_train_orig[:,2]
z = X_train_orig[:,3]
ax.scatter3D(x,y,z, c=Y_train_orig, cmap = 'Grrens')
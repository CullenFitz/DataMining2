# Question 1

import pandas as pd
import numpy as np
import math

# Create our adjacency matrix
A = [[1,1,0,1,1,1,1,1,1,1],
       [0,1,1,1,0,1,0,1,1,0],
       [1,0,1,0,0,1,1,0,1,0],
       [1,0,1,1,1,0,1,0,0,1],
       [1,0,1,1,1,0,1,0,1,1],
       [0,1,0,1,1,1,1,1,1,1],
       [1,0,0,1,0,0,1,1,1,0],
       [0,1,0,1,0,0,1,1,0,0],
       [1,0,1,1,0,0,0,1,1,0],
       [0,1,0,1,1,0,0,0,1,1]]

A = np.array(A)

vector = np.vectorize(float)

n = 10
d = 10
convFlag=0
tol = 0.0001
p0 = [1,1,1,1,1,1,1,1,1,1]
p0 = np.array(p0)
p0 = p0.transpose()
#aa, bb = np.array(A).max(0), np.array(A).argmax(0)
#pmax = aa
while convFlag == 0:
    p = A.transpose() * p0   # Update popularity vector
    p = np.array(p)
    aa, bb = p.max(), p.argmax()
    lam = aa
    p=p/aa   # Scale popularity vector (max should be 1
    diff = p - p0
    diff = np.array(diff)
    err = np.sqrt(diff.transpose() * diff)
    if err.all() < tol:
        convFlag = 1
    else:
        p0 = p
    print(err)
    print(p)

# Eigenvector
pev = p / np.sqrt(np.transpose(p) * p)

# Eigenvalue
ev = np.array(p).max()



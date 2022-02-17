# Question 1

import pandas as pd
import numpy as np

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

n = 10
d = 10
convFlag=0
tol = 0.0001
p0 = [1,1,1,1,1,1,1,1,1,1]
p0 = np.transpose(p)
#aa, bb = np.array(A).max(0), np.array(A).argmax(0)
#pmax = aa
while convFlag == 0:
    p = np.transpose(A) * p0   # Update popularity vector
    aa, bb =
    lam = aa
    p=p/np.array(p).max()   # Scale popularity vector (max should be 1
    if p - p0



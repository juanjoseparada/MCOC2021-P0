# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:41:40 2021

@author: juanp
"""

from time import perf_counter
from numpy import zeros
from scipy.linalg import inv
from numpy.linalg import inv
from numpy import float16, float32, float64
import numpy as np 

N=5

def laplaciana(N, dtype= np.single):
    A=zeros((N,N), dtype=dtype)
    
    for i in range(N):
        for j in range(N):
            if i==j:
                A[i,i]=2
            elif abs(i-j)==1:
                A[i,j]=-1
    return A

print (laplaciana(N))


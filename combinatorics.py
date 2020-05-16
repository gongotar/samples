#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:18:05 2020

@author: gongotar
"""


import operator as op
from functools import reduce

def ncr(n, r):
    if (r < 0):
        return 0
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


k = 40
m = 20
n = 3
N = 2
balls = N*m*n

# modified answer

rj = 0
div = min(int(k/n),N)
for j in range(0,div+1):
    rs = 0  
    for s in range(0,N*m - j+1):

        if (s*n+j*n)<=k:
            rs += (-1)**(s) * ncr(N*m-j,s) * ncr(N*n*m-n*j-n*s, k-n*j-n*s)
    
    rj += ncr(N,j) * m**j * rs

fr = 1-float(rj)/float(ncr(balls,k))
print(fr)

# the answer
rj = 0
div = int(k/n)
for j in range(0,div+1):
    rs = 0  
    for s in range(0,div - j+1):
        rs += (-1)**(s) * ncr(N*m-j,s) * ncr(N*n*m-n*j-n*s, k-n*j-n*s)
    rj += ncr(N,j) * m**j * rs

fr = 1-float(rj)/float(ncr(balls,k))
print(fr)
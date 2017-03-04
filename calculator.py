# -----------------------------------------------------------------------------
# calculator.py
# ----------------------------------------------------------------------------- 

'''
I used cProfile to track the performance of original calculator script.

1015920 function calls (1015799 primitive calls) in 1.888 seconds

This function is significantly slowing down the code.
1000001    0.074    0.000    0.074    0.000 {math.sqrt}

Timer unit: 1e-06 s

Total time: 2.87545 s
File: calculator.py
Function: hypotenuse at line 45

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    45                                           def hypotenuse(x,y):
    46                                               """
    47                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
    48                                               x and y must be two-dimensional arrays of the same shape.
    49                                               """
    50         1       721832 721832.0     25.1      xx = multiply(x,x)
    51         1       758080 758080.0     26.4      yy = multiply(y,y)
    52         1       747363 747363.0     26.0      zz = add(xx, yy)
    53         1       648178 648178.0     22.5      return sqrt(zz)
'''

'''
I changed the for-loop in add function to numpy array adding
I changed the for-loop in multiply function to numpy element-wise multiplication 
I changed the for-loop in sqrt function to numpy square roo function

The performance is improved from 1.8 sec to 0.17 sec.
'''
import numpy as np

def add(x,y):
    """
    Add two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    m,n = x.shape
    z = np.zeros((m,n))
    # for i in range(m):
    #     for j in range(n):
    #         z[i,j] = x[i,j] + y[i,j]
    z = x + y
    return z


def multiply(x,y):
    """
    Multiply two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    m,n = x.shape
    z = np.zeros((m,n))
    # for i in range(m):
    #     for j in range(n):
    #         z[i,j] = x[i,j] * y[i,j]
    np.multiply(x, y)
    return z


def sqrt(x):
    """
    Take the square root of the elements of an arrays using a Python loop.
    """
    # from math import sqrt
    m,n = x.shape
    z = np.zeros((m,n))
    # for i in range(m):
    #     for j in range(n):
    #         z[i,j] = sqrt(x[i,j])
    z = np.sqrt(x)
    return z


def hypotenuse(x,y):
    """
    Return sqrt(x**2 + y**2) for two arrays, a and b.
    x and y must be two-dimensional arrays of the same shape.
    """
    xx = multiply(x,x)
    yy = multiply(y,y)
    zz = add(xx, yy)
    return sqrt(zz)

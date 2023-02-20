# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:38:03 2023

@author: user
numpy library - test
"""


import numpy as np


a = np.arange(20)
a
 
a.shape
a[0]
a[3]
 
a = a.reshape(2,10)
a.shape
a
 
a[0]
a[3]
a[0][3]
 
a = a.reshape(2,5,2)
a.shape
a
 
a[0]
a[0][3]
a[0][3][1]
 
b=np.arange(0,40,2).reshape(4,5)
b
 
list =  [2**x for x in range(10)]
c=np.array(list)
c
 
zero_array = np.zeros(10)
zero_array
 
one_array = np.ones(10)
one_array
 
empty_array = np.empty(100)
empty_array
 
array_11 = np.full((5,5), 11)
array_11
 
diagonal_array = np.eye(5)
diagonal_array
 
random_array = np.random.random(10)
random_array
 
linspace_array = np.linspace(100,200, num=5)
linspace_array


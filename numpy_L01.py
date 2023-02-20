# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:38:03 2023

@author: user
numpy library - test
"""


import numpy as np

#
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

# create an array arr containing odd numbers from 5 to 29
arr = np.arange(5, 30, 2)
arr
#Create a boolArr array containing True/False values. True if number < 10  
boolArr = arr < 10
boolArr
   
newArr = arr[boolArr]
newArr
 
newArr = arr[arr < 20]
newArr 
#the item value is divisible by 3 
newArr = arr[arr%3==0]
newArr
#the value is greater than 10 and less than 20   
newArr = arr[(arr > 5) & (arr < 20)]
newArr
 
# array with numbers from 0 to 23. We reshape arr to 4x6
arr = np.arange(24).reshape(4,6)
arr
#we display column rows and values 
arr[1]
 
arr[1][2]
arr[1, 2]
 
arr[1, 2:4]
arr[1, 2:5]
 
arr[1, :]
 
 
arr[: , 2]
arr[0:3 , 2]
 
arr[:3 , 2]
 
arr[:3 , 2:4]
 
arr[: , -1]
 
arr[:, :-1]
 
#we mix the values 
np.random.shuffle(arr)
arr
 


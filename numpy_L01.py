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

# create and reshape an array 
X = np.arange(1,26).reshape(5,5)
X
 
Ones = np.ones(X.shape)
Ones
# multiply matrices
np.dot(X, Ones)
diag = np.zeros(X.shape)
np.fill_diagonal(diag, 1)
diag
np.dot(X, diag)
 
# where 
np.where(X > 10, 1, 0)
 
np.where(X % 2 == 0, 1, 0)
 
np.where(X % 2 == 0, X, 0)
 
np.where(X % 2 == 0, X, X + 1)
 
np.where(X > 10, 2 * X, 0)
 
X_bis = np.where(X > 10, 2*X, 0)
X_bis

# Counts the number of non-zero values in the array
np.count_nonzero(X_bis)
 
x = np.array([[10,20,30], [40,50,60]])
y = np.array([[100], [200]])
print(np.append(x, y, axis=1))
 
x = np.array([[10,20,30], [40,50,60]])
y = np.array([[100, 200, 300]])
print(np.append(x, y, axis=0))
 
#we connect arrays 
x = np.array([[10,20,30], [40,50,60]])
print(np.append(x, x, axis=0))

# statistic in numpy
data = np.array([[11, 4, 8], [3, 2, 1]])
data
 
np.median(data)
 
np.median(data, axis=0)
 
np.median(data, axis=1)
 
np.mean(data)
np.mean(data, axis=0)
np.mean(data, axis=1)
np.mean(data, dtype=np.float32)
np.mean(data, dtype=np.float64)
 
np.average(data)
np.average(data, axis=0)
np.average(data, axis=1)
 
np.average(data, weights=[0,1,2], axis=1)
np.average(data, weights=[2,3,4], axis=1)

np.var(data)
np.var(data, axis=0)
np.var(data, axis=1)

np.std(data)
np.std(data, axis=0)
np.std(data, axis=1)


np.mean(data, dtype=np.float32)
np.mean(data, dtype=np.float64)

# random variables
rand_a = np.random.rand()
print(rand_a)
 
rand_a = np.random.rand(2,5)
print(rand_a)
 
rand_b = np.random.rand(1,5)
print(rand_b)
 
rand_b = rand_b*100 
print(rand_b)
#adding rows
rand_c = np.vstack((rand_a, rand_b))
print(rand_c)
 
rand_b = np.random.rand(2,1)
print(rand_b)
#adding columns 
rand_c = np.hstack((rand_a, rand_b))
print(rand_c)
 
 
X = rand_c[:,2]
print(X)
 
a=3
b=8
 
y = a * X + b
print(y)
 
 
X = np.random.randint(low=0, high=10, size = 10) 
print(X)
X = X *10 
print(X)
 
np.random.choice(10, size=3, replace=False)
 
np.random.choice(10, size=3, replace=True)
 
idx = np.random.choice(X.shape[0], size=3, replace=False)
print(X)
print(idx)
print(X[idx])



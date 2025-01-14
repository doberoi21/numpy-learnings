import numpy as np

list1=[1,2,3,4]
# print(list1)

list2=[12,"abc",list1,True]
# print(list2)

# NUMPY - Numeric Python 
# Data type of numpy - ndarray = n - dimensional array

np1 = np.array([0,1,2,3,4,5,6,7,8])
print(np1)
# len of array - shape
print(np1.shape)
#  make array of certain range 
np2 = np.arange(10)
print(np2)
# array with range and steps 
np3 = np.arange(0,10,2)
print(np3)
# Zeroes
np4 = np.zeros(10)
print(np4)
# Multi dimensional Zeros 
np5= np.zeros((2,10))
print(np5)
# full()
np6 = np.full(10,6)
print(np6)
# Multi - Dimensional 
np7 = np.full((2,10),7)
print(np7)

# Convert Python list to NUmpy
my_list = [1,2,3,5]
np8 = np.array(my_list)
print(np8)
import numpy as np

np1 = np.array([1,2,3,4,5,6,7,8,9])

# Slicing
# return 2,3,4,5
print(np1[1:5]) 

# Something from indx to end
print(np1[1:]) # 2-9

# Return negative slice 
print(np1[-3:-1]) # 7,8

# Steps 
print(np1[1:5]) # 2,3,4
print(np1[1:5:2]) # 2,4

# 
print(np1[::3])

# Slice 2-D array 
np2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# pull oout isngle item
print(np2[1][2]) # 8 
print(np2[1,2]) # 8 

# Slice 2D array
print(np2[0:1,1:3])

# Slice from both rows 
print(np2[0:2,1:3])

  



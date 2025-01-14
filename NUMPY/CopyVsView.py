import numpy as np

np1 = np.array([1,2,3,4,5])

'''
np2 = np1.view()

print(f'Original np1: {np1}')
print(f'Original np2: {np2}')

np1[1]=10
print(f'Chnage np1: {np1}')
print(f'CHANGED np2: {np2}')
# Chnge in the original VIEW will also get chnge VICE VERSA
''' 

# COPY 
np2 = np1.copy()

print(f'Original np1: {np1}')
print(f'Original np2: {np2}')

np1[1]=10
print(f'Chnage np1: {np1}')
print(f'ORIGINAL np2: {np2}')
# Chnge in the original COPY will not get chnge 
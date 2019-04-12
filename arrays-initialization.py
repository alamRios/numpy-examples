'''
    using python 3.7
'''
import numpy as np

print('>> 1D array')
pyarray_1 = [15,5,3,10,0,6]
nparray = np.array(pyarray_1)
print(nparray)
print(nparray.shape)
print()

print('>> 2D array')
pyarray_2 = [6,0,10,3,5,15]
nparray = np.array([pyarray_1, pyarray_2])
print(nparray)
print(nparray.shape)
print()

print('>> Reshape 1D array to 2D array')
pyarray_1 = [15,5,3,10,0,6]
nparray = np.array(pyarray_1)
print(nparray.reshape(2,3))
print(nparray.shape)
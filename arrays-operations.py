import numpy as np

pyarray = [15,5,3,10,0,6]
x = np.array(pyarray)
y = np.array([10,10,10,10,10,10])

print('>> x:',x)
print('>> y:',y)
print()
print('>> x[x>4]:',x[x>4])
print('>> x[~(x>4)]:',x[~(x>4)])
print('>> x*y:',x*y)
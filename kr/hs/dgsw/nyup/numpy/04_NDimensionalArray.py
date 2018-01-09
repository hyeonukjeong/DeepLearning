import numpy as np

A = np.array([[1, 2], [3, 4]])

print(A)
'''
[[1 2]
 [3 4]]
'''
print(A.shape)
# (2, 2)
print(A.dtype)
# int64

B = np.array([[3, 0], [0, 6]])

print(A + B)
'''
[[ 4  2]
 [ 3 10]]
'''
print(A * B)
'''
[[ 3  0]
 [ 0 24]]
'''
print(A * 10)
'''
[[10 20]
 [30 40]]
'''
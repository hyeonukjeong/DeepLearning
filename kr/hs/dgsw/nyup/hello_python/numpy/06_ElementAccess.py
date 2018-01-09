import numpy as np

X = np.array([[51, 55], [14, 19], [0, 4]])

print(X)
'''
[[51 55]
 [14 19]
 [ 0  4]]
'''
print(X[0])
# [51 55]
print(X[0][1])
# 55

for row in X:
    print(row)
'''
[51 55]
[14 19]
[0 4]
'''

X = X.flatten()

print(X)
# [51 55 14 19  0  4]
print(X[np.array([0, 2, 4])])
# [51 14  0]

print(X > 15)
# [ True  True False  True False False]
print(X[X > 15])
# [51 55 19]

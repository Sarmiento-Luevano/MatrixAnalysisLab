import numpy as np

A = np.array([[1, 2, 2],
              [2, 3, 4],
              [3, 4, 6]])


I = np.identity(3)

c_1 = np.array([0,2,3])
e_1 = np.array([1,0,0])

outer = np.outer(c_1, e_1)

print(outer)

import Gauss_elimination as gauss 
import numpy as np

A = np.array([[1, 1, 1, 1],
              [1, 1, 3, 3],
              [1, 1, 2, 3],
              [1, 3, 3, 3]])

b = np.array([1, 3, 3, 4])

gaussian_solve = gauss.GaussianElimination(A,b)
solution = gaussian_solve.solve()
print("Solution to Ax = b is x = ", solution)
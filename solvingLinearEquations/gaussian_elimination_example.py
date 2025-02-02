import Gauss_elimination as gauss 
import numpy as np

A = np.array([[4, 0, 0, 2],
              [0, 4, 3, 2],
              [0, 3, 4, 2],
              [6, 3, 3, 4]])

b = np.array([12, 25, 26, 37])

gaussian_solve = gauss.GaussianElimination(A,b)
solution = gaussian_solve.solve()
print("Solution to Ax = b is x = ", solution)
import numpy as np
class GaussianElimination:
    def __init__(self, A, b):
        self.A = A.astype(float)
        self.b = b.astype(float)

    def move_pivot(self, k, i=0):
        # For wrong cases
        if k + i >= self.A.shape[0]:
            print("No non-zero pivot found in column", k)
            return
        
        if self.A[k, k] == 0:
            # Swapping in matrix A
            self.A[[k, k + (i + 1)]] = self.A[[k + (i + 1), k]]
            # Swapping in vector b
            self.b[k], self.b[k + (i + 1)] = self.b[k + (i + 1)], self.b[k]
            return self.move_pivot(k, i + 1)

    def eliminate_below_pivot(self, k):
        n = self.A.shape[0]  # Number of rows in A
        
        for j in range(k + 1, n):
            if self.A[j, k] != 0:
                factor = self.A[j, k] / self.A[k, k]
                self.A[j, :] -= factor * self.A[k, :]  # Update row j of A
                self.b[j] -= factor * self.b[k]  # Update the corresponding entry in b

    def back_substitution(self):
        n = len(self.b) - 1
        x = np.zeros_like(self.b, dtype=float)

        x[n] = self.b[n] / self.A[n, n]

        for i in range(n - 1, -1, -1):
            x[i] = self.b[i]
            for k in range(i + 1, n + 1):
                x[i] -= self.A[i, k] * x[k]
            x[i] /= self.A[i, i]

        return x

    def solve(self):
        n = self.A.shape[0]
        for k in range(n):  # Going through each row and their corresponding value in b
            if (self.A[k, k] == 0):
                self.move_pivot(k)  # Call with both A and b
            self.eliminate_below_pivot(k)

        x = self.back_substitution()
        return x

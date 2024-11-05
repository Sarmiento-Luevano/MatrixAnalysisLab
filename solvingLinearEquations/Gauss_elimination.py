import numpy as np


def move_pivot(A, b, k, i=0):
    # For wrong cases
    if k + i >= A.shape[0]:
        print("No non-zero pivot found in column", k)
        return A, b  
    
    if A[k, k] == 0:
        # Swappin in matrix A
        A[[k, k + (i + 1)]] = A[[k + (i + 1), k]]
        # Swapping in vector b
        b[k], b[k + (i + 1)] = b[k + (i + 1)], b[k]
        return move_pivot(A, b, k, i + 1)
    else:
        return A, b  


def back_substitution(T,c):
    n = len(c) - 1
    x = np.zeros_like(c, dtype=float)

    x[n] = c[n] / T[n,n]

    for i in range(n-2,-1,-1):
        x[i] = c[i]

        for k in range(i+1, n+1):
            x[i] = x[i] - T[i,k] * x[k]
        
        x[i] = x[i] / T[i,i]

    return x

def eliminate_below_pivot(A, b, k):
    n = A.shape[0]  

    for j in range(k + 1, n):
        if A[j, k] != 0:
            factor = A[j, k] / A[k, k]
            A[j, :] -= factor * A[k, :]  # Update row j of A
            b[j] -= factor * b[k]  # Update the corresponding entry in b

    return A, b  

A = np.array([[1,1,1,1],
              [1,1,3,3],
              [1,1,2,3],
              [1,3,3,3]], dtype=float)

b = np.array([1,3,3,4], dtype=float)

def solve_Gauss(A, b):
    n = A.shape[0]
    A, b = A.copy(), b.copy()  
    for k in range(n):     # Going through each row and their corresponding value in b
        if (A[k, k] == 0):
            A, b = move_pivot(A, b, k)  # Call with both A and b
        A, b = eliminate_below_pivot(A, b, k)

    x = back_substitution(A, b)
    print("The solution vector to Ax=b is x =", x)
    return x

x = solve_Gauss(A,b)

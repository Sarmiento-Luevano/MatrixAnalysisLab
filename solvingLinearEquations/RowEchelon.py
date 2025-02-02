import Gauss_elimination as gauss 
import numpy as np

A = np.array([[4, 0, 0, 2],
              [0, 4, 3, 4],
              [0, 3, 4, 3],
              [0, 3, 3, 4]])

def check_nonzeros_below(A, pivot, k):
    v = A[pivot:, k]

    if (np.size(v) == 0):
        return False

    if (np.max(v) == 0):
        return False
        
    return True

def findLargestPivot(A,k,pivot):
    # Find the largest pivot in the matrix A on column k starting from last pivot
    v = A[pivot:, k]
    if (np.size(v) == 0):
        return -1

    largest = np.argmax(np.abs(v))

    # If the entire c
    if (v[largest] == 0):
        return -1      # Out of bounds

    return largest + pivot   # In the moment I shorten the vector, I need to make up for it by adding the index 'lost'

def swap_rows(A, row1, row2):
    if row1 == row2:
        return
    
    A[[row1, row2]] = A[[row2, row1]]


def eliminate_below_pivot(A, k, pivot_i):
    n = A.shape[0] 

    for i in range(pivot_i+1, n):
        # print(f"A[{i}] = {A[pivot_i,k]}*{A[i]} - {A[i,k]}*{A[pivot_i]}")  # Debugging purposes
        A[i] = A[pivot_i,k]*A[i] - A[i,k]*A[pivot_i]


def Row_Echelon_Sorted(A):
    m = A.shape[1]
    pivot = 0
    for j in range(m):
        i_argmax = findLargestPivot(A,j,pivot)
        if (i_argmax == -1):
            continue
        swap_rows(A, i_argmax, pivot)
        eliminate_below_pivot(A,j, pivot)
        pivot += 1
    return A

def Row_Echelon(A):
    m = A.shape[1]
    pivot = 0
    for j in range(m):
        pivot_boolean = check_nonzeros_below(A, pivot, j)
        if pivot_boolean == False:
            continue
        eliminate_below_pivot(A,j,pivot)
        pivot += 1
        print(A)
    return A

# A = Row_Echelon(A)
# print(A)
A = np.array([[4, 0, 0, 2],
              [0, 4, 3, 2],
              [0, 3, 4, 2],
              [6, 3, 3, 4]])

p = np.array([1,2,3,4])


for k in range(1,20):
    print("k = ", k)
    A = np.linalg.matrix_power(A,k)
    print(np.dot(p, A))
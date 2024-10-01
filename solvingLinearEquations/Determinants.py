import numpy as np

def det2(C):
    return C[0,0]*C[1,1] - C[0,1]*C[1,0]

def det3(A):
    n = A.shape[0]
    i = 0

    sum = 0
    for j in np.arange(n):
        B = np.delete(A, i, axis = 0)
        B = np.delete(B, j, axis = 1)
        sum = sum + ((-1)**j)*A[i,j]*det2(B)
    
    return sum 
    
def inputMatrix():
    print("Write down the constants of each of the linear equations...")
    A = np.zeros((3,3))
    b = np.zeros(3)
    for i in np.arange(3):
        print(f"{i+1}nd equation...")
        for j in np.arange(3):
            A[i,j] = (input(f"Enter the element for x_{j+1}: "))
        b[i] = input(f"Enter the {i+1}nd constant: ")

    for i in range(3):
        print(f"{i+1}nd equation")
        for j in range(3):
            print(f"{A[i,j]}x_{j+1} +", end=' ')
        print(f" = {b[i]}")

    return A, b

def crammerMatrix_kth(A,b,k):
    n = A.shape[0]
    B = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if (j == k):
                B[i,j] = b[i]
            else:
                B[i,j] = A[i,j]
    return B

def iterateCrammer(n,A,b):
    crammerMatrices = []
    for k in range(n):
        subMatrix = crammerMatrix_kth(A,b,k)
        crammerMatrices.append(subMatrix)
    return crammerMatrices

def CrammerDeterminants_list(A,b):
    n = A.shape[0]
    matrices = iterateCrammer(n,A,b)
    determinants = []
    for matrix in matrices:
        determinants.append(float(det3(matrix)))
    return determinants
    
def CrammerSolutions(A,b):
    detA = det3(A)
    
    if np.isclose(detA, 0):
        return np.array([0])

    lst = CrammerDeterminants_list(A,b)
    solutions = np.array(lst)
    solutions = solutions / detA
    return solutions    
    

def main():
    A, b = inputMatrix()

    solutions = CrammerSolutions(A,b)

    if (solutions[0] == 0):
        print("The system has no solutions")
        return
    print("The solutions are...")
    for i in range(len(solutions)):
        print(f"x_{i+1} = ", solutions[i])




if __name__ == '__main__':
    main()


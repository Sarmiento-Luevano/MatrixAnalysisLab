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
    for i in np.arange(3):
        print(f"{i+1}nd equation...")
        for j in np.arange(3):
            A[i,j] = (input(f"Enter the element for x_{j+1}: "))

    for i in range(3):
        print(f"{i+1}nd equation")
        for j in range(3):
            print(f"{A[i,j]}x_{j+1}", end=' ')
        print("")

    return A

def main():
    A = inputMatrix()
    

if __name__ == '__main__':
    main()


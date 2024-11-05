import numpy as np

x = np.array([0,0,1])
x_tilde = x[1:]
n = len(x)
alpha = 1 / (1 - x[0])

def R_prime(x, alpha):
    n = len(x)
    I = np.identity(n=n)
    outer_x = np.outer(x,x)
    return I - alpha*outer_x

def generate_rotator(x):
    x_tilde = x[1:]

    if np.abs(x[0]) == 1:
        raise ValueError("|x[0]| should be different than 1")
        return

    n = len(x)
    alpha = 1 / (1 - x[0])
    R = np.zeros(shape=(n,n))

    R_p = R_prime(x_tilde, alpha)

    for i in range(n):
        for j in range(n):
            if i==0 and j==0:
                R[i,j] = x[0]
                continue
            if i==0:
                R[i,j] = x_tilde[j-1]
                continue
            if j==0:
                R[i,j] = x_tilde[i-1]
                continue
            R[i,j] = R_p[i-1,j-1]

    return R

R = generate_rotator(x)
print(R)
    




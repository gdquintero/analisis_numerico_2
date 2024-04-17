import numpy as np

def backward_sustitution(A,b,n,x):
    x[n-1] = b[n-1] / A[n-1,n-1]

    for k in range(n-2,-1,-1):
        for i in range(k+1,n):
            x[k] += A[k,i] * x[i]
        x[k] = (b[k] - x[k]) / A[k,k]

    return x

A = np.array([
    [1,2,-1,2],
    [0,2,3,1],
    [0,0,-2,1],
    [0,0,0,2]])

b = np.array([1,1,1,1])


# A = np.array([
#     [2,1,-3],
#     [0,5,4],
#     [0,0,3]
#     ])

# b = np.array([4,2,6])
n = len(b)
x = np.zeros(n)

backward_sustitution(A,b,n,x)

print(x)
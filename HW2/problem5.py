import sys
import numpy as np
from scipy.linalg import solve_triangular
import copy
import time

def create_random_L(n):
    A = 0.001*np.tril(np.random.rand(n, n))
    np.fill_diagonal(A, 1)
    return A

def create_random_B(n):
    B = np.random.rand(n)
    return B

def forward1(L,b,n):
    try:
        if L.shape[0] != L.shape[1]:
            raise ValueError("L is not a square matrix")
        if L.shape[0] != b.shape[0]:
            raise ValueError("L is not compatible with b")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    # L[row,column]
    x=np.zeros(n)
    for i in range(n):
        for j in range(n):
            if j==i:
                x[i]+=b[i]/L[i,j]
            elif j<i:
                x[i]-=x[j]*L[i,j]/L[j,j]
    return x

def forward2(L,b,n):
    try:
        if L.shape[0] != L.shape[1]:
            raise ValueError("L is not a square matrix")
        if L.shape[0] != b.shape[0]:
            raise ValueError("L is not compatible with b")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    # L[row,column]
    x=np.zeros(n)
    x[0] = b[0]/L[0,0]
    for i in range(1,n):
        x[i] = (b[i]-np.sum(L[i,:i]*x[:i]))/L[i,i]
    return x

def forward3(L, b, n):
    try:
        if L.shape[0] != L.shape[1]:
            raise ValueError("L is not a square matrix")
        if L.shape[0] != b.shape[0]:
            raise ValueError("L is not compatible with b")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    B = b.copy()
    for j in range(n - 1):
        B[j] = B[j] / L[j, j]
        B[j+1:n] = B[j+1:n] - L[j+1:n, j] * B[j]

    # the bn = bn/Lnn case
    B[n-1] = B[n-1] / L[n-1, n-1]
    return B

def built_in(L, b, n=None):
    return solve_triangular(L, b, lower=True, unit_diagonal=False, overwrite_b=False)

def time_solver(solver, L, b, n=None):
    start = time.perf_counter()
    x = solver(L, b, n)
    end = time.perf_counter()
    T = (end - start)
    print(f"{solver.__name__}: {T:.6f} s")
    return x, T

if __name__=="__main__":
    n=5000
    L=create_random_L(n)
    b=create_random_B(n)
    x4, t4 = time_solver(built_in, L, b, n)
    x1, t1 = time_solver(forward1, L, b, n)
    x2, t2 = time_solver(forward2, L, b, n)
    x3, t3 = time_solver(forward3, L, b, n)
    print(x1)
    print(x2)
    print(x3)
    print(x4)

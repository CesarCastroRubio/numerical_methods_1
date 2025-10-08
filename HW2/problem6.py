import sys
import numpy as np
import time
sys.setrecursionlimit(10000)

def create_random_A_SPD(n):
	a = np.random.rand(n, n)
	a = a.T @ a + np.eye(n)
	return a

def check_spd(a):
	mask = np.where(np.diag(a) <= 0)
	try:
		if a.shape[0] != a.shape[1]:
			raise ValueError("L is not a square matrix")
		if len(mask[0])-1 > 0:
			raise ValueError("Matrix diagonals contain negative values or zeros")
	except ValueError as e:
		print(f"Error: {e}")
		sys.exit(1)
	
	return a.shape[0]


def my_chol(a):
	N = check_spd(a)
	R = np.zeros((N, N))
	A_star = a.copy().astype(float)

	# loop over rows
	for j in range(N):
		# get beta
		alpha = A_star[j, j]
		beta = np.sqrt(alpha)
		R[j, j] = beta

		# get omega as row j and entries column+1 to the end rescaled by beta
		v = A_star[j, j+1:]
		omega = v / beta
		R[j, j+1:] = omega

		# Get new submatrix A* - wTw
		A_star[j+1:, j+1:] -= np.outer(omega, omega)

	return R

def built_in_chol(a):
	return np.linalg.cholesky(a).T

def time_solver(solver, A):
	start = time.perf_counter()
	x = solver(A)
	end = time.perf_counter()
	T = (end - start)
	print(f"{solver.__name__}: {T:.6f} s")
	return x, T

if __name__=="__main__":
	n=3
	A=create_random_A_SPD(n)
	R = my_chol(A)
	R_built_in = built_in_chol(A)

	# same thing
	print(f"A: \n{A}")
	print(f"R: \n{R}")
	print(f"R_built_in: \n{R_built_in}")
	
	for n in [500,1000,5000]:
		for solver in [my_chol,built_in_chol]:
			A=create_random_A_SPD(n)
			time_solver(solver, A)
		

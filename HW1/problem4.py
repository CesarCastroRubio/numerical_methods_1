import numpy as np
import sys


print("Explain values")
print(np.spacing(1))
print(np.spacing(np.single(1)))
print(np.spacing(2**40))
print(np.spacing(np.single(2**40)))

print("Explain Behavior")
a=0.50
b=0.7-0.2
print(a==b)
print("%20.18f"% a)
print("%20.18f"% b)


print("Conditions")
A=1e16
B=1e-1
C=1
print(A,B,C)
print(A+B==A)
print((A+B)+C==A+(B+C))

print(sys.float_info.min/2)

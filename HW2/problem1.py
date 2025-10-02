import numpy as np
import matplotlib.pyplot as plt

I_full = 2.434370698241593
a, b = 0, 4

def f(x):
    return np.exp(x) / (1 + 4 * x**2)

def trapezoidal(N, A, B):
    h = (B - A) / N
    total = 0
    for j in range(1, N):
        total += f(A + j * h)
    return h / 2 * (f(A) + 2 * total + f(B))

# Data collection
N_values = [2**k for k in range(16)]
h_values = []
errors = []
errors2 = []

for N in N_values:
    h = (b - a) / N
    I = trapezoidal(N, a, b)
    err = abs(I - I_full)
    h_values.append(h)
    errors.append(err)

h_values = np.array(h_values)
errors = np.array(errors)

# Convergence order p
p_values = []
h_mid = []
for i in range(len(N_values) - 1):
    eN = errors[i]
    e2N = errors[i + 1]
    p = np.log2(eN / e2N)
    p_values.append(p)
    h_mid.append(h_values[i])  # align p with h at N

p_values_1 = np.array(p_values)
h_mid = np.array(h_mid)

for N in N_values:
    Ih1 = trapezoidal(N, a, b)
    Ih2 = trapezoidal(2*N, a, b)
    err = abs(Ih1 - Ih2)
    errors2.append(err)

p_values_2 = []
for i in range(len(N_values) - 1):
    eN = errors2[i]
    e2N = errors2[i + 1]
    exp_p = np.abs((eN / e2N))
    p_values_2.append(exp_p)

p_values_2 = np.array(p_values_2)
# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.4, 3.2), dpi=300)

# Left plot: error vs h (log-log)
ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.plot(h_values, errors, marker="o", linestyle="-", label="Error")
ax1.set_xlabel(r"$h$")
ax1.set_ylabel("Absolute error")
ax1.legend()

# Right plot: p vs h
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.plot(h_mid, p_values_1, marker="s", linestyle="-", label="p")
ax2.plot(h_mid, p_values_2, marker=".", linestyle="-", label="2^p")
ax2.set_xlabel(r"$h$")
ax2.set_ylabel(r"Output of Methods")
ax2.legend()

fig.tight_layout()
plt.savefig("problem1.pdf")

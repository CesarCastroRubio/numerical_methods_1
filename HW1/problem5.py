import numpy as np
import matplotlib.pyplot as plt

ff=np.double(3.101766393836051)
x0=np.pi/4

def f(x):
    y=np.exp(x)
    y/=(np.cos(x)**3+np.sin(x)**3)
    return y

def finite_diff(x0,h):
    return (f(x0+h)-f(x0))/h

def center_diff(x0,h):
    return (f(x0+h)-f(x0-h))/h/2

def complex_step_diff(x0,h):
    return np.imag(f(x0+1j*h)/h)

finite_difference=[]
center_difference=[]
complex_step_differentiation=[]
h0=[]

for i in range(1,16+1):
    h0.append(10**(-i))
    finite_difference.append(finite_diff(x0,h0[-1])-ff)
    center_difference.append(center_diff(x0,h0[-1])-ff)
    complex_step_differentiation.append(complex_step_diff(x0,h0[-1])-ff)


import matplotlib.pyplot as plt

_ax = None

def plt_create(figsize=(4.2, 3.2), dpi=300):
    global _ax
    plt.rcParams.update({
        "figure.dpi": dpi,
        "savefig.dpi": dpi,
        "font.size": 10,
        "axes.labelsize": 11,
        "axes.titlesize": 12,
        "axes.linewidth": 0.9,
        "lines.linewidth": 1.8,
        "lines.markersize": 5,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.minor.visible": True,
        "ytick.minor.visible": True,
        "legend.frameon": False,
    })
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"perturbation $h$")
    ax.set_ylabel("absolute error")
    ax.grid(True, which="major", linestyle="--", alpha=0.5)
    ax.grid(True, which="minor", linestyle=":", alpha=0.3)
    _ax = ax
    return ax

def plot(x, y, label=None, color=None, marker=".", linestyle="-", linewidth=None):
    _ax.plot(x, y, label=label, color=color, marker=marker, linestyle=linestyle, linewidth=linewidth)


def finalize(show_legend=True, loc="best", legend_fontsize=7):
    if show_legend:
        _ax.legend(loc=loc, fontsize=legend_fontsize)
    _ax.figure.tight_layout()

plt.create = plt_create

plt.create()
plot(h0, np.ones(16)*np.spacing(np.double(ff)), label="$exact\cdot\epsilon_{mach}$")
plot(h0, np.abs(finite_difference), label="Finite difference")
plot(h0, np.abs(center_difference), label="Center difference")
plot(h0, np.abs(complex_step_differentiation), label="Complex step")
finalize()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def f(x,n):
    y=x**n
    N_fac=1.0
    for i in range(1,n+1):
        N_fac *= i

    return y/N_fac

exact=np.exp(-5.5)
eps=np.spacing(1)
exp_1=[1]
exp_2=[1]
exp_3=[1]
n=[1]
x1=-1*5.5
x2=5.5
x3=0.5
for i in range(1,30):
    n.append(i+1)
    exp_1.append(exp_1[-1]+f(x1,i))
    exp_2.append(exp_2[-1]+f(x2,i))
    exp_3.append(exp_3[-1]+f(x3,i))

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
    #ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"n")
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
plot(n,np.abs(exp_1-exact))
plot(n,np.abs(1/np.array(exp_2) - exact))
plot(n,np.abs((1/np.array(exp_3))**11 - exact))
plot(n,np.ones(30)*exact*eps)
finalize()
plt.show()

import numpy as np
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
    #ax.set_yscale("log")
    ax.set_xlabel(r"$x$")
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
x=np.linspace(1.920,2.080, num=160)
y=x**9 - 18*x**8 + 144*x**7 - 672*x**6 + 2016*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x - 512

plot(x, (x-2)**9, label="$(x-2)^9$")
plot(x, y, label="Coefficient Representation")
finalize()
plt.show()

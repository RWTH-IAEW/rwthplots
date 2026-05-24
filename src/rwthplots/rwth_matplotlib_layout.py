import matplotlib as mpl
from cycler import cycler

cm2in = 1 / 2.54
fig_side_cm = 12
figsize = (fig_side_cm * cm2in,) * 2
major = 5.0
minor = 3.0

rwth_cycle = [
    '#00549f',  # RWTH blue 100
    '#407fb7',  # RWTH blue 75
    '#8ebae5',  # RWTH blue 50
    '#c7ddf2',  # RWTH blue 25
    '#e8f1fa',  # RWTH blue 10
]


def apply_pptx_style():
    """Apply the RWTH PowerPoint rcParams to the current matplotlib session.

    Calling this function is equivalent to plt.style.use('rwthplots.styles.rwth-pptx')
    but is expressed programmatically.  Import of this module alone has no side effects.
    """
    mpl.rcParams.update({
        "text.usetex": True,
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial"],
        "font.size": 16,
        "text.color": "#404040",
        "legend.fontsize": 16,
        "axes.titlesize": 20,
        "axes.titleweight": "bold",
        "axes.prop_cycle": cycler(color=rwth_cycle),
        "axes.grid": True,
        "axes.grid.axis": "both",
        "axes.grid.which": "both",
        "grid.linestyle": "--",
        "grid.alpha": 0.5,
        "xtick.labelsize": 16,
        "ytick.labelsize": 16,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.major.size": major,
        "xtick.minor.size": minor,
        "ytick.major.size": major,
        "ytick.minor.size": minor,
        "figure.figsize": figsize,
        "figure.dpi": 1500,
        "figure.facecolor": "none",
        "axes.facecolor": "white",
        "savefig.transparent": False,
    })

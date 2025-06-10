import matplotlib as mpl
from cycler import cycler

# --- 1.  GLOBAL STYLE --------------------------------------------------------
cm2in   = 1/2.54                               # centimetres → inches
side = 12 * cm2in                              # 15 cm = 5.905 in

# ------------------------------------------------------------------
# 0.  Figure geometry for PowerPoint
cm2in          = 1/2.54                # cm → inch
fig_side_cm = 12                    # desired side length
figsize     = (fig_side_cm*cm2in,)*2   # (width, height) in inches
major = 5.0
minor = 3.0

# ------------------------------------------------------------------
# 1.  Corporate colour cycle  (your hand-picked RWTH set)
rwth_cycle = ['#00549f',            # RWTH blue
              '#407fb7',            # RWTH blue 75
              '#8ebae5',            # RWTH blue 50
              '#c7ddf2',            # RWTH blue 25
              '#e8f1fa']            # RWTH blue 10

mpl.rcParams.update({
    # fonts
    "text.usetex": True,
    "font.family":      "sans-serif",
    "font.sans-serif":  ["Arial"],          # tell Matplotlib to pick Arial
    "font.size":        16,                 # default text size (red, see below)
    "text.color":       "#404040",          # grey body text
    "legend.fontsize":  16,
    # axes & title
    "axes.titlesize":   20,
    "axes.titleweight": "bold",
    "axes.prop_cycle"  : cycler(color=rwth_cycle),   # <--- colour cycle
    # grid
    "axes.grid":        True,
    "axes.grid.axis": "both",
    "axes.grid.which": "both",
    "grid.linestyle":   "--",
    "grid.alpha":       0.5,
    # ticks
    "xtick.labelsize"  : 16,
    "ytick.labelsize"  : 16,
    "xtick.direction"  : "out",
    "ytick.direction"  : "out",
    "xtick.major.size" : major,
    "xtick.minor.size" : minor,
    "ytick.major.size" : major,
    "ytick.minor.size" : minor,
    # backgrounds
    "figure.figsize": (side, side),
    "figure.dpi": 1500,
    "figure.facecolor": "none",             # transparent canvas
    "axes.facecolor":   "white",            # white plotting area
    # saving
    "savefig.transparent": False            # keep axes background white
})
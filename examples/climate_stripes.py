"""
Climate stripes with RWTH colours
==================================
Recreates Ed Hawkins' 'warming stripes' visualisation using RWTH blue and red
with varying opacity: cold years → RWTH blue (#00549F), warm years → RWTH red
(#CC071E), opacity proportional to the magnitude of the anomaly.

Original concept: Ed Hawkins (University of Reading), showyourstripes.info
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import rwthplots
from rwthplots import save_figure

# ---------------------------------------------------------------------------
# Synthetic data — 130 years of temperature anomaly (resembles HadCRUT trend)
# ---------------------------------------------------------------------------
rng = np.random.default_rng(0)
years = np.arange(1890, 2024)
n = len(years)
trend = np.linspace(-0.4, 0.8, n)
noise = rng.normal(0, 0.15, n)
anomaly = trend + noise  # °C relative to 1961-1990 baseline

# RWTH colours
BLUE = "#00549F"
RED  = "#CC071E"

# Scale opacity by the global maximum absolute anomaly so extremes hit alpha=1
max_abs = np.max(np.abs(anomaly))

def stripe_color(val):
    alpha = min(abs(val) / max_abs, 1.0)
    return (BLUE if val < 0 else RED, alpha)

# ---------------------------------------------------------------------------
# Figure — classic stripe layout (no axes, just colour bars)
# ---------------------------------------------------------------------------
with rwthplots.context("rwth-word"):
    fig, ax = plt.subplots(figsize=(12, 3))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    for year, val in zip(years, anomaly):
        color, alpha = stripe_color(val)
        ax.axvspan(year - 0.5, year + 0.5, color=color, alpha=alpha, linewidth=0)

    ax.set_xlim(years[0] - 0.5, years[-1] + 0.5)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.01, 0.04, str(years[0]),  transform=ax.transAxes,
            fontsize=8, color="#555555", va="bottom")
    ax.text(0.99, 0.04, str(years[-1]), transform=ax.transAxes,
            fontsize=8, color="#555555", va="bottom", ha="right")
    ax.set_title("Global temperature anomaly (synthetic)",
                 fontsize=9, pad=6)

    cold_patch = mpatches.Patch(color=BLUE, label="Below baseline")
    warm_patch = mpatches.Patch(color=RED,  label="Above baseline")
    ax.legend(handles=[cold_patch, warm_patch], loc="upper left",
              fontsize=7, framealpha=0.7, handlelength=1.2)

    import os
    os.makedirs("figures", exist_ok=True)
    save_figure(fig, "figures/climate_stripes", formats=["png", "pdf"])
    plt.close(fig)

print("Saved figures/climate_stripes.{png,pdf}")

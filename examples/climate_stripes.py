"""
Climate stripes with RWTH colours
==================================
Recreates Ed Hawkins' 'warming stripes' visualisation using the RWTH
blue-to-red divergent colourmap.  A synthetic temperature anomaly series
is used so the example runs without an external data file.

Original concept: Ed Hawkins (University of Reading), showyourstripes.info
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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

# Normalise to [0, 1] for colourmap lookup
vmin, vmax = -0.8, 0.8
norm = plt.Normalize(vmin=vmin, vmax=vmax)
cmap = plt.get_cmap("divergent_RWTH")   # blue → green → red, registered by rwthplots

# ---------------------------------------------------------------------------
# Figure — classic stripe layout (no axes, just colour bars)
# ---------------------------------------------------------------------------
with rwthplots.context("rwth-word"):
    fig, ax = plt.subplots(figsize=(12, 3))

    for i, (year, val) in enumerate(zip(years, anomaly)):
        ax.axvspan(year - 0.5, year + 0.5, color=cmap(norm(val)), linewidth=0)

    ax.set_xlim(years[0] - 0.5, years[-1] + 0.5)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Minimal annotation
    ax.text(0.01, 0.04, str(years[0]),  transform=ax.transAxes,
            fontsize=8, color="white", va="bottom")
    ax.text(0.99, 0.04, str(years[-1]), transform=ax.transAxes,
            fontsize=8, color="white", va="bottom", ha="right")
    ax.set_title("Global temperature anomaly (synthetic) — RWTH divergent colourmap",
                 fontsize=9, pad=6)

    # Colourbar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    cbar = fig.colorbar(sm, ax=ax, orientation="horizontal",
                        fraction=0.04, pad=0.15, shrink=0.4)
    cbar.set_label("Temperature anomaly (°C)", fontsize=8)
    cbar.ax.tick_params(labelsize=7)

    import os
    os.makedirs("figures", exist_ok=True)
    save_figure(fig, "figures/climate_stripes", formats=["png", "pdf"])
    plt.close(fig)

print("Saved figures/climate_stripes.{png,pdf}")

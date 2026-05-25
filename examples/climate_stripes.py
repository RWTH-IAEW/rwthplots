"""
Climate stripes — Nordrhein-Westfalen (DWD area average)
=========================================================
Recreates Ed Hawkins' 'warming stripes' using the official NRW area-averaged
annual mean temperature published by the German Weather Service (DWD).

Dataset:  DWD regional averages — Nordrhein-Westfalen, annual air temperature mean
Period:   1881–2025  (145 years, no gaps)
Baseline: 1961–1990 mean (~8.96 °C)
Colours:  cold years → RWTH blue (#00549F),
          warm years → RWTH red  (#CC071E),
          opacity proportional to the magnitude of the anomaly.

Source:   DWD Climate Data Center (CDC), open data
          https://opendata.dwd.de/climate_environment/CDC/
          regional_averages_DE/annual/air_temperature_mean/
Original concept: Ed Hawkins (University of Reading), showyourstripes.info
"""

import io
import os
import urllib.request

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import rwthplots
from rwthplots import save_figure

# ---------------------------------------------------------------------------
# Download and parse DWD Germany area-averaged annual temperature
# ---------------------------------------------------------------------------
_DWD_URL = (
    "https://opendata.dwd.de/climate_environment/CDC/"
    "regional_averages_DE/annual/air_temperature_mean/"
    "regional_averages_tm_year.txt"
)


def _load_germany_temperatures():
    """Return (years, annual_mean_temp_degC) numpy arrays for Nordrhein-Westfalen."""
    with urllib.request.urlopen(_DWD_URL, timeout=15) as resp:
        lines = resp.read().decode("latin-1").splitlines()

    # Line 0: description/date; line 1: column header; lines 2+: data
    header = [h.strip() for h in lines[1].split(";")]
    de_idx = header.index("Nordrhein-Westfalen")

    years, temps = [], []
    for line in lines[2:]:
        parts = [p.strip() for p in line.split(";")]
        if len(parts) <= de_idx or parts[de_idx] == "":
            continue
        years.append(int(parts[0]))
        temps.append(float(parts[de_idx]))

    return np.array(years), np.array(temps)


years, temps = _load_germany_temperatures()

# Anomaly relative to 1961–1990 baseline
_mask_base = (years >= 1961) & (years <= 1990)
baseline = temps[_mask_base].mean()
anomaly = temps - baseline

# ---------------------------------------------------------------------------
# Colour mapping — RWTH blue / red with opacity scaling
# ---------------------------------------------------------------------------
BLUE = "#00549F"
RED  = "#CC071E"
_max_abs = np.max(np.abs(anomaly))


def _stripe(val):
    """Return (hex_colour, alpha) for a given anomaly value."""
    return (BLUE if val < 0 else RED, min(abs(val) / _max_abs, 1.0))


# ---------------------------------------------------------------------------
# Figure — classic stripe layout (no axes, just colour bars)
# ---------------------------------------------------------------------------
with rwthplots.context("rwth-word"):
    fig, ax = plt.subplots(figsize=(12, 3))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    for year, val in zip(years, anomaly):
        color, alpha = _stripe(val)
        ax.axvspan(year - 0.5, year + 0.5, color=color, alpha=alpha, linewidth=0)

    ax.set_xlim(years[0] - 0.5, years[-1] + 0.5)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.01, 0.04, str(years[0]),  transform=ax.transAxes,
            fontsize=8, color="#555555", va="bottom")
    ax.text(0.99, 0.04, str(years[-1]), transform=ax.transAxes,
            fontsize=8, color="#555555", va="bottom", ha="right")

    ax.set_title(
        f"Nordrhein-Westfalen annual temperature anomaly relative to {baseline:.2f} °C"
        f" (1961–1990 baseline)  ·  DWD area average",
        fontsize=9, pad=6,
    )

    cold_patch = mpatches.Patch(color=BLUE, label="Below baseline")
    warm_patch = mpatches.Patch(color=RED,  label="Above baseline")
    ax.legend(handles=[cold_patch, warm_patch], loc="upper left",
              fontsize=7, framealpha=0.7, handlelength=1.2)

    os.makedirs("figures", exist_ok=True)
    save_figure(fig, "figures/climate_stripes", formats=["png", "pdf"])
    plt.close(fig)

print(
    f"Saved figures/climate_stripes.{{png,pdf}}  "
    f"({years[0]}–{years[-1]}, baseline {baseline:.3f} °C, n={len(years)} years)"
)

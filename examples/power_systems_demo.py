"""
Power-system colormaps demonstration
======================================
Shows the four RWTH colormaps designed for power-system visualisation:
voltage deviations, line loading, renewable fraction, and frequency deviation.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import rwthplots
from rwthplots import save_figure, context
from rwthplots.cmap import rwth_cmap
from rwthplots.formatter import set_size

import os
os.makedirs("figures", exist_ok=True)
rng = np.random.default_rng(0)

# ---------------------------------------------------------------------------
# Shared helper — grid of random values for each colourmap
# ---------------------------------------------------------------------------
x = np.linspace(0, 1, 256)
gradient = np.vstack([x, x])

with context("rwth-word"):
    fig, axes = plt.subplots(4, 1, figsize=set_size("a4-half", subplots=(4, 1)))
    fig.subplots_adjust(hspace=0.15, left=0.22, right=0.98, top=0.96, bottom=0.04)

    specs = [
        ("voltage_RWTH",   "Voltage deviation  (red ← nominal → red)"),
        ("loading_RWTH",   "Line loading  (blue → green → yellow → orange → red)"),
        ("renewable_RWTH", "Renewable fraction  (black → orange → green)"),
        ("frequency_RWTH", "Frequency deviation  (blue ← nominal → red)"),
    ]

    for ax, (name, label) in zip(axes, specs):
        ax.imshow(gradient, aspect="auto", cmap=rwth_cmap(name))
        ax.set_axis_off()
        ax.text(-0.01, 0.5, label, va="center", ha="right", fontsize=7.5,
                transform=ax.transAxes)

    fig.suptitle("Power-system colormaps", fontsize=9, x=0.6)
    save_figure(fig, "figures/power_systems_cmaps", formats=["png", "pdf"])
    plt.close(fig)

# ---------------------------------------------------------------------------
# Voltage map — 2D grid of bus voltages
# ---------------------------------------------------------------------------
n_buses = 20
voltages = 1.0 + rng.uniform(-0.12, 0.12, (n_buses, n_buses))

with context("rwth-word"):
    fig, ax = plt.subplots(figsize=set_size("ieee-column"))
    # Symmetric norm centred at 1.0 pu
    norm = mcolors.TwoSlopeNorm(vcenter=1.0, vmin=0.88, vmax=1.12)
    im = ax.imshow(voltages, cmap=rwth_cmap("voltage_RWTH"), norm=norm,
                   interpolation="nearest")
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Voltage (pu)", fontsize=7)
    cbar.ax.tick_params(labelsize=6)
    ax.set_title("Bus voltage magnitudes", fontsize=8)
    ax.set_xlabel("Bus column", fontsize=7)
    ax.set_ylabel("Bus row", fontsize=7)
    ax.tick_params(labelsize=6)
    save_figure(fig, "figures/voltage_map", formats=["png"])
    plt.close(fig)

# ---------------------------------------------------------------------------
# Line loading bar chart
# ---------------------------------------------------------------------------
n_lines = 15
loading = rng.uniform(0.1, 1.15, n_lines)
line_labels = [f"L{i+1:02d}" for i in range(n_lines)]

cmap_load = rwth_cmap("loading_RWTH")

with context("rwth-word"):
    fig, ax = plt.subplots(figsize=set_size("ieee-column"))
    colors = [cmap_load(min(v, 1.0)) for v in loading]
    bars = ax.bar(line_labels, loading * 100, color=colors, edgecolor="none")
    ax.axhline(100, color="#CC071E", linewidth=1, linestyle="--", label="Limit")
    ax.set_ylabel("Loading (%)", fontsize=7)
    ax.set_title("Line loading", fontsize=8)
    ax.tick_params(axis="x", rotation=45, labelsize=6)
    ax.tick_params(axis="y", labelsize=6)
    ax.legend(fontsize=7)
    save_figure(fig, "figures/line_loading", formats=["png"])
    plt.close(fig)

# ---------------------------------------------------------------------------
# Frequency deviation time series with coloured fill
# ---------------------------------------------------------------------------
t = np.linspace(0, 60, 600)  # 60 seconds
freq_dev = 0.3 * np.sin(2 * np.pi * t / 20) * np.exp(-t / 30)
freq_dev += rng.normal(0, 0.03, len(t))

cmap_freq = rwth_cmap("frequency_RWTH")

with context("rwth-word"):
    fig, ax = plt.subplots(figsize=set_size("ieee-column"))
    norm_freq = mcolors.Normalize(vmin=-0.5, vmax=0.5)
    for i in range(len(t) - 1):
        ax.fill_between(t[i:i+2], freq_dev[i:i+2], color=cmap_freq(norm_freq(freq_dev[i])),
                        linewidth=0)
    ax.axhline(0, color="#000000", linewidth=0.5)
    ax.set_xlabel("Time (s)", fontsize=7)
    ax.set_ylabel("Frequency deviation (Hz)", fontsize=7)
    ax.set_title("Frequency deviation", fontsize=8)
    ax.tick_params(labelsize=6)
    save_figure(fig, "figures/frequency_deviation", formats=["png"])
    plt.close(fig)

print("Power-system figures saved to examples/figures/")

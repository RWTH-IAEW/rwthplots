"""
New features demonstration
===========================
Shows the features added in v3.1: accessibility utilities, context manager,
save_figure, pick_colors, new colormaps, and journal / size styles.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import rwthplots
from rwthplots import (
    context, save_figure, pick_colors, check_accessibility,
    plot_color_palette, set_size,
)
from rwthplots.cmap import rwth_cmap, rwth_cset

os.makedirs("figures", exist_ok=True)
rng = np.random.default_rng(42)

# ---------------------------------------------------------------------------
# 1. plot_color_palette — overview of all RWTH tints
# ---------------------------------------------------------------------------
fig = plot_color_palette()
save_figure(fig, "figures/color_palette", formats=["png"])
plt.close(fig)
print("1. colour palette saved")

# ---------------------------------------------------------------------------
# 2. New colormaps (heat, thermal, divergent_bm, divergent_gy, viridis)
# ---------------------------------------------------------------------------
cmaps_to_show = [
    "heat_RWTH", "thermal_RWTH",
    "divergent_RWTH", "divergent_bm_RWTH", "divergent_gy_RWTH",
    "viridis_RWTH",
]
x = np.linspace(0, 1, 256)
gradient = np.vstack([x, x])

with context("rwth-word"):
    fig, axes = plt.subplots(len(cmaps_to_show), 1,
                             figsize=set_size("a4-half", subplots=(len(cmaps_to_show), 1)))
    fig.subplots_adjust(hspace=0.1, left=0.25, right=0.98, top=0.97, bottom=0.03)
    for ax, name in zip(axes, cmaps_to_show):
        ax.imshow(gradient, aspect="auto", cmap=rwth_cmap(name))
        ax.set_axis_off()
        ax.text(-0.01, 0.5, name, va="center", ha="right", fontsize=7,
                transform=ax.transAxes)
    save_figure(fig, "figures/new_colormaps", formats=["png"])
    plt.close(fig)
print("2. new colormaps saved")

# ---------------------------------------------------------------------------
# 3. pick_colors — most distinct RWTH colours for N series
# ---------------------------------------------------------------------------
with context("rwth-word"):
    fig, ax = plt.subplots(figsize=set_size("a4-half"))
    x = np.linspace(0, 2 * np.pi, 200)
    for i, color in enumerate(pick_colors(6)):
        ax.plot(x, np.sin(x + i * np.pi / 6), color=color,
                label=f"Series {i + 1}", linewidth=1.5)
    ax.set_xlabel("x")
    ax.set_ylabel("amplitude")
    ax.set_title("6 most distinct RWTH colours (pick_colors)")
    ax.legend(fontsize=7, ncol=2)
    save_figure(fig, "figures/pick_colors_demo", formats=["png"])
    plt.close(fig)
print("3. pick_colors demo saved")

# ---------------------------------------------------------------------------
# 4. check_accessibility — print results for the default RWTH 100% palette
# ---------------------------------------------------------------------------
colors_100 = list(rwth_cset("rwth_100"))
issues = check_accessibility(colors_100, threshold=20.0)
print(f"\n4. Accessibility check (threshold delta-E = 20):")
if issues:
    for iss in issues[:5]:
        print(f"   {iss['cvd_type']:15s}  {iss['color_a']} ↔ {iss['color_b']}"
              f"  ΔE={iss['delta_e']:.1f}")
    if len(issues) > 5:
        print(f"   ... {len(issues) - 5} more")
else:
    print("   No issues found.")

# ---------------------------------------------------------------------------
# 5. context() + size styles — compose styles concisely
# ---------------------------------------------------------------------------
with context("rwth-word", "size.ieee-column"):
    fig, ax = plt.subplots()
    x = np.linspace(0, 4 * np.pi, 300)
    ax.plot(x, np.sin(x), label="sin")
    ax.plot(x, np.cos(x), label="cos")
    ax.set_xlabel("x (rad)")
    ax.set_ylabel("amplitude")
    ax.set_title("IEEE single-column size")
    ax.legend()
    save_figure(fig, "figures/ieee_column_demo", formats=["png"])
    plt.close(fig)
print("5. IEEE column figure saved")

# ---------------------------------------------------------------------------
# 6. save_figure — write PDF + PNG + SVG in one call
# ---------------------------------------------------------------------------
with context("rwth-word"):
    fig, ax = plt.subplots(figsize=set_size("nature-column"))
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.plot(np.cos(theta), np.sin(theta))
    ax.set_aspect("equal")
    ax.set_title("save_figure demo (PDF + PNG + SVG)")
    save_figure(fig, "figures/multi_format", formats=["pdf", "png", "svg"])
    plt.close(fig)
print("6. multi-format figure saved (pdf, png, svg)")

# ---------------------------------------------------------------------------
# 7. Colorblind-safe cycle
# ---------------------------------------------------------------------------
with context("rwth-word", "misc.colorblind"):
    fig, ax = plt.subplots(figsize=set_size("a4-half"))
    x = np.linspace(0, 2 * np.pi, 200)
    labels = ["blue", "orange", "black", "yellow", "violet", "purple"]
    for i, label in enumerate(labels):
        ax.plot(x, np.sin(x + i * np.pi / 6) * (1 - 0.08 * i),
                label=label, linewidth=1.5)
    ax.set_xlabel("x")
    ax.set_title("Colorblind-safe RWTH cycle (misc.colorblind)")
    ax.legend(fontsize=7, ncol=2)
    save_figure(fig, "figures/colorblind_demo", formats=["png"])
    plt.close(fig)
print("7. colorblind demo saved")

print("\nAll figures written to examples/figures/")

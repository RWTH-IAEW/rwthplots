# rwthplots

**Matplotlib style sheets, colormaps, and colour utilities based on the RWTH Aachen University corporate design palette.**

Developed at the [Institute for High Voltage Equipment and Grids, Digitalization and Energy Economics (IAEW)](https://www.iaew.rwth-aachen.de), RWTH Aachen University.

---

## Gallery

**RWTH colour palette** — 13 base colours × 5 tint levels

![Colour palette](images/color_palette.png)

**Line plot with `context()` and `pick_colors(6)`**

![Style demo](images/style_demo.png)

**Colormaps** — key maps overview

![Colormaps](images/colormaps.png)

**Climate stripes** — RWTH blue / red with opacity

![Climate stripes](images/climate_stripes.png)

---

## Features at a glance

| Feature | Description |
|---|---|
| **6 base styles** | LaTeX, Word, PowerPoint, dark, Beamer — drop-in `plt.style.use()` |
| **Composable modifiers** | 16 colour cycles, 6 misc tweaks, 6 journal presets, 15 size modifiers |
| **41 colormaps** | Diverging, sequential, discrete, and power-system maps |
| **Colour sets** | Named qualitative palettes in HEX / RGB / normalised RGB |
| **Accessibility** | CVD simulation, delta-E reporting, `pick_colors()` greedy selection |
| **Figure sizing** | `set_size()` with 15 journal/paper presets |
| **Multi-format export** | `save_figure()` writes PDF + PNG + SVG in one call |

---

## Quick install

```sh
pip install git+https://gitlab.iaew.rwth-aachen.de/aev/RWTHPlots.git
```

See [Installation](installation.md) for full options.

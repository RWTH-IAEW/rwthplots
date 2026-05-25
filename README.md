# rwthplots

**Matplotlib style sheets, colormaps, and figure utilities for RWTH Aachen University's corporate design palette.**

[![PyPI](https://img.shields.io/pypi/v/rwthplots)](https://pypi.org/project/rwthplots/)
[![Python](https://img.shields.io/pypi/pyversions/rwthplots)](https://pypi.org/project/rwthplots/)
[![CI](https://github.com/RWTH-IAEW/rwthplots/actions/workflows/ci.yml/badge.svg)](https://github.com/RWTH-IAEW/rwthplots/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://rwth-iaew.github.io/rwthplots/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE.txt)

Developed at the [Institute for High Voltage Equipment and Grids, Digitalization and Energy Economics (IAEW)](https://www.iaew.rwth-aachen.de), RWTH Aachen University.

---

## What it does

`rwthplots` brings the official [RWTH Aachen corporate design](https://www.rwth-aachen.de/go/id/obfa)
into Matplotlib — so your thesis, paper, and presentation figures are always
on-brand without manual rcParams setup.

- **Style sheets** for every output format: LaTeX/thesis, Word, PowerPoint, Beamer, dark-mode
- **38 colormaps** (+ `_r` reversed variants) — discrete, diverging, sequential, and power-system maps
- **Journal presets** for IEEE, Nature, Elsevier, Springer, APS, and ACM
- **Accessibility utilities** — CVD simulation, colour-confusion detection, greedy `pick_colors()`
- **Figure sizing** — `set_size()` with 15 paper/journal presets and golden-ratio height
- **Multi-format export** — `save_figure()` writes PDF + PNG + SVG in one call

---

## Gallery

**RWTH colour palette** — 13 base colours × 5 tint levels

![Colour palette](docs/images/color_palette.png)

**Line plot with `context()` and `pick_colors(6)`**

![Style demo](docs/images/style_demo.png)

**Colormaps** — selection of available maps

![Colormaps](docs/images/colormaps.png)

**Climate stripes** — Nordrhein-Westfalen 1881–2025, DWD area average

![Climate stripes](docs/images/climate_stripes.png)

---

## Installation

```sh
pip install rwthplots
```

Or install the latest development version directly from GitHub:

```sh
pip install git+https://github.com/RWTH-IAEW/rwthplots.git
```

Requires Python ≥ 3.10 and Matplotlib ≥ 3.7.

---

## Quick start

```python
import rwthplots
import matplotlib.pyplot as plt

# Apply a style — all styles and colormaps are registered on import
with rwthplots.context("rwth-latex", "color.blue", "size.ieee-column"):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    rwthplots.save_figure(fig, "results/fig1", formats=["pdf", "png"])
```

See the [Quick Start guide](https://rwth-iaew.github.io/rwthplots/quickstart/) for a full walkthrough.

---

## Style sheets

### Base styles

| Name | Use case |
|---|---|
| `rwthplots.styles.rwth-latex` | LaTeX/PGF, thesis, journal |
| `rwthplots.styles.rwth-word` | Word, reports |
| `rwthplots.styles.rwth-pptx` | PowerPoint |
| `rwthplots.styles.rwth-latex-pptx` | LaTeX-rendered text in PPT |
| `rwthplots.styles.rwth-latex-beamer` | Beamer slides |
| `rwthplots.styles.rwth-dark` | Dark background / screens |

### Modifier layers

Stack any modifier on top of a base style:

| Category | Examples |
|---|---|
| `color/` | `color.blue`, `color.orange`, `color.green`, … (16 total) |
| `misc/` | `misc.grid`, `misc.colorblind`, `misc.sans`, `misc.no-latex`, … |
| `journals/` | `journals.ieee`, `journals.nature`, `journals.elsevier`, `journals.springer`, `journals.aps`, `journals.acm` |
| `size/` | `size.ieee-column`, `size.a4`, `size.nature-column`, … (15 total) |

---

## Colormaps

38 colormaps registered on import (plus `_r` reversed variants for all). Key maps:

| Name | Type | Description |
|---|---|---|
| `extended_RWTH_discrete` | discrete | Full RWTH palette, up to 65 colours (`lut=`) |
| `continuous_RWTH_discrete` | discrete | Continuous coverage, 1–65 colours (`lut=`) |
| `divergent_RWTH` | diverging | Blue → green → red |
| `divergent_bm_RWTH` | diverging | Blue – white – magenta |
| `divergent_gy_RWTH` | diverging | Green – white – yellow |
| `viridis_RWTH` | sequential | Violet → turquoise → may green → yellow |
| `thermal_RWTH` | sequential | Black → bordeaux → red → orange → yellow → white (blackbody) |
| `loading_RWTH` | sequential | Blue → white → yellow → red → bordeaux (line/transformer loading) |
| `voltage_RWTH` | diverging | Red → orange → green → orange → red (voltage deviation) |
| `blue_RWTH` | sequential | Blue tint gradient |
| *(+ 12 single-colour gradients)* | | One per RWTH base colour |

---

## Development

```sh
git clone https://github.com/RWTH-IAEW/rwthplots.git
cd rwthplots
uv sync --group dev
uv run python -m pytest -q
```

---

## License

MIT — see [`LICENSE.txt`](LICENSE.txt).

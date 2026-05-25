# Quick Start

```python
import rwthplots                    # registers all colormaps and styles on import
import matplotlib.pyplot as plt
import numpy as np
```

On import, rwthplots performs two setup steps automatically so you never need
to call any registration function manually:

1. All 41 RWTH colormaps are registered with Matplotlib via
   `matplotlib.colormaps.register()`.
2. All `.mplstyle` files under the package's `styles/` tree are injected into
   `plt.style.library`, making them addressable as `rwthplots.styles.<name>`.

---

## Applying a style

rwthplots ships six base styles that target different output formats, plus a
library of composable modifier sheets.

```python
# Apply a single base style globally
plt.style.use("rwthplots.styles.rwth-latex")   # LaTeX / thesis
plt.style.use("rwthplots.styles.rwth-word")    # Word / report
plt.style.use("rwthplots.styles.rwth-pptx")    # PowerPoint
plt.style.use("rwthplots.styles.rwth-dark")    # Dark background

# Layer a base style with modifier sheets
plt.style.use([
    "rwthplots.styles.rwth-latex",
    "rwthplots.styles.color.blue",        # single-hue blue cycle
    "rwthplots.styles.misc.grid",         # add grid lines
    "rwthplots.styles.size.ieee-column",  # set figure size for IEEE
])
```

!!! note "Style sheet persistence"
    `plt.style.use()` changes rcParams globally for the rest of the session.
    Use `rwthplots.context()` to apply styles only inside a `with` block and
    have them reset automatically afterwards.

## Context manager

The `context()` helper wraps `plt.style.context()` and auto-expands short
names so you don't have to type the full `rwthplots.styles.` prefix:

```python
x = np.linspace(0, 2 * np.pi, 200)

with rwthplots.context("rwth-latex", "color.blue", "size.ieee-column"):
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), label=r"$\sin(x)$")
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.legend()
    plt.show()
# rcParams are fully restored here — no side effects outside the block
```

Name expansion rules:

| You write | Resolved to |
|---|---|
| `"rwth-latex"` | `"rwthplots.styles.rwth-latex"` |
| `"color.blue"` | `"rwthplots.styles.color.blue"` |
| `"misc.grid"` | `"rwthplots.styles.misc.grid"` |
| `"size.ieee-column"` | `"rwthplots.styles.size.ieee-column"` |
| `"rwthplots.styles.rwth-word"` | passed through unchanged |

---

## Colormaps

All 38 colormaps are registered with Matplotlib on import — including `_r`
reversed variants for every map (e.g. `loading_RWTH_r`):

```python
plt.set_cmap("divergent_RWTH")          # blue → green → red diverging
plt.set_cmap("loading_RWTH")            # blue → white → yellow → red

# Factory — returns a LinearSegmentedColormap object
from rwthplots.cmap import rwth_cmap
cmap = rwth_cmap("extended_RWTH_discrete", lut=8)  # 8-colour discrete palette

# Use directly with any Matplotlib function
fig, ax = plt.subplots()
ax.imshow(data, cmap=rwth_cmap("voltage_RWTH"))
```

Print all registered names:

```python
print(rwth_cmap())   # returns tuple of all 38 names
```

See [Colormaps](colormaps.md) for guidance on choosing the right map.

---

## Colour sets

Named qualitative palettes for categorical data. Each of the 13 RWTH base
colours is available at five tint levels (100 %, 75 %, 50 %, 25 %, 10 %).

```python
from rwthplots.cmap import rwth_cset

cset = rwth_cset("rwth_100")            # full-intensity colours (default)
print(cset.blue)                        # '#00549F'
print(cset.orange)                      # '#F6A800'
print(list(cset))                       # all 13 as a list

# Other tint levels
cset_75 = rwth_cset("rwth_75")         # 75 % tints
cset_50 = rwth_cset("rwth_50")         # 50 % tints

# Format conversion
cset_rgb  = rwth_cset("rwth_100", frmt="RGB")    # integer (R, G, B) tuples
cset_nrgb = rwth_cset("rwth_100", frmt="NRGB")   # normalised float tuples
print(cset_rgb.blue)                    # (0, 84, 159)
print(cset_nrgb.blue)                   # (0.0, 0.329..., 0.624...)
```

---

## Figure sizing

`set_size()` converts a point width (or a named preset) to a `(width, height)`
tuple in inches, using the golden ratio for height. Pass the result directly
to `figsize=`:

```python
from rwthplots.formatter import set_size, list_presets

# Named presets
fig, ax = plt.subplots(figsize=set_size("ieee-column"))    # 252 pt / 3.5 in
fig, ax = plt.subplots(figsize=set_size("a4"))             # 484 pt / 6.7 in
fig, ax = plt.subplots(figsize=set_size("nature-column"))  # 253 pt / 3.5 in

# Custom point width
fig, ax = plt.subplots(figsize=set_size(300))              # 300 pt wide

# Multi-panel figures — height scaled for the subplot grid
fig, axes = plt.subplots(3, 1, figsize=set_size("ieee-column", subplots=(3, 1)))

# List all 18 named presets and their widths in points
print(list_presets())
```

Alternatively, use a `size/` style modifier — it applies the same geometry
via rcParams:

```python
plt.style.use(["rwthplots.styles.rwth-latex",
               "rwthplots.styles.size.nature-column"])
```

---

## Accessibility tools

### Pick maximally distinct colours

`pick_colors(n)` uses a greedy farthest-point algorithm in CIELAB space to
select the *n* most perceptually distinct colours from the RWTH 100 % palette.
The first colour is always RWTH blue:

```python
colors = rwthplots.pick_colors(4)
# → ['#00549F', '#FFED00', '#57AB27', '#E30066']  (approximately)

# Use as a manual colour cycle
with rwthplots.context("rwth-word"):
    fig, ax = plt.subplots(figsize=set_size("ieee-page"))
    for i, c in enumerate(rwthplots.pick_colors(6)):
        ax.plot(x, np.sin(x + i * 0.5), color=c, label=f"Series {i+1}")
    ax.legend()
```

### Check for colour-vision deficiency issues

`check_accessibility()` simulates three CVD types (deuteranopia, protanopia,
tritanopia) using the Viénot-Brettel-Mollon (1997/1999) model and reports
colour pairs whose simulated CIE 1976 delta-E falls below a threshold:

```python
colors = rwthplots.pick_colors(6)
issues = rwthplots.check_accessibility(colors, threshold=20.0)

if not issues:
    print("Palette passes CVD check.")
else:
    for issue in issues:
        print(f"{issue['cvd_type']}: {issue['color_a']} ↔ {issue['color_b']}  "
              f"ΔE = {issue['delta_e']}")
```

### Built-in CVD-safe cycle

The `misc.colorblind` modifier applies a pre-validated 6-colour cycle that
differs in both hue and luminance across all three common CVD types:

```python
plt.style.use(["rwthplots.styles.rwth-latex",
               "rwthplots.styles.misc.colorblind"])
```

---

## Exporting figures

`save_figure()` writes a figure to multiple formats in a single call and
creates any missing parent directories automatically.  DPI is ignored for
vector formats (PDF, SVG, EPS):

```python
rwthplots.save_figure(fig, "results/voltage_map", formats=["pdf", "png"], dpi=300)
# Creates:  results/voltage_map.pdf
#           results/voltage_map.png  (300 dpi)
```

---

## Visualising the RWTH palette

```python
fig = rwthplots.plot_color_palette()   # 13 × 5 tint grid
plt.show()
```

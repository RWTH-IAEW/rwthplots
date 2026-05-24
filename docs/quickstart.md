# Quick Start

```python
import rwthplots                    # registers all colormaps and styles on import
import matplotlib.pyplot as plt
```

## Applying a style

```python
# Direct use
plt.style.use("rwthplots.styles.rwth-latex")   # LaTeX / thesis
plt.style.use("rwthplots.styles.rwth-word")    # Word / report
plt.style.use("rwthplots.styles.rwth-pptx")    # PowerPoint
plt.style.use("rwthplots.styles.rwth-dark")    # Dark background

# Compose a base style with modifiers
plt.style.use([
    "rwthplots.styles.rwth-latex",
    "rwthplots.styles.color.blue",
    "rwthplots.styles.misc.grid",
    "rwthplots.styles.size.ieee-column",
])
```

## Context manager

Short style names are auto-expanded — no need to type the full prefix:

```python
import numpy as np
with rwthplots.context("rwth-latex", "color.blue", "size.ieee-column"):
    fig, ax = plt.subplots()
    ax.plot(np.linspace(0, 1, 100), np.sin(np.linspace(0, 6, 100)))
    plt.show()
```

## Colormaps

```python
plt.set_cmap("divergent_RWTH")          # blue → green → red diverging
plt.set_cmap("loading_RWTH")            # blue → green → yellow → red (loading)
plt.set_cmap("voltage_RWTH")            # symmetric voltage deviation

from rwthplots.cmap import rwth_cmap
cmap = rwth_cmap("extended_RWTH_discrete", lut=13)
```

## Colour sets

```python
from rwthplots.cmap import rwth_cset

cset = rwth_cset("rwth_100")            # hex strings (default)
print(cset.blue)                        # '#00549F'

cset_rgb  = rwth_cset("rwth_100", frmt="RGB")    # integer (R,G,B) tuples
cset_nrgb = rwth_cset("rwth_100", frmt="NRGB")   # normalised float tuples
```

## Figure sizing

```python
from rwthplots.formatter import set_size, list_presets

fig, ax = plt.subplots(figsize=set_size("ieee-column"))   # 252 pt wide
fig, ax = plt.subplots(figsize=set_size("a4"))            # A4 text width
print(list_presets())                                     # all preset names
```

## Accessibility tools

```python
# Pick N maximally distinct RWTH colours in CIELAB space
colors = rwthplots.pick_colors(6)

# Simulate colour-vision deficiency and report confusable pairs
issues = rwthplots.check_accessibility(colors, threshold=20.0)
for issue in issues:
    print(issue)

# Apply the built-in CVD-safe 6-colour cycle
plt.style.use(["rwthplots.styles.rwth-latex",
               "rwthplots.styles.misc.colorblind"])
```

## Exporting figures

```python
# Save to multiple formats in one call
rwthplots.save_figure(fig, "output/my_plot", formats=["pdf", "png", "svg"], dpi=300)
```

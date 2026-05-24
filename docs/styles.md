# Style Sheets

All styles are registered automatically on `import rwthplots` and can be used
via `plt.style.use()` or the [`context()`][rwthplots.utils.context] manager.

## How style discovery works

On import, rwthplots walks its `styles/` directory tree and calls
`plt.style.core.read_style_directory()` on each subfolder, then merges the
results into `plt.style.library`.  This means:

- **New `.mplstyle` files** placed anywhere under `src/rwthplots/styles/` are
  auto-discovered the next time the package is imported — no registration code
  needed.
- **Full Matplotlib names** like `rwthplots.styles.rwth-latex` or
  `rwthplots.styles.color.blue` work in `plt.style.use()` out of the box.
- **Short names** work with the `context()` helper, which prepends the
  `rwthplots.styles.` prefix automatically.

---

## Base styles

Choose one base style that matches your target output format, then layer
modifier sheets on top.

| Name | Use case |
|---|---|
| `rwth-latex` | LaTeX/PGF output — serif font, full LaTeX rendering, 1200 dpi, 426 pt thesis width |
| `rwth-word` | Word / reports — same geometry as `rwth-latex` but no LaTeX dependency |
| `rwth-pptx` | PowerPoint — 12 × 12 cm canvas, Arial, transparent background, 1500 dpi |
| `rwth-latex-pptx` | LaTeX-rendered text sized and positioned for PowerPoint slides |
| `rwth-latex-beamer` | Beamer slides — standard 4:3 slide geometry with LaTeX fonts |
| `rwth-dark` | Dark background for screens and presentations — 50 % tint colour cycle on black |

!!! tip "Thesis / journal workflow"
    Use `rwth-latex` as the base for all publication figures.  The style sets
    `text.usetex = True` and `font.family = serif`, so Matplotlib hands off
    all text rendering to LaTeX.  Add `pgf` to the style stack when embedding
    figures directly in a `.tex` document via `\includegraphics`.

!!! tip "PowerPoint workflow"
    `rwth-pptx` sets a transparent canvas background so the figure blends
    seamlessly into a slide.  Export with `save_figure(fig, path, formats=["png"],
    dpi=300)` for screen quality, or `formats=["pdf"]` if your slide deck
    supports vector graphics.

---

## Composing styles

Modifier sheets are designed to be layered on top of any base style.
Later sheets override earlier ones, so order matters:

```python
# Apply globally
plt.style.use([
    "rwthplots.styles.rwth-latex",       # base: LaTeX rendering, serif
    "rwthplots.styles.color.orange",     # override colour cycle → orange tints
    "rwthplots.styles.misc.grid",        # add light grid lines
    "rwthplots.styles.size.nature-column",  # set figure size for Nature
])

# Or scoped to a block
with rwthplots.context("rwth-word", "color.orange", "misc.grid", "size.nature-column"):
    fig, ax = plt.subplots()
    ax.plot(x, y)
```

---

## Colour modifiers (`color/`)

Each colour modifier sets `axes.prop_cycle` to a 5-step tint ramp for one
RWTH base colour (100 % → 75 % → 50 % → 25 % → 10 %).  They are ideal for
single-hue plots such as bar charts or line series that encode one quantity
across categories.

| Style | Base colour |
|---|---|
| `color.blue` | RWTH Blue `#00549F` |
| `color.red` | Red `#CC071E` |
| `color.orange` | Orange `#F6A800` |
| `color.yellow` | Yellow `#FFED00` |
| `color.green` | Green `#57AB27` |
| `color.maygreen` | May Green `#BDCD00` |
| `color.petrol` | Petrol `#006165` |
| `color.turquoise` | Turquoise `#0098A1` |
| `color.magenta` | Magenta `#E30066` |
| `color.bordeaux` | Bordeaux `#A11035` |
| `color.violet` | Violet `#612158` |
| `color.purple` | Purple `#7A6FAC` |
| `color.black` | Greyscale ramp |
| `color.standard` | Full 13-colour RWTH cycle |
| `color.extended` | Full 65-colour RWTH cycle |
| `color.divergent` | 24-step blue → red cycle for diverging data |

---

## Miscellaneous modifiers (`misc/`)

Small cross-cutting tweaks that can be combined with any base or colour style.

| Style | Effect |
|---|---|
| `misc.grid` | Adds light grey grid lines (`axes.grid = True`, low alpha) |
| `misc.colorblind` | Replaces the colour cycle with a pre-validated 6-colour CVD-safe set |
| `misc.sans` | Switches to sans-serif font (no LaTeX) |
| `misc.no-latex` | Disables LaTeX rendering (`text.usetex = False`) |
| `misc.latex-sans` | LaTeX rendering with sans-serif math font (`sfmath` package) |
| `misc.pgf` | PGF backend settings for embedding in LaTeX documents |

### `misc.colorblind` in detail

The 6-colour CVD-safe cycle is:

| Colour | Hex | L* |
|---|---|---|
| RWTH Blue | `#00549F` | 34 |
| Orange | `#F6A800` | 72 |
| Black | `#000000` | 0 |
| Yellow | `#FFED00` | 94 |
| Violet | `#612158` | 19 |
| Purple | `#7A6FAC` | 51 |

The luminance spread (L* range 0–94) ensures the palette remains distinguishable
when converted to greyscale and under all three common CVD types.

---

## Journal styles (`journals/`)

Journal modifiers set figure size, font family, font size, and DPI to match
the submission requirements of specific publishers.  Stack them on top of
`rwth-latex` or `rwth-word`:

```python
plt.style.use(["rwthplots.styles.rwth-latex",
               "rwthplots.styles.journals.nature"])
```

| Style | Column width | Font | Size | DPI |
|---|---|---|---|---|
| `journals.ieee` | 3.30 in | Times | 8 pt | 600 |
| `journals.nature` | 3.54 in | Sans-serif | 8 pt | 600 |
| `journals.elsevier` | 3.54 in | Serif | 9 pt | 600 |
| `journals.springer` | 4.80 in | Serif | 10 pt | 600 |
| `journals.aps` | 3.38 in | Serif | 10 pt | 600 |
| `journals.acm` | 3.33 in | Serif | 9 pt | 600 |

!!! note
    For the exact current submission requirements, always check the journal's
    author guidelines — these values follow typical specifications but may
    change.

---

## Size modifiers (`size/`)

Size modifiers set only `figure.figsize` using the golden ratio for height.
They are the style-sheet equivalent of calling `set_size("name")` and can be
combined with any base style or journal modifier.

```python
# Style-based sizing
plt.style.use(["rwthplots.styles.rwth-latex",
               "rwthplots.styles.size.ieee-column"])

# Programmatic sizing (equivalent)
from rwthplots.formatter import set_size
fig, ax = plt.subplots(figsize=set_size("ieee-column"))
```

| Style | Width (pt) | Width (in) | Typical use |
|---|---|---|---|
| `size.a4` | 483.69 | 6.70 | A4 full text width |
| `size.a4-half` | 241.85 | 3.35 | A4 half-width / two columns |
| `size.letter` | 469.76 | 6.50 | US Letter text width |
| `size.letter-half` | 234.88 | 3.25 | US Letter half-width |
| `size.ieee-column` | 252.0 | 3.49 | IEEE Transactions single column |
| `size.ieee-page` | 505.89 | 7.00 | IEEE Transactions full page |
| `size.nature-column` | 253.16 | 3.50 | Nature single column |
| `size.nature-page` | 520.47 | 7.20 | Nature full page |
| `size.science-column` | 162.09 | 2.24 | Science single column |
| `size.elsevier-column` | 255.87 | 3.54 | Elsevier single column |
| `size.elsevier-page` | 540.17 | 7.48 | Elsevier full page |
| `size.springer-column` | 346.88 | 4.80 | Springer LNCS column |
| `size.aps-column` | 243.91 | 3.38 | APS Physical Review column |
| `size.aps-page` | 487.82 | 6.75 | APS Physical Review full page |
| `size.acm-column` | 240.66 | 3.33 | ACM column |

Height is calculated automatically as `width × (√5 − 1) / 2` (golden ratio).
For multi-panel figures use `set_size("name", subplots=(rows, cols))` instead
of the style modifier.

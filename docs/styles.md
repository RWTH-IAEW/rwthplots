# Style Sheets

All styles are registered automatically on `import rwthplots` and can be used
via `plt.style.use()` or the [`context()`][rwthplots.context] manager.

## Base styles

| Name | Use case |
|---|---|
| `rwthplots.styles.rwth-latex` | LaTeX/PGF, thesis, journal — serif font, LaTeX rendering |
| `rwthplots.styles.rwth-word` | Word, reports — same geometry without LaTeX dependency |
| `rwthplots.styles.rwth-pptx` | PowerPoint — 12 × 12 cm, Arial, transparent canvas |
| `rwthplots.styles.rwth-latex-pptx` | LaTeX-rendered text sized for PowerPoint |
| `rwthplots.styles.rwth-latex-beamer` | Beamer slides |
| `rwthplots.styles.rwth-dark` | Dark background for screens and presentations |

## Composing styles

Modifier sheets are layered on top of any base style:

```python
plt.style.use([
    "rwthplots.styles.rwth-latex",       # base
    "rwthplots.styles.color.orange",     # colour modifier
    "rwthplots.styles.misc.grid",        # grid lines
    "rwthplots.styles.size.nature-column",  # figure size
])

# Or with the short-name context manager
with rwthplots.context("rwth-latex", "color.orange", "misc.grid", "size.nature-column"):
    ...
```

## Colour modifiers (`color/`)

Single-hue colour cycles derived from the RWTH palette (100 % → 10 % tints):

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
| `color.black` | Black/Grey scale |
| `color.standard` | Full 13-colour RWTH cycle |
| `color.extended` | Full 65-colour RWTH cycle |
| `color.divergent` | 24-step blue→red divergent cycle |

## Miscellaneous modifiers (`misc/`)

| Style | Effect |
|---|---|
| `misc.grid` | Adds light grid lines |
| `misc.colorblind` | 6-colour CVD-safe RWTH cycle |
| `misc.sans` | Switch to sans-serif font |
| `misc.no-latex` | Disable LaTeX rendering |
| `misc.latex-sans` | LaTeX rendering with sans-serif math font |
| `misc.pgf` | PGF backend settings for LaTeX integration |

## Journal styles (`journals/`)

| Style | Journal / publisher |
|---|---|
| `journals.ieee` | IEEE two-column (3.3 in, Times, 8 pt) |
| `journals.nature` | Nature (3.5 in, sans-serif, 8 pt) |
| `journals.elsevier` | Elsevier (3.54 in, serif, 9 pt) |
| `journals.springer` | Springer (4.8 in, serif, 10 pt) |
| `journals.aps` | APS Physical Review (3.375 in, serif, 10 pt) |
| `journals.acm` | ACM (3.33 in, serif, 9 pt) |

## Size modifiers (`size/`)

Drop-in figure geometry modifiers — set only `figure.figsize` using the golden
ratio. Combine with any base style.

| Style | Width (pt) | Typical use |
|---|---|---|
| `size.a4` | 483.69 | A4 full text width |
| `size.a4-half` | 241.85 | A4 half-width |
| `size.letter` | 469.76 | US Letter text width |
| `size.letter-half` | 234.88 | US Letter half-width |
| `size.ieee-column` | 252.0 | IEEE single column |
| `size.ieee-page` | 505.89 | IEEE full page |
| `size.nature-column` | 253.16 | Nature single column |
| `size.nature-page` | 520.47 | Nature full page |
| `size.science-column` | 162.09 | Science single column |
| `size.elsevier-column` | 255.87 | Elsevier single column |
| `size.elsevier-page` | 540.17 | Elsevier full page |
| `size.springer-column` | 346.88 | Springer single column |
| `size.aps-column` | 243.91 | APS single column |
| `size.aps-page` | 487.82 | APS full page |
| `size.acm-column` | 240.66 | ACM single column |

!!! note
    Size modifiers are also available programmatically via
    [`set_size()`][rwthplots.formatter.set_size] and
    [`list_presets()`][rwthplots.formatter.list_presets].

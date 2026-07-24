# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [Unreleased]

### Removed
- Renovate configuration (`.github/renovate.json5`) — the Renovate app is no
  longer installed on the repository.

---

## [3.2.2] — 2026-07-24

### Fixed
- Compatibility with matplotlib 3.11: style registration no longer uses the
  `matplotlib.style.core` module (deprecated in 3.9, removed in 3.11).
  Styles are now parsed with the stable `matplotlib.rc_params_from_file()`
  API. Importing rwthplots under matplotlib 3.11 previously raised
  `AttributeError`. Internal `_`-prefixed matplotlib styles are also no
  longer exposed in `plt.style.available`.

### Changed
- All locked dependencies upgraded (matplotlib 3.11.1 on Python ≥ 3.11,
  pytest 9, pillow 12, coverage 7.15, …).
- GitHub Actions bumped to latest majors: `checkout@v7`, `setup-python@v7`,
  `setup-uv@v9`, `upload-artifact@v7`.

### Added
- Renovate configuration (`.github/renovate.json5`) for automated weekly
  dependency updates: grouped non-major Python PRs, weekly `uv.lock`
  refresh, automerged GitHub Actions minor/patch bumps.

---

## [3.2.1] — 2026-05-25

### Changed
- README and documentation index rewritten with PyPI/CI/docs badges, clearer
  RWTH-internal audience framing, and "Why rwthplots?" motivating paragraph.
- `pyproject.toml` updated: SPDX license string, `matplotlib>=3.7` minimum
  (was incorrect `>=3.10.9`), full `[project.urls]` block, and PyPI classifiers.

### Added
- GitHub Actions workflows: `ci.yml` (pytest matrix 3.10–3.13), `docs.yml`
  (MkDocs gh-deploy on push to main), `release.yml` (test matrix + PyPI
  Trusted Publisher publish on version tag).

---

## [3.2.0] — 2026-05-25

### Added
- `_r` reversed variants registered for all 38 colormaps at import time
  (e.g. `loading_RWTH_r`, `thermal_RWTH_r`), matching standard Matplotlib
  convention.

### Changed
- `loading_RWTH` redesigned: **blue → white → yellow → red → bordeaux**.
  Removed green and orange stops; a pale-blue bridge prevents the RGB
  green cast that arises from linear blue→yellow interpolation.
- `thermal_RWTH` redesigned as a blackbody/incandescence map:
  **black → bordeaux → red → orange → yellow → white**.
- `climate_stripes.py` now downloads real DWD data for Nordrhein-Westfalen
  (area average, 1881–2025, 145 years) and computes anomalies relative to
  the 1961–1990 baseline.
- Gallery images regenerated; `docs/images/colormaps.png` updated.

### Removed
- `heat_RWTH` colormap (blue → orange → white sequential).
- `renewable_RWTH` colormap (black → orange → yellow → green).
- `frequency_RWTH` colormap (blue → green → red diverging).
- `styles_discovery.py` (dead module; style loading is handled in `__init__.py`).

---

## [3.1.1] — 2026-05-24

### Added
- MkDocs Material documentation site with IAEW branding, full API reference,
  style sheet and colormap guides, and example gallery.

### Changed
- `loading_RWTH` colormap starts from RWTH blue (unloaded) instead of green
  for better contrast at low loading values.
- Climate stripes example uses RWTH blue / red with opacity only (no
  intermediate colours), matching the original Ed Hawkins design intent.

### Fixed
- Cycler syntax in 22 `.mplstyle` files changed from single-quoted to
  double-quoted strings for Matplotlib 3.10 compatibility.
- `MANIFEST.in` removed (redundant with `pyproject.toml` package-data).
- `.DS_Store` removed from repository; added to `.gitignore`.

---

## [3.1.0] — 2026-05-24

### Added

**Colormaps** (13 new, total 41)
- `viridis_RWTH` — violet → turquoise → may green → yellow perceptual gradient.
  Inspired by RWTH-Colors (Philipp Simon Leibner, IFS RWTH Aachen, MIT).
- `heat_RWTH` — sequential: blue → orange → white.
- `thermal_RWTH` — cold-to-hot: petrol → turquoise → green → yellow.
- `divergent_bm_RWTH` — blue – white – magenta.
- `divergent_gy_RWTH` — green – white – yellow.
- **Power-system colormaps:**
  - `voltage_RWTH` — symmetric red → orange → green → orange → red for
    voltage deviations centred at the nominal value.
  - `loading_RWTH` — green → yellow → orange → red → bordeaux for line /
    transformer loading (0 % to overloaded).
  - `renewable_RWTH` — black → orange → yellow → green for renewable fraction.
  - `frequency_RWTH` — blue → green (nominal) → red for frequency deviation.

**Colour sets**
- `rwth_cset()` now accepts `frmt='HEX'|'RGB'|'NRGB'`.
  Inspired by RWTH-Colors (Philipp Simon Leibner, IFS RWTH Aachen, MIT).

**Utility functions** (all accessible as `rwthplots.<name>`)
- `save_figure(fig, path, formats, dpi)` — multi-format export, auto-mkdir.
- `context(*styles)` — `plt.style.context` wrapper with auto-prefix expansion.
- `check_accessibility(colors, types, threshold)` — CVD simulation (Viénot-
  Brettel-Mollon model) with delta-E reporting.
- `pick_colors(n, colorset)` — greedy farthest-point selection in CIELAB.
- `list_presets()` — dict of all `set_size()` preset names and pt widths.
- `plot_color_palette()` — 13 × 5 RWTH tint grid figure.
  Inspired by RWTH-Colors (Philipp Simon Leibner, IFS RWTH Aachen, MIT).

**Style sheets** (10 new)
- `rwth-dark` — dark-background variant.
  Inspired by RWTH-Colors (Philipp Simon Leibner, IFS RWTH Aachen, MIT).
- `misc.colorblind` — 6-colour CVD-safe RWTH cycle.
- `journals.elsevier`, `journals.springer`, `journals.aps`, `journals.acm`.
- `size/` directory — 15 composable figure-geometry modifiers:
  `a4`, `a4-half`, `letter`, `letter-half`, `ieee-column`, `ieee-page`,
  `nature-column`, `nature-page`, `science-column`, `elsevier-column`,
  `elsevier-page`, `springer-column`, `aps-column`, `aps-page`, `acm-column`.

**`set_size()` presets** — all 15 size-style names added to `_PRESETS`.

**Examples**
- `climate_stripes.py` — warming-stripes with `divergent_RWTH`.
- `new_features_demo.py` — walkthrough of all v3.1 features.
- `power_systems_demo.py` — voltage map, loading bars, frequency time series.

### Changed
- Fallback warnings in `rwth_cmap()` and `rwth_cset()` now use
  `warnings.warn()` instead of `print()`.
- All `rwth_cset()` namedtuple types unified to `RWTHColorset`.
- `_PRESETS` in `formatter.py` lifted to module level.
- `__all__` added to `__init__.py`, `cmap.py`, `formatter.py`, `utils.py`.
- `rwthplots.styles.size` registered as a style package.

### Fixed
- `SyntaxWarning: invalid escape sequence '\s'` in `formatter.py` docstring.
- `turqoise_RWTH` typo corrected to `turquoise_RWTH` in colourmap namelist.
- `lut` parameter silently dropped for `continuous_RWTH_discrete`; fixed.
- `mpl.colormaps.register()` now called with `force=True`.

---

## [3.0.2] — prior release
- Fixed installation issue with pip.

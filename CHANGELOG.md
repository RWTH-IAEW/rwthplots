# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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

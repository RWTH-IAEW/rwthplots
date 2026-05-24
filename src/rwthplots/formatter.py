#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
Definition of figure size for using Matplotlib with LaTeX.

example of usage:
x = np.linspace(0, 2 * np.pi, 100)
# Initialise figure instance
fig, ax = plt.subplots(1, 1, figsize=set_size(width))

or for multiple figures: fig, ax = plt.subplots(5, 2, figsize=set_size(width, subplots=(5, 2)))

# Plot
ax.plot(x, np.sin(x))
ax.set_xlim(0, 2 * np.pi)
ax.set_xlabel(r'$\theta$')
ax.set_ylabel(r'$\sin (\theta)$')

# Save and remove excess whitespace
fig.savefig('example_1.pdf', format='pdf', bbox_inches='tight')

all credits go out to Jack Walton https://jwalton.info/Embed-Publication-Matplotlib-Latex/

Predefined width names: call list_presets() to see all available keys.

Institut für Elektrische Anlagen und Netze, Digitalisierung und Energiewirtschaft (IAEW)
(c) 2022, Steffen Kortmann
"""

__all__ = ["set_size", "list_presets"]

# Width presets in typographic points (1 pt = 1/72.27 in).
_PRESETS: dict[str, float] = {
    # RWTH-specific
    'thesis':            426.79135,
    'beamer-full':       918.08522,
    'beamer-half':       440.67697,
    # Paper sizes (text area with typical margins)
    'a4':                483.69,     # 170 mm text width
    'a4-half':           241.85,     # half-column A4
    'letter':            469.76,     # 6.5 in (US letter, 1 in margins)
    'letter-half':       234.88,     # half-column letter
    # Journal column / page widths
    'ieee-column':       252.0,      # IEEE Transactions, 3.5 in single column
    'ieee-page':         505.89,     # IEEE Transactions, 7.0 in full page
    'nature-column':     253.16,     # Nature, 89 mm single column
    'nature-page':       520.47,     # Nature, 183 mm full page
    'science-column':    162.09,     # Science, 57 mm single column
    'elsevier-column':   255.87,     # Elsevier, 90 mm single column
    'elsevier-page':     540.17,     # Elsevier, 190 mm full page
    'springer-column':   346.88,     # Springer LNCS, 122 mm
    'aps-column':        243.91,     # APS Physical Review, 3.375 in single column
    'aps-page':          487.82,     # APS Physical Review, 6.75 in full page
    'acm-column':        240.66,     # ACM, 3.33 in single column
}


def set_size(width: float | str, fraction=1, subplots=(1, 1)):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float or string
            Document width in points, or a predefined name.
            Call ``list_presets()`` for all available names.
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: array-like, optional
            The number of rows and columns of subplots.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    if isinstance(width, str):
        if width not in _PRESETS:  # type: ignore[operator]
            raise ValueError(
                f"Unknown predefined width {width!r}. "
                f"Known values: {sorted(_PRESETS)}. "
                "Pass a numeric point value for a custom width."
            )
        width_pt = _PRESETS[width]
    else:
        width_pt = width

    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction
    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5 ** .5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return fig_width_in, fig_height_in


def list_presets() -> dict[str, float]:
    """Return all named width presets and their values in typographic points."""
    return dict(_PRESETS)

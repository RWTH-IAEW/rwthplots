#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utility helpers: figure export, style context, and colour accessibility tools.
"""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import Sequence

import numpy as np

__all__ = ["save_figure", "context", "check_accessibility", "pick_colors"]


# ---------------------------------------------------------------------------
# CVD simulation constants
# Matrices from Viénot, Brettel & Mollon (1999) and Brettel, Viénot & Mollon
# (1997), as validated in the daltonize project
# (https://github.com/joergdietrich/daltonize, MIT license).
# ---------------------------------------------------------------------------

# sRGB → XYZ (D65, IEC 61966-2-1)
_SRGB_TO_XYZ = np.array([
    [0.4124564, 0.3575761, 0.1804375],
    [0.2126729, 0.7151522, 0.0721750],
    [0.0193339, 0.1191920, 0.9503041],
])

# XYZ → LMS (Hunt-Pointer-Estévez / Bradford D65 adaptation)
_XYZ_TO_LMS = np.array([
    [ 0.8951,  0.2664, -0.1614],
    [-0.7502,  1.7135,  0.0367],
    [ 0.0389, -0.0685,  1.0296],
])

_RGB_TO_LMS: np.ndarray = _XYZ_TO_LMS @ _SRGB_TO_XYZ
_LMS_TO_RGB: np.ndarray = np.linalg.inv(_RGB_TO_LMS)
_D65_XYZ = np.array([0.95047, 1.00000, 1.08883])

# Confusion matrices in LMS space (one per CVD type)
_CVD_MATRICES: dict[str, np.ndarray] = {
    "deuteranopia": np.array([   # M cone absent (~6 % of males)
        [1.,       0.,       0.     ],
        [0.494207, 0.,       1.24827],
        [0.,       0.,       1.     ],
    ]),
    "protanopia": np.array([     # L cone absent (~2 % of males)
        [0.,       2.02344, -2.52581],
        [0.,       1.,       0.     ],
        [0.,       0.,       1.     ],
    ]),
    "tritanopia": np.array([     # S cone absent (rare, ~0.003 %)
        [1.,        0.,       0.],
        [0.,        1.,       0.],
        [-0.395913, 0.801109, 0.],
    ]),
}

_VECTOR_FORMATS = frozenset({"pdf", "svg", "eps", "pgf", "ps"})


# ---------------------------------------------------------------------------
# Internal colour math
# ---------------------------------------------------------------------------

def _srgb_to_linear(c: np.ndarray) -> np.ndarray:
    c = np.asarray(c, dtype=float)
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def _simulate_cvd(rgb_linear: np.ndarray, cvd_type: str) -> np.ndarray:
    lms = rgb_linear @ _RGB_TO_LMS.T
    lms_sim = lms @ _CVD_MATRICES[cvd_type].T
    return np.clip(lms_sim @ _LMS_TO_RGB.T, 0.0, 1.0)


def _linear_rgb_to_lab(rgb: np.ndarray) -> np.ndarray:
    """Convert linear sRGB (..., 3) → CIELAB (..., 3) under D65."""
    xyz = (rgb @ _SRGB_TO_XYZ.T) / _D65_XYZ
    delta = 6.0 / 29.0

    def _f(t: np.ndarray) -> np.ndarray:
        return np.where(t > delta ** 3, t ** (1.0 / 3.0),
                        t / (3.0 * delta ** 2) + 4.0 / 29.0)

    fx, fy, fz = _f(xyz[..., 0]), _f(xyz[..., 1]), _f(xyz[..., 2])
    return np.stack([116.0 * fy - 16.0, 500.0 * (fx - fy), 200.0 * (fy - fz)], axis=-1)


def _hex_colors_to_linear(colors: Sequence[str]) -> np.ndarray:
    from .cmap import _hex_to_rgb
    srgb = np.array([np.array(_hex_to_rgb(c)) / 255.0 for c in colors])
    return _srgb_to_linear(srgb)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def save_figure(fig, path, formats=("pdf", "png"), dpi=None, **savefig_kwargs):
    """
    Save a matplotlib figure to multiple file formats in one call.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
    path : str or pathlib.Path
        Output path *without* file extension.  Parent directories are created
        automatically.
    formats : sequence of str
        File formats to write (e.g. ``["pdf", "png", "svg"]``).
    dpi : int or None
        DPI override for raster formats.  Ignored for vector formats
        (pdf, svg, eps, pgf, ps).  If *None*, the figure's current DPI is used.
    **savefig_kwargs
        Forwarded to :meth:`~matplotlib.figure.Figure.savefig`.

    Examples
    --------
    save_figure(fig, "results/my_plot", formats=["pdf", "png"], dpi=300)
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    for fmt in formats:
        kw = dict(savefig_kwargs)
        kw.setdefault("bbox_inches", "tight")
        if dpi is not None and fmt.lower() not in _VECTOR_FORMATS:
            kw.setdefault("dpi", dpi)
        fig.savefig(path.with_suffix(f".{fmt}"), format=fmt, **kw)


def context(*styles: str):
    """
    Return a :func:`matplotlib.pyplot.style.context` manager with automatic
    ``rwthplots.styles.`` prefix expansion.

    Short names (without ``rwthplots.styles.``) are expanded automatically:

    * ``'rwth-latex'``        → ``'rwthplots.styles.rwth-latex'``
    * ``'color.blue'``        → ``'rwthplots.styles.color.blue'``
    * ``'misc.grid'``         → ``'rwthplots.styles.misc.grid'``
    * ``'size.ieee-column'``  → ``'rwthplots.styles.size.ieee-column'``

    Full names (already starting with ``'rwthplots.'``) are passed through.

    Examples
    --------
    with rwthplots.context('rwth-latex', 'color.blue', 'misc.grid'):
        fig, ax = plt.subplots()
        ax.plot(x, y)
    """
    import matplotlib.pyplot as plt
    resolved = [
        s if s.startswith("rwthplots.") else f"rwthplots.styles.{s}"
        for s in styles
    ]
    return plt.style.context(resolved)


def check_accessibility(
    colors: Sequence[str],
    types: Sequence[str] = ("deuteranopia", "protanopia", "tritanopia"),
    threshold: float = 10.0,
) -> list[dict]:
    """
    Simulate colour vision deficiencies and report pairs that would be confused.

    CVD simulation uses the Viénot-Brettel-Mollon model (1997/1999).
    Perceptual distance is CIE 1976 delta-E in CIELAB.

    Parameters
    ----------
    colors : sequence of str
        ``'#RRGGBB'`` hex colour strings to evaluate.
    types : sequence of str
        CVD types to simulate.  Supported: ``'deuteranopia'``,
        ``'protanopia'``, ``'tritanopia'``.
    threshold : float
        Delta-E below which two simulated colours are flagged as confusable.
        Default 10 (clearly noticeable); use 20 for a stricter check.

    Returns
    -------
    issues : list of dict
        Each entry: ``{'cvd_type', 'color_a', 'color_b', 'delta_e'}``.
        Empty list means the palette passes.

    Examples
    --------
    from rwthplots.cmap import rwth_cset
    issues = check_accessibility(list(rwth_cset('rwth_100')))
    for issue in issues:
        print(issue)
    """
    unknown = set(types) - set(_CVD_MATRICES)
    if unknown:
        raise ValueError(
            f"Unknown CVD type(s): {unknown}. Choose from {set(_CVD_MATRICES)}."
        )

    linear = _hex_colors_to_linear(colors)
    n = len(colors)
    issues: list[dict] = []

    for cvd_type in types:
        sim_linear = _simulate_cvd(linear, cvd_type)
        sim_lab = _linear_rgb_to_lab(sim_linear)
        for i in range(n):
            for j in range(i + 1, n):
                delta_e = float(np.sqrt(np.sum((sim_lab[i] - sim_lab[j]) ** 2)))
                if delta_e < threshold:
                    issues.append({
                        "cvd_type": cvd_type,
                        "color_a": colors[i],
                        "color_b": colors[j],
                        "delta_e": round(delta_e, 2),
                    })

    return issues


def pick_colors(n: int, colorset: str = "rwth_100") -> list[str]:
    """
    Return the *n* most perceptually distinct RWTH colours.

    Uses a greedy farthest-point algorithm in CIELAB space.  The first
    colour is always RWTH blue; each subsequent pick maximises the minimum
    CIE 1976 delta-E to the already-selected set.

    Parameters
    ----------
    n : int
        Number of colours to return (1–13).
    colorset : str
        RWTH tint level to sample from.

    Returns
    -------
    colors : list of str
        ``'#RRGGBB'`` hex strings in selection order.

    Examples
    --------
    pick_colors(4)
    # ['#00549F', '#FFED00', '#57AB27', '#E30066']  (approximately)
    """
    from .cmap import rwth_cset

    all_colors = list(rwth_cset(colorset))
    total = len(all_colors)

    if not (1 <= n <= total):
        raise ValueError(f"n must be between 1 and {total}, got {n}.")

    lab = _linear_rgb_to_lab(_hex_colors_to_linear(all_colors))

    selected: list[int] = [0]  # start with blue
    remaining = list(range(1, total))
    while len(selected) < n:
        best_idx = max(
            remaining,
            key=lambda i: min(
                float(np.sqrt(np.sum((lab[i] - lab[j]) ** 2)))
                for j in selected
            ),
        )
        selected.append(best_idx)
        remaining.remove(best_idx)

    return [all_colors[i] for i in selected]

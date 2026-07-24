import importlib.resources as _ir
import matplotlib as _mpl
import matplotlib.pyplot as _plt

from .register_colors import register_rwth_colormaps
from .cmap import RWTHcmaps, plot_color_palette
from .formatter import set_size, list_presets
from .utils import save_figure, context, check_accessibility, pick_colors

__all__ = [
    "RWTHcmaps",
    "plot_color_palette",
    "set_size",
    "list_presets",
    "save_figure",
    "context",
    "check_accessibility",
    "pick_colors",
    "register_rwth_colormaps",
]

register_rwth_colormaps()

# Populate plt.style.library so rwthplots styles appear in plt.style.available.
# plt.style.use("rwthplots.styles.<name>") also works without this block via
# matplotlib's built-in package-lookup mechanism (importlib.resources).
# The matplotlib.style entry points in pyproject.toml will handle this
# automatically once a future matplotlib release adds entry-point support.
_STYLE_PACKAGES = [
    "rwthplots.styles",
    "rwthplots.styles.color",
    "rwthplots.styles.misc",
    "rwthplots.styles.journals",
    "rwthplots.styles.size",
]
# matplotlib.style.core was removed in matplotlib 3.11, so only stable public
# API is used here (rc_params_from_file, style.library, style.available).
for _pkg in _STYLE_PACKAGES:
    try:
        for _res in _ir.files(_pkg).iterdir():
            if not _res.name.endswith(".mplstyle"):
                continue
            _style_name = f"{_pkg}.{_res.name.removesuffix('.mplstyle')}"
            with _ir.as_file(_res) as _style_path:
                _plt.style.library[_style_name] = _mpl.rc_params_from_file(
                    _style_path, use_default_template=False
                )
    except Exception as _exc:
        import warnings as _warnings
        _warnings.warn(f"rwthplots: could not load styles from {_pkg!r}: {_exc}", stacklevel=1)
_plt.style.available[:] = sorted(
    _name for _name in _plt.style.library if not _name.startswith("_")
)
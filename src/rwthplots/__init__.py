import importlib.resources as _ir
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
for _pkg in _STYLE_PACKAGES:
    try:
        _pkg_styles = _plt.style.core.read_style_directory(_ir.files(_pkg))
        _plt.style.core.update_nested_dict(
            _plt.style.library,
            {f"{_pkg}.{name}": rc for name, rc in _pkg_styles.items()},
        )
    except Exception as _exc:
        import warnings as _warnings
        _warnings.warn(f"rwthplots: could not load styles from {_pkg!r}: {_exc}", stacklevel=1)
_plt.style.core.available[:] = sorted(_plt.style.library.keys())
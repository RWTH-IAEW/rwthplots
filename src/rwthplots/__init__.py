import os  # pathlib.Path.walk not available in Python <3.12
import matplotlib.pyplot as plt
import rwthplots
from .styles_discovery import read_styles_in_folders
from .register_colors import register_rwth_colormaps
from .cmap import RWTHcmaps
from .formatter import set_size

# Register the RWTH colormaps when the package is imported
register_rwth_colormaps()

# https://github.com/garrettj403/SciencePlots/blob/master/scienceplots/__init__.py
# register the bundled stylesheets in the matplotlib style library
scienceplots_path = rwthplots.__path__[0]
styles_path = os.path.join(scienceplots_path, "styles")

# Reads styles in /styles folder and all subfolders
stylesheets = read_styles_in_folders(styles_path)

# Update dictionary of styles - plt.style.library
plt.style.core.update_nested_dict(plt.style.library, stylesheets)

# Update `plt.style.available`, copy-paste from:
# https://github.com/matplotlib/matplotlib/blob/a170539a421623bb2967a45a24bb7926e2feb542/lib/matplotlib/style/core.py#L266  # noqa: E501
plt.style.core.available[:] = sorted(plt.style.library.keys())
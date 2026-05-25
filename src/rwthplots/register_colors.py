#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Registers RWTH colormaps with Matplotlib.

Copyright (c) by Institute for High Voltage Equipment and Grids,
Digitalization and Energy Economics (IAEW), RWTH Aachen University,
05.12.2024, s.kortmann. All rights reserved.
"""

import logging

from .cmap import RWTHcmaps
import matplotlib.pyplot as plt
import matplotlib as mpl

def register_rwth_colormaps():
    """
    Register all RWTH colormaps defined in RWTHcmaps.
    """
    rwth_cmaps = RWTHcmaps()  # Initialize RWTHcmaps instance

    for cmap_name in rwth_cmaps.namelist:
        # Check if the function exists in the class
        if cmap_name in rwth_cmaps.funcdict:
            # Set the cmap name in the instance
            rwth_cmaps.cname = cmap_name
            # Generate the colormap by calling the respective method
            rwth_cmaps.funcdict[cmap_name]()
            # Register the generated colormap with Matplotlib
            mpl.colormaps.register(name=cmap_name, cmap=rwth_cmaps.cmap, force=True)
            # Register the reversed variant (e.g. loading_RWTH_r)
            mpl.colormaps.register(name=f"{cmap_name}_r", cmap=rwth_cmaps.cmap.reversed(), force=True)
            logging.info(f"Registered RWTH colormap: {cmap_name}")

def plot_cmap():
    # Test the colormaps by printing the registered colormaps
    print("Registered colormaps:")
    print(sorted(mpl.colormaps(), reverse=True))

    # Visualize a test colormap
    cmap_name = 'divergent_RWTH'
    rwth_divergent_colors = [
        '#00549f', '#37628f', '#4c7080', '#5c7e73', '#6a8b67', '#77995b',
        '#86a650', '#96b345', '#a7bf3a', '#bbcc2e', '#d0d722', '#e6e213',
        '#fddd01', '#fbce04', '#f8be09', '#f5ae0e', '#f19e12', '#ed8e15',
        '#e87e17', '#e36d1a', '#de5c1b', '#d8481d', '#d2311d', '#cc071e'
    ]

    plt.figure(figsize=(8, 2))
    plt.imshow([list(range(len(rwth_divergent_colors)))], cmap=cmap_name, aspect="auto")
    plt.gca().set_axis_off()
    plt.title(f"Example: {cmap_name}")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    register_rwth_colormaps()
    plot_cmap()



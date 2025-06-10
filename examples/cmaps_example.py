#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Small description of cmaps_example

Copyright (c) by Institute for High Voltage Equipment and Grids, 
Digitalization and Energy Economics (IAEW), RWTH Aachen University, 
06.12.2024, s.kortmann. All rights reserved.
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example script to test and visualize all registered RWTH colormaps.

Copyright (c) by Institute for High Voltage Equipment and Grids,
Digitalization and Energy Economics (IAEW), RWTH Aachen University,
05.12.2024, s.kortmann. All rights reserved.
"""
import rwthplots
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure output directory exists
output_dir = "figures/cmaps"
os.makedirs(output_dir, exist_ok=True)

# Generate data for visualization
gradient = np.linspace(0, 1, 256).reshape(1, -1)  # Gradient for colormap visualization
x = np.linspace(-4 * np.pi, 4 * np.pi, 500)  # x values for line plot
y = np.sin(x)  # Example sinusoidal data

# List all registered colormaps
colormaps = sorted([cmap for cmap in rwthplots.cmap.RWTHcmaps().namelist])

print(f"Testing {len(colormaps)} colormaps...")

# Generate a plot for each colormap
for cmap_name in colormaps:
    try:
        print(f"Visualizing colormap: {cmap_name}")

        # Colormap gradient visualization
        plt.figure(figsize=(6, 2))
        plt.imshow(gradient, aspect='auto', cmap=cmap_name)
        plt.gca().set_axis_off()
        plt.title(f"Colormap: {cmap_name}")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/{cmap_name}_gradient.png", dpi=300)
        plt.close()

        # Line plot with the colormap
        plt.figure(figsize=(6, 4))
        colors = matplotlib.colormaps.get_cmap(cmap_name)(np.linspace(0, 1, 5))
        for i, color in enumerate(colors):
            plt.plot(x, y + i * 0.5, color=color, label=f"Line {i + 1}")
        plt.title(f"Line Plot with {cmap_name}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{output_dir}/{cmap_name}_lines.png", dpi=300)
        plt.close()

    except Exception as e:
        print(f"Failed to generate visualizations for {cmap_name}: {e}")

print("All colormaps have been tested and visualized.")

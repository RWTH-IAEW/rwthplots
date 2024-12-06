#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Small description of colours_example.py

Copyright (c) by Institute for High Voltage Equipment and Grids,
Digitalization and Energy Economics (IAEW), RWTH Aachen University,
14.03.2024, s.kortmann. All rights reserved.
"""
import RWTHPlots
from rwth_colors import colors
import matplotlib.pyplot as plt
plt.style.use('rwth-latex-beamer')

import os
if not os.path.exists("figures/colors"):
    os.makedirs("figures/colors")

import numpy as np

### Line Plot - Voltage vs. Time
t = np.linspace(-4 * np.pi, 4 * np.pi, 1000)  # Time vector
current = np.sin(t)  # Example current waveform
voltage = np.sin(t+np.pi/2)

plt.figure()
plt.plot(t, current, label="Current (I)", color=colors["blue"])
plt.plot(t, voltage, label="Voltage (V)", color=colors["magenta"])
plt.xlabel("Time (s)")
plt.ylabel("Current (A) / Voltage (V)")
plt.title("Electrical Voltage Current Waveform")
plt.legend()
plt.grid(True)
plt.savefig("figures/colors/v_i_characteristic.pdf", format="pdf")
plt.savefig("figures/colors/v_i_characteristic.png", format="png", dpi=300)

### Bar Chart - Power Consumption of Various Devices
devices = ['Laptop', 'Monitor', 'Router', 'Printer']
power_usage = [70, 30, 10, 5]

plt.figure()
plt.bar(devices, power_usage, color=[colors['green', 100], colors['green', 75], colors['green', 50], colors['green', 25]])
plt.title('Power Consumption of Various Devices')
plt.xlabel('Device')
plt.ylabel('Power Consumption (W)')
plt.savefig("figures/colors/power_consumption.pdf", format="pdf")
plt.savefig("figures/colors/power_consumption.png", format="png", dpi=300)

### Scatter Plot - Efficiency vs. Load for Different Generators
load = np.random.randint(50, 100, size=50)
efficiency = load / 100 + np.random.normal(0, 0.05, size=50)

plt.figure()
plt.scatter(load, efficiency, color=colors['magenta', 100], label='Generator Efficiency')
plt.title('Efficiency vs. Load')
plt.xlabel('Load (%)')
plt.ylabel('Efficiency')
plt.legend()
plt.savefig("figures/colors/efficiency.pdf", format="pdf")
plt.savefig("figures/colors/efficiency.png", format="png", dpi=300)

### Pie Chart - Distribution of Energy Sources
sources = ['Solar', 'Wind', 'Hydro', 'Nuclear']
distribution = [25, 35, 15, 25]

plt.figure()
plt.pie(distribution, labels=sources, colors=[colors['orange', 100], colors['lime', 100], colors['blue', 100], colors['lavender', 100]])
plt.title('Distribution of Energy Sources')
plt.savefig("figures/colors/distribution.pdf", format="pdf")
plt.savefig("figures/colors/distribution.png", format="png", dpi=300)


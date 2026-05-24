#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Known LaTeX rendering issues with RWTHPlots styles.

The rwth-word style is LaTeX-free and can be used when a system LaTeX
installation is unavailable.  The rwth-latex style requires a working
LaTeX installation and produces higher-quality output for publications.

Copyright (c) by Institute for High Voltage Equipment and Grids,
Digitalization and Energy Economics (IAEW), RWTH Aachen University,
14.03.2024, s.kortmann. All rights reserved.
"""

import os

import numpy as np
import matplotlib.pyplot as plt
import rwthplots  # noqa: F401 – registers colormaps and styles

os.makedirs("figures", exist_ok=True)


def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))


pparam = dict(xlabel='Voltage (mV)', ylabel='Current (A)')
x = np.linspace(0.75, 1.25, 201)

with plt.style.context(['rwthplots.styles.rwth-word']):
    fig, ax = plt.subplots()
    for p in [10, 20, 40, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig2a_word.pdf')
    fig.savefig('figures/fig2a_word.jpg', dpi=300)
    plt.close(fig)

with plt.style.context(['rwthplots.styles.rwth-latex']):
    fig, ax = plt.subplots()
    for p in [10, 20, 40, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig2a.pdf')
    fig.savefig('figures/fig2a.jpg', dpi=300)
    plt.close(fig)

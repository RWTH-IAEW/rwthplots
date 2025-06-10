#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
There are known issues for the usage of LaTeX in the RWTHPlots style.
PyCharm cannot plot it for some reason, but it can be displayed without the LaTeX style.
Then we can inspect the plots first and save it then to LaTeX.

Copyright (c) by Institute for High Voltage Equipment and Grids, 
Digitalization and Energy Economics (IAEW), RWTH Aachen University, 
14.03.2024, s.kortmann. All rights reserved.
"""

import numpy as np
import matplotlib.pyplot as plt

import os

if not os.path.exists("figures"):
    os.makedirs("figures")


def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))


pparam = dict(xlabel='Voltage (mV)', ylabel='Current ($\mu$A)')

x = np.linspace(0.75, 1.25, 201)

with plt.style.context(['rwth-word']):
    fig, ax = plt.subplots()
    for p in [10, 20, 40, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    # Note: $\mu$ doesn't work with Times font (used by ieee style)
    ax.set_ylabel(r'Current (A)')
    plt.show()

with plt.style.context(['rwth-latex']):
    fig, ax = plt.subplots()
    for p in [10, 20, 40, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    # Note: $\mu$ doesn't work with Times font (used by ieee style)
    ax.set_ylabel(r'Current (A)')
    fig.savefig('figures/fig2a.pdf')
    fig.savefig('figures/fig2a.jpg', dpi=300)
    plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Plot examples of RWTHPlots styles.

all credits go out to John D. Garret https://github.com/garrettj403/SciencePlots

Institut für Elektrische Anlagen und Netze, Digitalisierung und Energiewirtschaft (IAEW)
(c) 2022, Steffen Kortmann
"""

import os

import numpy as np
import matplotlib.pyplot as plt
import rwthplots  # noqa: F401 – registers colormaps

os.makedirs("figures", exist_ok=True)


def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))


pparam = dict(xlabel='Voltage (mV)', ylabel='Current (A)')
x = np.linspace(0.75, 1.25, 201)

with plt.style.context(['rwthplots.styles.rwth-custom']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100, 200, 300, 500]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(**pparam)
    fig.savefig('figures/fig1.pdf')
    fig.savefig('figures/fig1.jpg', dpi=300)
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

with plt.style.context(['rwthplots.styles.rwth-latex', 'rwthplots.styles.misc.grid']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig2b.pdf')
    fig.savefig('figures/fig2b.jpg', dpi=300)
    plt.close(fig)

with plt.style.context(['rwthplots.styles.rwth-latex', 'rwthplots.styles.color.blue']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig2c.pdf')
    fig.savefig('figures/fig2c.jpg', dpi=300)
    plt.close(fig)

with plt.style.context(['rwthplots.styles.rwth-latex', 'rwthplots.styles.color.red']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig2d.pdf')
    fig.savefig('figures/fig2d.jpg', dpi=300)
    plt.close(fig)

with plt.style.context(['rwthplots.styles.rwth-latex', 'rwthplots.styles.color.extended']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig2e.pdf')
    fig.savefig('figures/fig2e.jpg', dpi=300)
    plt.close(fig)

with plt.style.context(['rwthplots.styles.rwth-word', 'rwthplots.styles.color.extended']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig3.pdf')
    fig.savefig('figures/fig3.jpg', dpi=300)
    plt.close(fig)

with plt.style.context(['rwthplots.styles.rwth-latex-beamer-fira']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig4.pdf')
    fig.savefig('figures/fig4.jpg', dpi=300)
    plt.close(fig)

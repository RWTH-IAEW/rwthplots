#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition of RWTH colour schemes for lines and maps.

# Change default colorset (for lines) and colormap (for maps).
plt.rc('axes', prop_cycle=plt.cycler('color', list(rwth_cset('rwth_100'))))
matplotlib.colormaps.register(rwth_cmap('standard_RWTH_discrete'))
plt.rc('image', cmap='standard_RWTH_discrete')

all credits go out to Paul Tol //personal.sron.nl/~pault/

Institut für Elektrische Anlagen und Netze, Digitalisierung und Energiewirtschaft (IAEW)
(c) 2022, Steffen Kortmann
"""

import copy
import warnings
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, to_rgba_array

__all__ = ["RWTHcmaps", "rwth_cmap", "rwth_cset", "plot_color_palette", "discretemap"]


def _hex_to_rgb(h):
    """Convert a hex color string to an (R, G, B) integer tuple (0–255)."""
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def _hex_to_nrgb(h):
    """Convert a hex color string to a normalized (R, G, B) float tuple (0–1)."""
    return tuple(v / 255.0 for v in _hex_to_rgb(h))


def discretemap(colormap, hexclrs):
    """
    Produce a colormap from a list of discrete colors without interpolation.
    """
    clrs = to_rgba_array(hexclrs)
    clrs = np.vstack([clrs[0], clrs, clrs[-1]])
    cdict = {}
    for ki, key in enumerate(('red', 'green', 'blue')):
        cdict[key] = [(i / (len(clrs) - 2.), clrs[i, ki], clrs[i + 1, ki]) for i in
                      range(len(clrs) - 1)]
    return LinearSegmentedColormap(colormap, cdict)


class RWTHcmaps(object):
    """Registry of all RWTH Aachen colormaps.

    Each colormap is implemented as a method that sets ``self.cmap`` to a
    :class:`~matplotlib.colors.LinearSegmentedColormap` or discrete variant.
    The :func:`rwth_cmap` factory is the normal public entry point; instantiate
    this class directly only if you need to iterate over ``namelist``.

    Attributes:
        namelist: Tuple of all registered colormap name strings.
        funcdict: Mapping of name → bound method.
        cmap: Set by each method after calling :meth:`get`.
        cname: Set by :meth:`get` before calling the colormap method.
    """

    def __init__(self):
        self.cmap = None
        self.cname = None
        self.namelist = (
            'standard_RWTH_discrete', 'standard_RWTH',
            'blue_RWTH_discrete', 'blue_RWTH',
            'black_RWTH_discrete', 'black_RWTH',
            'magenta_RWTH_discrete', 'magenta_RWTH',
            'yellow_RWTH_discrete', 'yellow_RWTH',
            'petrol_RWTH_discrete', 'petrol_RWTH',
            'turquoise_RWTH_discrete', 'turquoise_RWTH',
            'green_RWTH_discrete', 'green_RWTH',
            'maygreen_RWTH_discrete', 'maygreen_RWTH',
            'orange_RWTH_discrete', 'orange_RWTH',
            'red_RWTH_discrete', 'red_RWTH',
            'bordeaux_RWTH_discrete', 'bordeaux_RWTH',
            'violet_RWTH_discrete', 'violet_RWTH',
            'purple_RWTH_discrete', 'purple_RWTH',
            'continuous_RWTH_discrete',
            'rolling_RWTH_discrete',
            'extended_RWTH_discrete',
            'divergent_RWTH',
            'viridis_RWTH',
            'thermal_RWTH',
            'divergent_bm_RWTH',
            'divergent_gy_RWTH',
            'voltage_RWTH',
            'loading_RWTH')

        self.funcdict = dict(
            zip(self.namelist,
                (self.standard_RWTH_discrete, self.standard_RWTH,
                 self.blue_RWTH_discrete, self.blue_RWTH,
                 self.black_RWTH_discrete, self.black_RWTH,
                 self.magenta_RWTH_discrete, self.magenta_RWTH,
                 self.yellow_RWTH_discrete, self.yellow_RWTH,
                 self.petrol_RWTH_discrete, self.petrol_RWTH,
                 self.turquoise_RWTH_discrete, self.turquoise_RWTH,
                 self.green_RWTH_discrete, self.green_RWTH,
                 self.maygreen_RWTH_discrete, self.maygreen_RWTH,
                 self.orange_RWTH_discrete, self.orange_RWTH,
                 self.red_RWTH_discrete, self.red_RWTH,
                 self.bordeaux_RWTH_discrete, self.bordeaux_RWTH,
                 self.violet_RWTH_discrete, self.violet_RWTH,
                 self.purple_RWTH_discrete, self.purple_RWTH,
                 self.continuous_RWTH_discrete, self.rolling_RWTH_discrete,
                 self.extended_RWTH_discrete, self.divergent_RWTH,
                 self.viridis_RWTH, self.thermal_RWTH,
                 self.divergent_bm_RWTH, self.divergent_gy_RWTH,
                 self.voltage_RWTH, self.loading_RWTH)))

    def standard_RWTH_discrete(self):
        """
        Define colormap 'RWTH_discrete'.
        """
        clrs = ['#00549F', '#000000', '#E30066', '#FFED00', '#006165',
                '#0098A1', '#57AB27', '#BDCD00', '#F6A800', '#CC071E',
                '#A11035', '#612158', '#7A6FAC']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def standard_RWTH(self):
        """
        Define colormap 'RWTH'.
        """
        clrs = ['#00549F', '#000000', '#E30066', '#FFED00', '#006165',
                '#0098A1', '#57AB27', '#BDCD00', '#F6A800', '#CC071E',
                '#A11035', '#612158', '#7A6FAC']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def blue_RWTH_discrete(self):
        """
        Define colormap 'blue_RWTH_discrete'.
        """
        clrs = ['#00549F', '#407FB7', '#8EBAE5', '#C7DDF2', '#E8F1FA']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def blue_RWTH(self):
        """
        Define colormap 'blue_RWTH'.
        """
        clrs = ['#00549F', '#407FB7', '#8EBAE5', '#C7DDF2', '#E8F1FA']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def black_RWTH_discrete(self):
        """
        Define colormap 'black_RWTH_discrete'.
        """
        clrs = ['#000000', '#646567', '#9C9E9F', '#CFD1D2', '#ECEDED']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def black_RWTH(self):
        """
        Define colormap 'black_RWTH'.
        """
        clrs = ['#000000', '#646567', '#9C9E9F', '#CFD1D2', '#ECEDED']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def magenta_RWTH_discrete(self):
        """
        Define colormap 'magenta_RWTH_discrete'.
        """
        clrs = ['#E30066', '#E96088', '#F19EB1', '#F9D2DA', '#FDEEF0']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def magenta_RWTH(self):
        """
        Define colormap 'magenta_RWTH'.
        """
        clrs = ['#E30066', '#E96088', '#F19EB1', '#F9D2DA', '#FDEEF0']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def yellow_RWTH_discrete(self):
        """
        Define colormap 'yellow_RWTH_discrete'.
        """
        clrs = ['#FFED00', '#FFF055', '#FFF59B', '#FFFAD1', '#FFFDEE']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def yellow_RWTH(self):
        """
        Define colormap 'yellow_RWTH'.
        """
        clrs = ['#FFED00', '#FFF055', '#FFF59B', '#FFFAD1', '#FFFDEE']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def petrol_RWTH_discrete(self):
        """
        Define colormap 'petrol_RWTH_discrete'.
        """
        clrs = ['#006165', '#2D7F83', '#7DA4A7', '#BFD0D1', '#E6ECEC']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def petrol_RWTH(self):
        """
        Define colormap 'petrol_RWTH'.
        """
        clrs = ['#006165', '#2D7F83', '#7DA4A7', '#BFD0D1', '#E6ECEC']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def turquoise_RWTH_discrete(self):
        """
        Define colormap 'turquoise_RWTH_discrete'.
        """
        clrs = ['#0098A1', '#00B1B7', '#89CCCF', '#CAE7E7', '#EBF6F6']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def turquoise_RWTH(self):
        """
        Define colormap 'turquoise_RWTH'.
        """
        clrs = ['#0098A1', '#00B1B7', '#89CCCF', '#CAE7E7', '#EBF6F6']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def green_RWTH_discrete(self):
        """
        Define colormap 'green_RWTH_discrete'.
        """
        clrs = ['#57AB27', '#8DC060', '#B8D698', '#DDEBCE', '#F2F7EC']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def green_RWTH(self):
        """
        Define colormap 'green_RWTH'.
        """
        clrs = ['#57AB27', '#8DC060', '#B8D698', '#DDEBCE', '#F2F7EC']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def maygreen_RWTH_discrete(self):
        """
        Define colormap 'maygreen_RWTH_discrete'.
        """
        clrs = ['#BDCD00', '#D0D95C', '#E0E69A', '#F0F3D0', '#F9FAED']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def maygreen_RWTH(self):
        """
        Define colormap 'maygreen_RWTH'.
        """
        clrs = ['#BDCD00', '#D0D95C', '#E0E69A', '#F0F3D0', '#F9FAED']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def orange_RWTH_discrete(self):
        """
        Define colormap 'orange_RWTH_discrete'.
        """
        clrs = ['#F6A800', '#FABE50', '#FDD48F', '#FEEAC9', '#FFF7EA']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def orange_RWTH(self):
        """
        Define colormap 'orange_RWTH'.
        """
        clrs = ['#F6A800', '#FABE50', '#FDD48F', '#FEEAC9', '#FFF7EA']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def red_RWTH_discrete(self):
        """
        Define colormap 'red_RWTH_discrete'.
        """
        clrs = ['#CC071E', '#D85C41', '#E69679', '#F3CDBB', '#FAEBE3']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def red_RWTH(self):
        """
        Define colormap 'red_RWTH'.
        """
        clrs = ['#CC071E', '#D85C41', '#E69679', '#F3CDBB', '#FAEBE3']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def bordeaux_RWTH_discrete(self):
        """
        Define colormap 'bordeaux_RWTH_discrete'.
        """
        clrs = ['#A11035', '#B65256', '#CD8B87', '#E5C5C0', '#F5E8E5']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def bordeaux_RWTH(self):
        """
        Define colormap 'bordeaux_RWTH'.
        """
        clrs = ['#A11035', '#B65256', '#CD8B87', '#E5C5C0', '#F5E8E5']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def violet_RWTH_discrete(self):
        """
        Define colormap 'violet_RWTH_discrete'.
        """
        clrs = ['#612158', '#834E75', '#A8859E', '#D2C0CD', '#EDE5EA']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def violet_RWTH(self):
        """
        Define colormap 'violet_RWTH'.
        """
        clrs = ['#612158', '#834E75', '#A8859E', '#D2C0CD', '#EDE5EA']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def purple_RWTH_discrete(self):
        """
        Define colormap 'purple_RWTH_discrete'.
        """
        clrs = ['#7A6FAC', '#9B91C1', '#BCB5D7', '#DEDAEB', '#F2F0F7']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def purple_RWTH(self):
        """
        Define colormap 'purple_RWTH'.
        """
        clrs = ['#7A6FAC', '#9B91C1', '#BCB5D7', '#DEDAEB', '#F2F0F7']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def continuous_RWTH_discrete(self, lut=None):
        """
        Define colormap 'continuous_RWTH_discrete'.
        """
        clrs = ['#00549F', '#000000', '#E30066', '#FFED00', '#006165',
                '#0098A1', '#57AB27', '#BDCD00', '#F6A800', '#CC071E',
                '#A11035', '#612158', '#7A6FAC',
                '#407FB7', '#646567', '#E96088', '#FFF055', '#2D7F83',
                '#00B1B7', '#8DC060', '#D0D95C', '#FABE50', '#D85C41',
                '#B65256', '#834E75', '#9B91C1',
                '#8EBAE5', '#9C9E9F', '#F19EB1', '#FFF59B', '#7DA4A7',
                '#89CCCF', '#B8D698', '#E0E69A', '#FDD48F', '#E69679',
                '#CD8B87', '#A8859E', '#BCB5D7',
                '#C7DDF2', '#CFD1D2', '#F9D2DA', '#FFFAD1', '#BFD0D1',
                '#CAE7E7', '#DDEBCE', '#F0F3D0', '#FEEAC9', '#F3CDBB',
                '#E5C5C0', '#D2C0CD', '#DEDAEB',
                '#E8F1FA', '#ECEDED', '#FDEEF0', '#FFFDEE', '#E6ECEC',
                '#EBF6F6', '#F2F7EC', '#F9FAED', '#FFF7EA', '#FAEBE3',
                '#F5E8E5', '#EDE5EA', '#F2F0F7'
                ]
        indexes = []
        for i in range(5):
            indexes.append([i * 13 for i in range(i + 1)])
        for j in range(12):
            for i in range(5):
                indexes.append(copy.deepcopy(indexes[-1]))
                indexes[-1].append(i * 13 + (j + 1))
        if lut is None or lut < 1 or lut > (13 * 5):
            lut = 23
        self.cmap = discretemap(self.cname, [clrs[i] for i in indexes[lut - 1]])
        if lut == 23:
            self.cmap.set_bad('#777777')
        else:
            self.cmap.set_bad('#FFFFFF')

    def rolling_RWTH_discrete(self, lut=None):
        """
        Define colormap 'rolling_RWTH_discrete'.
        """
        clrs = ['#00549F', '#000000', '#E30066', '#FFED00', '#006165',
                '#0098A1', '#57AB27', '#BDCD00', '#F6A800', '#CC071E',
                '#A11035', '#612158', '#7A6FAC',
                '#407FB7', '#646567', '#E96088', '#FFF055', '#2D7F83',
                '#00B1B7', '#8DC060', '#D0D95C', '#FABE50', '#D85C41',
                '#B65256', '#834E75', '#9B91C1',
                '#8EBAE5', '#9C9E9F', '#F19EB1', '#FFF59B', '#7DA4A7',
                '#89CCCF', '#B8D698', '#E0E69A', '#FDD48F', '#E69679',
                '#CD8B87', '#A8859E', '#BCB5D7',
                '#C7DDF2', '#CFD1D2', '#F9D2DA', '#FFFAD1', '#BFD0D1',
                '#CAE7E7', '#DDEBCE', '#F0F3D0', '#FEEAC9', '#F3CDBB',
                '#E5C5C0', '#D2C0CD', '#DEDAEB',
                '#E8F1FA', '#ECEDED', '#FDEEF0', '#FFFDEE', '#E6ECEC',
                '#EBF6F6', '#F2F7EC', '#F9FAED', '#FFF7EA', '#FAEBE3',
                '#F5E8E5', '#EDE5EA', '#F2F0F7'
                ]
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def extended_RWTH_discrete(self, lut=None):
        """
        Define colormap 'extended_RWTH_discrete'.
        """
        clrs = ['#00549F', '#000000', '#E30066', '#FFED00', '#006165',
                '#0098A1', '#57AB27', '#BDCD00', '#F6A800', '#CC071E',
                '#A11035', '#612158', '#7A6FAC',
                '#407FB7', '#646567', '#E96088', '#FFF055', '#2D7F83',
                '#00B1B7', '#8DC060', '#D0D95C', '#FABE50', '#D85C41',
                '#B65256', '#834E75', '#9B91C1',
                '#8EBAE5', '#9C9E9F', '#F19EB1', '#FFF59B', '#7DA4A7',
                '#89CCCF', '#B8D698', '#E0E69A', '#FDD48F', '#E69679',
                '#CD8B87', '#A8859E', '#BCB5D7',
                '#C7DDF2', '#CFD1D2', '#F9D2DA', '#FFFAD1', '#BFD0D1',
                '#CAE7E7', '#DDEBCE', '#F0F3D0', '#FEEAC9', '#F3CDBB',
                '#E5C5C0', '#D2C0CD', '#DEDAEB',
                '#E8F1FA', '#ECEDED', '#FDEEF0', '#FFFDEE', '#E6ECEC',
                '#EBF6F6', '#F2F7EC', '#F9FAED', '#FFF7EA', '#FAEBE3',
                '#F5E8E5', '#EDE5EA', '#F2F0F7'
                ]
        indexes = []
        for i in range(13):
            indexes.append([i for i in range(i + 1)])
        for j in range(4):
            for i in range(13):
                indexes.append(copy.deepcopy(indexes[-1]))
                indexes[-1].insert((i * 2 + 1 + j), (j * 13 + i + 13))
        if lut is None or lut < 1 or lut > (13 * 5):
            lut = 23
        self.cmap = discretemap(self.cname, [clrs[i] for i in indexes[lut - 1]])
        if lut == 23:
            self.cmap.set_bad('#777777')
        else:
            self.cmap.set_bad('#FFFFFF')

    def divergent_RWTH(self):
        """
        Define colormap 'rwth_divergent' for diverging data.
        """
        # Define the RWTH divergent color map
        divergent_rwth_colors = ['#00549f', '#37628f', '#4c7080', '#5c7e73', '#6a8b67', '#77995b',
            '#86a650', '#96b345', '#a7bf3a', '#bbcc2e', '#d0d722', '#e6e213',
            '#fddd01', '#fbce04', '#f8be09', '#f5ae0e', '#f19e12', '#ed8e15',
            '#e87e17', '#e36d1a', '#de5c1b', '#d8481d', '#d2311d', '#cc071e'
        ]

        self.cmap = LinearSegmentedColormap.from_list(self.cname, divergent_rwth_colors)
        self.cmap.set_bad('#FFFFFF')

    def viridis_RWTH(self):
        """
        Define colormap 'viridis_RWTH' — RWTH-branded perceptual gradient.

        Colour stops: Violet (0%) → Turquoise (25%) → May Green (75%) → Yellow (100%).
        Inspired by RWTH-Colors (https://github.com/ifs-rwth-aachen/RWTH-Colors,
        MIT license, Philipp Simon Leibner at IFS RWTH Aachen).
        """
        clrs = [
            (0.00, '#612158'),  # violet 100 %
            (0.25, '#0098A1'),  # turquoise 100 %
            (0.75, '#BDCD00'),  # maygreen 100 %
            (1.00, '#FFED00'),  # yellow 100 %
        ]
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs, N=256)
        self.cmap.set_bad('#FFFFFF')

    def thermal_RWTH(self):
        """
        Define colormap 'thermal_RWTH' — blackbody-style thermal map.

        Colour scheme: black → bordeaux → red → orange → yellow → white.
        Mimics Planck radiation / incandescence; suitable for temperature or
        heat-flux visualisation.
        """
        clrs = [
            (0.00, '#000000'),  # black     — cold / zero
            (0.20, '#A11035'),  # bordeaux  — dark red
            (0.40, '#CC071E'),  # red
            (0.60, '#F6A800'),  # orange
            (0.80, '#FFED00'),  # yellow
            (1.00, '#FFFFFF'),  # white     — hot / maximum
        ]
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs, N=256)
        self.cmap.set_bad('#CCCCCC')

    def divergent_bm_RWTH(self):
        """
        Define colormap 'divergent_bm_RWTH' — blue–white–magenta diverging map.
        Useful for signed data (e.g. residuals, anomalies) where zero is meaningful.
        """
        clrs = [
            (0.00, '#00549F'),  # blue 100 %
            (0.25, '#8EBAE5'),  # blue 50 %
            (0.50, '#FFFFFF'),  # white (zero)
            (0.75, '#F19EB1'),  # magenta 50 %
            (1.00, '#E30066'),  # magenta 100 %
        ]
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs, N=256)
        self.cmap.set_bad('#CCCCCC')

    def divergent_gy_RWTH(self):
        """
        Define colormap 'divergent_gy_RWTH' — green–white–yellow diverging map.
        Alternative diverging palette using RWTH secondary colours.
        """
        clrs = [
            (0.00, '#57AB27'),  # green 100 %
            (0.25, '#B8D698'),  # green 50 %
            (0.50, '#FFFFFF'),  # white (zero)
            (0.75, '#FFF59B'),  # yellow 50 %
            (1.00, '#FFED00'),  # yellow 100 %
        ]
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs, N=256)
        self.cmap.set_bad('#CCCCCC')

    # ------------------------------------------------------------------
    # Power-system colormaps
    # ------------------------------------------------------------------

    def voltage_RWTH(self):
        """
        Define colormap 'voltage_RWTH' — symmetric map for voltage deviations.

        Colour scheme: red → orange → green (nominal) → orange → red.
        Use with a diverging norm centred at the nominal voltage (e.g. 1.0 pu).
        Values at the centre (0.5) map to RWTH green (nominal / good),
        values at the extremes map to RWTH red (over- or under-voltage).
        """
        clrs = [
            (0.00, '#CC071E'),  # red       — extreme under-voltage
            (0.25, '#F6A800'),  # orange
            (0.50, '#57AB27'),  # green     — nominal
            (0.75, '#F6A800'),  # orange
            (1.00, '#CC071E'),  # red       — extreme over-voltage
        ]
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs, N=256)
        self.cmap.set_bad('#CCCCCC')

    def loading_RWTH(self):
        """
        Define colormap 'loading_RWTH' — single-ended loading / congestion map.

        Colour scheme: blue (0 % loading) → yellow → red → bordeaux
        (≥ 100 %, overloaded).  Use for line or transformer loading indicators.
        """
        clrs = [
            (0.00, '#00549F'),  # blue         — unloaded / cold
            (0.38, '#E8F1F8'),  # RWTH blue 10%— bridge to prevent green cast in RGB space
            (0.60, '#FFED00'),  # yellow        — moderate load / caution
            (0.88, '#CC071E'),  # red           — at limit
            (1.00, '#A11035'),  # bordeaux      — overloaded
        ]
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs, N=256)
        self.cmap.set_bad('#CCCCCC')

    def show(self):
        """
        List names of defined colormaps.
        """
        print(' '.join(repr(n) for n in self.namelist))

    def get(self, cname='extended_RWTH_discrete', lut=None):
        """
        Return requested colormap, default is 'extended_RWTH_discrete'.
        """
        self.cname = cname
        if cname in ('extended_RWTH_discrete', 'continuous_RWTH_discrete'):
            self.funcdict[cname](lut)
        else:
            self.funcdict[cname]()
        return self.cmap


def rwth_cmap(colormap: str | None = None, lut: int | None = None) -> "LinearSegmentedColormap | tuple":
    """Return a Matplotlib colormap from the RWTH palette.

    All 41 RWTH colormaps are registered automatically on ``import rwthplots``,
    so they can also be accessed via ``plt.get_cmap('name')`` or
    ``plt.set_cmap('name')``.  Use this factory when you need a
    :class:`~matplotlib.colors.LinearSegmentedColormap` object directly, or
    when you want to set a custom ``lut`` for the multi-level discrete maps.

    Args:
        colormap: Name of the colormap to return.  Call ``rwth_cmap()`` with no
            arguments to get a tuple of all available names.  Falls back to
            ``'standard_RWTH_discrete'`` with a warning if the name is unknown.
        lut: Number of colours for ``extended_RWTH_discrete`` and
            ``continuous_RWTH_discrete`` (1–65).  Ignored for all other maps.

    Returns:
        LinearSegmentedColormap | tuple[str, ...]: Colormap instance, or all
            name strings as a tuple when called with no arguments.

    Examples:
        >>> from rwthplots.cmap import rwth_cmap
        >>> cmap = rwth_cmap("divergent_RWTH")
        >>> cmap = rwth_cmap("extended_RWTH_discrete", lut=8)
        >>> all_names = rwth_cmap()   # returns the full namelist tuple
    """
    obj = RWTHcmaps()
    if colormap is None:
        return obj.namelist
    if colormap not in obj.namelist:
        colormap = 'standard_RWTH_discrete'
        warnings.warn(
            f"Requested colormap not defined; known colormaps are {obj.namelist}. "
            f"Falling back to {colormap!r}.",
            stacklevel=2,
        )
    return obj.get(colormap, lut)


def rwth_cset(colorset: str | None = None, frmt: str = 'HEX') -> "tuple":
    """Return a named RWTH colour set for qualitative (categorical) data.

    The RWTH corporate design defines 13 base colours, each available at five
    tint levels (100 %, 75 %, 50 %, 25 %, 10 %).  This function returns the
    chosen tint level as a :func:`~collections.namedtuple` with one attribute
    per colour name, making the values easy to access by name
    (``cset.blue``, ``cset.orange``, etc.) or to iterate over.

    The 13 colours in order are:
    ``blue``, ``black``, ``magenta``, ``yellow``, ``petrol``,
    ``turquoise``, ``green``, ``maygreen``, ``orange``, ``red``,
    ``bordeaux``, ``violet``, ``purple``.

    Args:
        colorset: Tint level to return.  One of ``'rwth_100'``, ``'rwth_75'``,
            ``'rwth_50'``, ``'rwth_25'``, ``'rwth_10'``.  Pass ``None`` to get
            a tuple of all available names.  Falls back to ``'rwth_100'`` with
            a warning if the name is unknown.
        frmt: Output format for the colour values.

            * ``'HEX'`` *(default)* — ``'#RRGGBB'`` strings
            * ``'RGB'`` — ``(R, G, B)`` integer tuples (0–255)
            * ``'NRGB'`` — ``(R, G, B)`` float tuples (0.0–1.0)

    Returns:
        RWTHColorset: Namedtuple with 13 named colour attributes, or a tuple
            of available colorset names when called with ``colorset=None``.

    Examples:
        >>> from rwthplots.cmap import rwth_cset
        >>> cset = rwth_cset("rwth_100")
        >>> cset.blue
        '#00549F'
        >>> list(cset)          # all 13 colours as a list
        ['#00549F', '#000000', ...]
        >>> cset_rgb = rwth_cset("rwth_100", frmt="RGB")
        >>> cset_rgb.blue
        (0, 84, 159)
        >>> cset_nrgb = rwth_cset("rwth_75", frmt="NRGB")
        >>> cset_nrgb.orange    # (0.98..., 0.745..., 0.314...)
    """
    from collections import namedtuple

    namelist = ('rwth_100', 'rwth_75', 'rwth_50', 'rwth_25', 'rwth_10')
    if colorset is None:
        return namelist
    if colorset not in namelist:
        colorset = 'rwth_100'
        warnings.warn(
            f"Requested colorset not defined; known colorsets are {namelist}. "
            f"Falling back to {colorset!r}.",
            stacklevel=2,
        )
    if frmt not in ('HEX', 'RGB', 'NRGB'):
        raise ValueError(f"Unknown format {frmt!r}. Use 'HEX', 'RGB', or 'NRGB'.")

    if colorset == 'rwth_100':
        cset = namedtuple('RWTHColorset',
                          'blue black magenta yellow petrol turquoise green maygreen orange red bordeaux violet purple')
        cset = cset('#00549F', '#000000', '#E30066', '#FFED00', '#006165',
                    '#0098A1', '#57AB27', '#BDCD00', '#F6A800', '#CC071E',
                    '#A11035', '#612158', '#7A6FAC')

    elif colorset == 'rwth_75':
        cset = namedtuple('RWTHColorset',
                          'blue black magenta yellow petrol turquoise green maygreen orange red bordeaux violet purple')
        cset = cset('#407FB7', '#646567', '#E96088', '#FFF055', '#2D7F83',
                    '#00B1B7', '#8DC060', '#D0D95C', '#FABE50', '#D85C41',
                    '#B65256', '#834E75', '#9B91C1')

    elif colorset == 'rwth_50':
        cset = namedtuple('RWTHColorset',
                          'blue black magenta yellow petrol turquoise green maygreen orange red bordeaux violet purple')
        cset = cset('#8EBAE5', '#9C9E9F', '#F19EB1', '#FFF59B', '#7DA4A7',
                    '#89CCCF', '#B8D698', '#E0E69A', '#FDD48F', '#E69679',
                    '#CD8B87', '#A8859E', '#BCB5D7')

    elif colorset == 'rwth_25':
        cset = namedtuple('RWTHColorset',
                          'blue black magenta yellow petrol turquoise green maygreen orange red bordeaux violet purple')
        cset = cset('#C7DDF2', '#CFD1D2', '#F9D2DA', '#FFFAD1', '#BFD0D1',
                    '#CAE7E7', '#DDEBCE', '#F0F3D0', '#FEEAC9', '#F3CDBB',
                    '#E5C5C0', '#D2C0CD', '#DEDAEB')

    elif colorset == 'rwth_10':
        cset = namedtuple('RWTHColorset',
                          'blue black magenta yellow petrol turquoise green maygreen orange red bordeaux violet purple')
        cset = cset('#E8F1FA', '#ECEDED', '#FDEEF0', '#FFFDEE', '#E6ECEC',
                    '#EBF6F6', '#F2F7EC', '#F9FAED', '#FFF7EA', '#FAEBE3',
                    '#F5E8E5', '#EDE5EA', '#F2F0F7')

    if frmt == 'RGB':
        cset = cset._make(_hex_to_rgb(c) for c in cset)
    elif frmt == 'NRGB':
        cset = cset._make(_hex_to_nrgb(c) for c in cset)
    return cset


def plot_color_palette():
    """
    Display all 13 RWTH base colors across their five tint levels (100 %–10 %)
    as a matplotlib figure.

    Returns the :class:`matplotlib.figure.Figure` so the caller can save or show it.

    Inspired by ``ColorManager.plot_color_palette()`` in RWTH-Colors
    (https://github.com/ifs-rwth-aachen/RWTH-Colors, MIT license,
    Philipp Simon Leibner at IFS RWTH Aachen).
    """
    from matplotlib import pyplot as plt

    tints = ('rwth_100', 'rwth_75', 'rwth_50', 'rwth_25', 'rwth_10')
    tint_labels = ('100 %', '75 %', '50 %', '25 %', '10 %')
    color_names = rwth_cset('rwth_100')._fields  # 13 names

    n_colors = len(color_names)
    n_tints = len(tints)

    fig, axes = plt.subplots(n_tints, n_colors, figsize=(n_colors * 1.3, n_tints * 1.1))
    fig.subplots_adjust(hspace=0.04, wspace=0.04)

    for row, (tint, label) in enumerate(zip(tints, tint_labels)):
        cset = rwth_cset(tint)
        for col, (name, color) in enumerate(zip(color_names, cset)):
            ax = axes[row, col]
            ax.set_facecolor(color)
            ax.set_xticks([])
            ax.set_yticks([])
            for spine in ax.spines.values():
                spine.set_visible(False)
            r, g, b = _hex_to_rgb(color)
            text_color = '#000000' if (0.299 * r + 0.587 * g + 0.114 * b) > 128 else '#FFFFFF'
            ax.text(0.5, 0.5, color, ha='center', va='center',
                    fontsize=5.5, color=text_color, transform=ax.transAxes)
            if row == 0:
                ax.set_title(name, fontsize=7.5, pad=3)
            if col == 0:
                ax.set_ylabel(label, fontsize=7.5, rotation=0, labelpad=28, va='center')

    fig.suptitle('RWTH Aachen University Colour Palette', fontsize=9, y=1.01)
    return fig


def main():
    from matplotlib import pyplot as plt

    # Show colorsets rwth_cset(<scheme>).
    schemes = rwth_cset()
    fig, axes = plt.subplots(ncols=len(schemes), figsize=(9, 3.5))
    fig.subplots_adjust(top=0.9, bottom=0.02, left=0.02, right=0.92)
    for ax, scheme in zip(axes, schemes):
        cset = rwth_cset(scheme)
        names = cset._fields
        colors = list(cset)
        for name, color in zip(names, colors):
            ax.scatter([], [], c=color, s=80, label=name)
        ax.set_axis_off()
        ax.legend(loc=2)
        ax.set_title(scheme)
    plt.show()

    # Show colormaps rwth_cmap(<scheme>). 
    schemes = rwth_cmap()
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    fig, axes = plt.subplots(nrows=len(schemes))
    fig.subplots_adjust(top=0.98, bottom=0.02, left=0.2, right=0.99)
    for ax, scheme in zip(axes, schemes):
        pos = list(ax.get_position().bounds)
        ax.set_axis_off()
        ax.imshow(gradient, aspect=4, cmap=rwth_cmap(scheme))
        fig.text(pos[0] - 0.01, pos[1] + pos[3] / 2., scheme, va='center', ha='right', fontsize=10)
    plt.show()

    # Show colormaps rwth_cmap('continous_RWTH_discrete', <lut>). 
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    fig, axes = plt.subplots(nrows=13 * 5)
    fig.subplots_adjust(top=0.98, bottom=0.02, left=0.25, right=0.99)
    for lut, ax in enumerate(axes, start=1):
        pos = list(ax.get_position().bounds)
        ax.set_axis_off()
        ax.imshow(gradient, aspect=4, cmap=rwth_cmap('continuous_RWTH_discrete', lut))
        fig.text(pos[0] - 0.01, pos[1] + pos[3] / 2., 'continuous_RWTH_discrete, ' + str(lut),
                 va='center', ha='right', fontsize=8)
    plt.show()

    # Show colormaps rwth_cmap('extended_RWTH_discrete', <lut>). 
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    fig, axes = plt.subplots(nrows=13 * 5)
    fig.subplots_adjust(top=0.98, bottom=0.02, left=0.25, right=0.99)
    for lut, ax in enumerate(axes, start=1):
        pos = list(ax.get_position().bounds)
        ax.set_axis_off()
        ax.imshow(gradient, aspect=4, cmap=rwth_cmap('extended_RWTH_discrete', lut))
        fig.text(pos[0] - 0.01, pos[1] + pos[3] / 2., 'extended_RWTH_discrete, ' + str(lut),
                 va='center', ha='right', fontsize=8)
    plt.show()


if __name__ == '__main__':
    main()

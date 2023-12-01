#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition of RWTH standard theme for plotting.

# Installation via
 > pip install .

# to check successful installation run python console
 > import matplotlib.pyplot as plt
 > plt.style.available

# for simple usage run in python console
 > import matplotlib.pyplot as plt
 > plt.style.use('rwth-latex')

# release note: certain characters need special escaping such as
$ % & ~ ^ \ { } \( \) \[ \]

# Temporary styling add to python scripr or run in python console
 > with plt.style.context('dark_background'):
 >   plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
 > plt.show()

all credits go out to John D. Garret https://github.com/garrettj403/SciencePlots

High Voltage Equipment and Grids, Digitalization and Energy Economics (IAEW)
(c) 2022, Steffen Kortmann
"""
import atexit
import glob
import os
import shutil

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


def install_styles():
    """Post-installation script to install styles defined in the /styles folder"""

    # import matplotlib inside function to avoid import error during installation initialization
    import matplotlib

    # Find all style files
    style_files = glob.glob('styles/**/*.mplstyle', recursive=True)

    # Find stylelib directory (where the *.mplstyle files go)
    print("Your style sheets are located at: {}".format(
        os.path.join(matplotlib.__path__[0], 'mpl-data', 'stylelib')))
    mpl_style_lib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_style_lib_dir):
        os.makedirs(mpl_style_lib_dir)

    # Copy files over
    print("Installing styles into", mpl_style_lib_dir)
    for style_file in style_files:
        print(os.path.basename(style_file))
        shutil.copy(style_file, os.path.join(mpl_style_lib_dir, os.path.basename(style_file)))


class PostInstallMoveFile(install):
    """Post-installation class to run the installation script"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)


class PostInstallDevMoveFile(develop):
    """Post-installation in develop (editable) mode class to run the installation script"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)


# Get description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='RWTHPlots',
    version='1.0.1',
    author="Steffen Kortmann",
    author_email="steffen.kortmann@rwth-aachen.de",
    description="Adding standard themes with RWTH Aachen University colours to matplotlib",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    keywords=[
        "matplotlib-style-sheets",
        "matplotlib-figures",
        "scientific-papers",
        "thesis-template",
        "matplotlib-styles",
        "python"
    ],
    url="https://github.com/skortmann/RWTHPlots",
    install_requires=['matplotlib', ],
    cmdclass={'install': PostInstallMoveFile,
              'develop': PostInstallDevMoveFile},
)

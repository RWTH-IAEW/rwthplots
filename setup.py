import atexit
import glob
import os
import shutil
import subprocess
from setuptools import setup
from setuptools.command.install import install

def install_styles():
    import matplotlib
    style_files = glob.glob('RWTHPlots/styles/**/*.mplstyle', recursive=True)
    mpl_style_lib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_style_lib_dir):
        os.makedirs(mpl_style_lib_dir)
    for style_file in style_files:
        shutil.copy(style_file, os.path.join(mpl_style_lib_dir, os.path.basename(style_file)))

class PostInstallMoveFile(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(self.run_post_install_tasks)

    def run_post_install_tasks(self):
        install_styles()

root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='RWTHPlots',
    version='2.3.0',
    author="Steffen Kortmann, Florian Schmidtke",
    author_email="s.kortmann@iaew.rwth-aachen.de, f.schmidtke@iaew.rwth-aachen.de",
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
    install_requires=['matplotlib', 'rwth-CD-colors'],
    packages=['RWTHPlots'],
    cmdclass={'install': PostInstallMoveFile, }
)

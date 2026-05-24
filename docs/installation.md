# Installation

Requires **Python ≥ 3.10** and **Matplotlib ≥ 3.10**.

## From GitLab (recommended)

```sh
pip install git+https://gitlab.iaew.rwth-aachen.de/aev/RWTHPlots.git
```

## Editable install for development

```sh
git clone https://gitlab.iaew.rwth-aachen.de/aev/RWTHPlots.git
cd RWTHPlots
uv pip install -e .
```

## With development dependencies

```sh
uv sync --group dev
```

This installs pytest, coverage, and the MkDocs documentation toolchain.

## Verifying the install

```python
import rwthplots
print(rwthplots.__version__)   # e.g. 3.1.0
```

On import, rwthplots automatically:

- registers all 41 RWTH colormaps with Matplotlib
- injects all `.mplstyle` files into `plt.style.library` so they are
  addressable as `rwthplots.styles.<name>`

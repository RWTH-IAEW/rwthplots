import rwthplots
import matplotlib
import matplotlib.pyplot as plt

import pytest
from pathlib import Path


@pytest.mark.parametrize("style", ["rwth-latex", "rwth-word"])
def test_style_use(style):
    """Test to set and use style"""

    # load during installation registered installation
    plt.style.use(f"rwthplots.styles.{style}")
    rc_params = matplotlib.RcParams

    # load and register from style file during runtime
    style_path = Path(__file__).parents[1] / "rwthplots" / "styles"
    plt.style.use(style_path / f"{style}.mplstyle")
    rc_params_compare = matplotlib.RcParams

    assert rc_params == rc_params_compare

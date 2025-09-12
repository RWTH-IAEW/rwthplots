from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
import pytest

@pytest.mark.parametrize("style", ["rwth-latex", "rwth-word"])
def test_style_use(style):
    """Style loaded via dotted name and via file path must produce identical rcParams."""

    # 1) load via dotted package style
    plt.style.use(f"rwthplots.styles.{style}")
    rc_params_pkg = matplotlib.rcParams.copy()

    # 2) load via direct file path from the repo (src-layout!)
    style_path = Path(__file__).parents[1] / "src" / "rwthplots" / "styles" / f"{style}.mplstyle"
    plt.style.use(style_path)
    rc_params_file = matplotlib.rcParams.copy()

    assert rc_params_pkg == rc_params_file

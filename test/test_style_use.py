from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
import pytest

# Styles that do not require a LaTeX installation for rcParam comparison.
# (text.usetex=True is just an rcParam; actual LaTeX rendering is not triggered.)
STYLES = ["rwth-latex", "rwth-word", "rwth-pptx", "rwth-latex-pptx", "rwth-custom"]


@pytest.mark.parametrize("style", STYLES)
def test_style_use(style):
    """Style loaded via dotted name and via file path must produce identical rcParams."""
    styles_dir = Path(__file__).parents[1] / "src" / "rwthplots" / "styles"

    plt.style.use(f"rwthplots.styles.{style}")
    rc_params_pkg = matplotlib.rcParams.copy()

    plt.style.use(styles_dir / f"{style}.mplstyle")
    rc_params_file = matplotlib.rcParams.copy()

    assert rc_params_pkg == rc_params_file


@pytest.mark.parametrize("subdir,style", [
    ("color", "blue"),
    ("color", "red"),
    ("color", "extended"),
    ("misc", "grid"),
    ("misc", "no-latex"),
    ("journals", "ieee"),
])
def test_subdir_style_use(subdir, style):
    """Subdirectory styles loaded via dotted name and file path must match."""
    styles_dir = Path(__file__).parents[1] / "src" / "rwthplots" / "styles"

    plt.style.use(f"rwthplots.styles.{subdir}.{style}")
    rc_params_pkg = matplotlib.rcParams.copy()

    plt.style.use(styles_dir / subdir / f"{style}.mplstyle")
    rc_params_file = matplotlib.rcParams.copy()

    assert rc_params_pkg == rc_params_file

import os
import pytest
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import rwthplots
from rwthplots.utils import save_figure, context, check_accessibility, pick_colors
from rwthplots.cmap import rwth_cset


# ---------------------------------------------------------------------------
# save_figure
# ---------------------------------------------------------------------------

def test_save_figure_creates_files(tmp_path):
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    save_figure(fig, tmp_path / "test_out", formats=["png", "pdf"])
    assert (tmp_path / "test_out.png").exists()
    assert (tmp_path / "test_out.pdf").exists()
    plt.close(fig)


def test_save_figure_creates_parent_dirs(tmp_path):
    fig, ax = plt.subplots()
    out = tmp_path / "a" / "b" / "c" / "plot"
    save_figure(fig, out, formats=["png"])
    assert out.with_suffix(".png").exists()
    plt.close(fig)


def test_save_figure_dpi_applied(tmp_path):
    fig, ax = plt.subplots()
    ax.plot([0], [0])
    save_figure(fig, tmp_path / "hi_res", formats=["png"], dpi=150)
    assert (tmp_path / "hi_res.png").exists()
    plt.close(fig)


def test_save_figure_svg(tmp_path):
    fig, ax = plt.subplots()
    save_figure(fig, tmp_path / "vector", formats=["svg"])
    assert (tmp_path / "vector.svg").exists()
    plt.close(fig)


# ---------------------------------------------------------------------------
# context
# ---------------------------------------------------------------------------

def test_context_short_name():
    with rwthplots.context("rwth-word"):
        assert plt.rcParams["font.family"] == ["sans-serif"]


def test_context_dotted_name():
    with rwthplots.context("color.blue"):
        cycle_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
        assert len(cycle_colors) > 0


def test_context_multiple_styles():
    with rwthplots.context("rwth-word", "misc.grid"):
        assert plt.rcParams["axes.grid"] is True


def test_context_full_name_passthrough():
    with rwthplots.context("rwthplots.styles.rwth-word"):
        assert plt.rcParams["font.family"] == ["sans-serif"]


def test_context_restores_rcparams():
    original_figsize = tuple(plt.rcParams["figure.figsize"])
    with rwthplots.context("rwth-word"):
        pass
    assert tuple(plt.rcParams["figure.figsize"]) == original_figsize


# ---------------------------------------------------------------------------
# check_accessibility
# ---------------------------------------------------------------------------

def test_check_accessibility_returns_list():
    colors = list(rwth_cset("rwth_100"))
    result = check_accessibility(colors)
    assert isinstance(result, list)


def test_check_accessibility_issue_keys():
    # Red/green are confused under deuteranopia (delta-E ≈ 18), so use threshold=20
    colors = ["#FF0000", "#00FF00"]
    issues = check_accessibility(colors, types=["deuteranopia"], threshold=20.0)
    assert len(issues) > 0
    issue = issues[0]
    assert set(issue.keys()) == {"cvd_type", "color_a", "color_b", "delta_e"}


def test_check_accessibility_safe_pair():
    # Pure blue and pure yellow are safe under deuteranopia/protanopia
    issues = check_accessibility(
        ["#0000FF", "#FFFF00"],
        types=["deuteranopia", "protanopia"],
        threshold=10.0,
    )
    assert len(issues) == 0


def test_check_accessibility_all_cvd_types():
    colors = ["#FF0000", "#00FF00", "#0000FF"]
    result = check_accessibility(colors, types=["deuteranopia", "protanopia", "tritanopia"])
    assert isinstance(result, list)


def test_check_accessibility_invalid_type():
    with pytest.raises(ValueError, match="Unknown CVD type"):
        check_accessibility(["#00549F"], types=["imaginary_cvd"])


def test_check_accessibility_threshold():
    colors = list(rwth_cset("rwth_100"))
    issues_strict = check_accessibility(colors, threshold=50.0)
    issues_loose = check_accessibility(colors, threshold=5.0)
    assert len(issues_strict) >= len(issues_loose)


# ---------------------------------------------------------------------------
# pick_colors
# ---------------------------------------------------------------------------

def test_pick_colors_returns_n(n=4):
    colors = pick_colors(n)
    assert len(colors) == n


def test_pick_colors_all_hex():
    colors = pick_colors(6)
    for c in colors:
        assert c.startswith("#") and len(c) == 7


def test_pick_colors_from_rwth_palette():
    full = list(rwth_cset("rwth_100"))
    colors = pick_colors(4)
    for c in colors:
        assert c in full


def test_pick_colors_n1_is_blue():
    colors = pick_colors(1)
    assert colors[0] == "#00549F"  # blue is the starting seed


def test_pick_colors_all_13():
    colors = pick_colors(13)
    assert len(colors) == 13
    assert len(set(colors)) == 13  # all distinct


def test_pick_colors_invalid_n():
    with pytest.raises(ValueError, match="n must be between"):
        pick_colors(0)
    with pytest.raises(ValueError, match="n must be between"):
        pick_colors(14)


@pytest.mark.parametrize("n", [1, 2, 4, 7, 13])
def test_pick_colors_various_n(n):
    colors = pick_colors(n)
    assert len(colors) == n

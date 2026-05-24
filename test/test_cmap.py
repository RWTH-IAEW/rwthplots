import numpy as np
import pytest
import matplotlib.pyplot as plt
import rwthplots
from rwthplots.cmap import RWTHcmaps, rwth_cmap, plot_color_palette


ALL_COLORMAPS = RWTHcmaps().namelist


@pytest.mark.parametrize("cmap_name", ALL_COLORMAPS)
def test_cmap_registered(cmap_name):
    """Every RWTH colormap must be registered with Matplotlib on package import."""
    plt.set_cmap(cmap_name)
    assert plt.get_cmap().name == cmap_name


@pytest.mark.parametrize("cmap_name", ALL_COLORMAPS)
def test_rwth_cmap_factory(cmap_name):
    """rwth_cmap() must return a valid colormap for every name."""
    cmap = rwth_cmap(cmap_name)
    assert cmap is not None
    assert cmap.name == cmap_name


def test_rwth_cmap_no_arg_returns_namelist():
    result = rwth_cmap()
    assert isinstance(result, tuple)
    assert len(result) > 0


def test_rwth_cmap_invalid_name_falls_back():
    cmap = rwth_cmap("nonexistent_cmap_xyz")
    assert cmap is not None


@pytest.mark.parametrize("lut", [1, 10, 23, 65])
def test_rwth_cmap_extended_lut(lut):
    cmap = rwth_cmap("extended_RWTH_discrete", lut=lut)
    assert cmap is not None


@pytest.mark.parametrize("lut", [1, 10, 23, 65])
def test_rwth_cmap_continuous_lut(lut):
    cmap = rwth_cmap("continuous_RWTH_discrete", lut=lut)
    assert cmap is not None


def test_rwth_cmap_continuous_lut_produces_different_maps():
    """lut=1 and lut=10 must yield distinct colormaps (catches silent lut-drop bug)."""
    cmap1 = rwth_cmap("continuous_RWTH_discrete", lut=1)
    cmap10 = rwth_cmap("continuous_RWTH_discrete", lut=10)
    sample = np.linspace(0, 1, 8)
    assert not np.allclose(cmap1(sample), cmap10(sample))


def test_viridis_rwth_registered():
    plt.set_cmap("viridis_RWTH")
    assert plt.get_cmap().name == "viridis_RWTH"


def test_viridis_rwth_is_smooth():
    """viridis_RWTH must interpolate — adjacent samples should differ."""
    cmap = rwth_cmap("viridis_RWTH")
    sample = np.linspace(0, 1, 64)
    rgba = cmap(sample)
    assert not np.allclose(rgba[0], rgba[-1])


def test_plot_color_palette_returns_figure():
    fig = plot_color_palette()
    assert fig is not None
    assert hasattr(fig, 'savefig')
    plt.close(fig)


def test_plot_color_palette_has_correct_axes():
    """5 tint rows × 13 color columns = 65 axes."""
    fig = plot_color_palette()
    assert len(fig.axes) == 65
    plt.close(fig)

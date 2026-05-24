import pytest
from rwthplots.cmap import rwth_cset


ALL_CSETS = ("rwth_100", "rwth_75", "rwth_50", "rwth_25", "rwth_10")
EXPECTED_FIELDS = (
    "blue", "black", "magenta", "yellow", "petrol",
    "turquoise", "green", "maygreen", "orange", "red",
    "bordeaux", "violet", "purple",
)


def test_rwth_cset_no_arg_returns_names():
    result = rwth_cset()
    assert isinstance(result, tuple)
    assert set(result) == set(ALL_CSETS)


@pytest.mark.parametrize("cset_name", ALL_CSETS)
def test_rwth_cset_fields(cset_name):
    cset = rwth_cset(cset_name)
    assert cset._fields == EXPECTED_FIELDS


@pytest.mark.parametrize("cset_name", ALL_CSETS)
def test_rwth_cset_length(cset_name):
    cset = rwth_cset(cset_name)
    assert len(list(cset)) == 13


@pytest.mark.parametrize("cset_name", ALL_CSETS)
def test_rwth_cset_hex_colors(cset_name):
    cset = rwth_cset(cset_name)
    for color in list(cset):
        assert color.startswith("#"), f"{color!r} is not a hex color"
        assert len(color) == 7, f"{color!r} is not #RRGGBB"


def test_rwth_cset_invalid_name_falls_back_to_rwth_100():
    cset = rwth_cset("nonexistent_cset_xyz")
    assert cset is not None
    assert cset._fields == EXPECTED_FIELDS  # must be rwth_100 fallback


@pytest.mark.parametrize("cset_name", ALL_CSETS)
def test_rwth_cset_type_name(cset_name):
    """All tint levels must use the consistent 'RWTHColorset' namedtuple type name."""
    cset = rwth_cset(cset_name)
    assert type(cset).__name__ == "RWTHColorset"


# --- frmt parameter tests ---------------------------------------------------

@pytest.mark.parametrize("cset_name", ALL_CSETS)
def test_rwth_cset_frmt_hex(cset_name):
    cset = rwth_cset(cset_name, frmt='HEX')
    for color in list(cset):
        assert color.startswith("#") and len(color) == 7


@pytest.mark.parametrize("cset_name", ALL_CSETS)
def test_rwth_cset_frmt_rgb(cset_name):
    cset = rwth_cset(cset_name, frmt='RGB')
    for color in list(cset):
        assert isinstance(color, tuple) and len(color) == 3
        assert all(isinstance(v, int) and 0 <= v <= 255 for v in color)


@pytest.mark.parametrize("cset_name", ALL_CSETS)
def test_rwth_cset_frmt_nrgb(cset_name):
    cset = rwth_cset(cset_name, frmt='NRGB')
    for color in list(cset):
        assert isinstance(color, tuple) and len(color) == 3
        assert all(isinstance(v, float) and 0.0 <= v <= 1.0 for v in color)


def test_rwth_cset_frmt_rgb_known_value():
    cset = rwth_cset('rwth_100', frmt='RGB')
    assert cset.blue == (0, 84, 159)  # #00549F


def test_rwth_cset_frmt_nrgb_known_value():
    cset = rwth_cset('rwth_100', frmt='NRGB')
    r, g, b = cset.blue
    assert abs(r - 0.0) < 1e-6
    assert abs(g - 84 / 255) < 1e-6
    assert abs(b - 159 / 255) < 1e-6


def test_rwth_cset_frmt_invalid_raises():
    with pytest.raises(ValueError, match="Unknown format"):
        rwth_cset('rwth_100', frmt='XYZ')

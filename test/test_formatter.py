import pytest
from rwthplots.formatter import set_size, list_presets

GOLDEN_RATIO = (5 ** 0.5 - 1) / 2


def test_numeric_width_positive_dimensions():
    w, h = set_size(100)
    assert w > 0
    assert h > 0


def test_numeric_width_golden_ratio():
    w, h = set_size(100)
    assert abs(h / w - GOLDEN_RATIO) < 1e-9


@pytest.mark.parametrize("name", ["thesis", "beamer-full", "beamer-half"])
def test_predefined_widths(name):
    w, h = set_size(name)
    assert w > 0
    assert h > 0


def test_beamer_half_narrower_than_full():
    w_full, _ = set_size("beamer-full")
    w_half, _ = set_size("beamer-half")
    assert w_half < w_full


def test_fraction_scales_width():
    w1, _ = set_size(200, fraction=1.0)
    w_half, _ = set_size(200, fraction=0.5)
    assert abs(w1 / w_half - 2.0) < 1e-9


def test_subplots_two_rows_taller():
    _, h1 = set_size(200, subplots=(1, 1))
    _, h2 = set_size(200, subplots=(2, 1))
    assert h2 > h1


def test_subplots_two_cols_shorter():
    _, h1 = set_size(200, subplots=(1, 1))
    _, h2 = set_size(200, subplots=(1, 2))
    assert h2 < h1


def test_unknown_string_raises_value_error():
    with pytest.raises(ValueError, match="Unknown predefined width"):
        set_size("a5")


NEW_PRESETS = [
    "a4", "a4-half", "letter", "letter-half",
    "ieee-column", "ieee-page",
    "nature-column", "nature-page",
    "science-column",
    "elsevier-column", "elsevier-page",
    "springer-column",
    "aps-column", "aps-page",
    "acm-column",
]


@pytest.mark.parametrize("name", NEW_PRESETS)
def test_new_presets_positive_dimensions(name):
    w, h = set_size(name)
    assert w > 0 and h > 0


def test_ieee_column_narrower_than_ieee_page():
    w_col, _ = set_size("ieee-column")
    w_page, _ = set_size("ieee-page")
    assert w_col < w_page


def test_list_presets_returns_dict():
    presets = list_presets()
    assert isinstance(presets, dict)
    assert "thesis" in presets
    assert "ieee-column" in presets
    assert all(v > 0 for v in presets.values())

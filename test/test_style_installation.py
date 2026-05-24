import matplotlib.pyplot as plt
import pytest

BASE_STYLES = [
    "rwthplots.styles.rwth-latex",
    "rwthplots.styles.rwth-word",
    "rwthplots.styles.rwth-pptx",
    "rwthplots.styles.rwth-latex-pptx",
    "rwthplots.styles.rwth-latex-beamer",
    "rwthplots.styles.rwth-latex-beamer-fira",
    "rwthplots.styles.rwth-custom",
    "rwthplots.styles.rwth-dark",
]

COLOR_STYLES = [
    "rwthplots.styles.color.black",
    "rwthplots.styles.color.blue",
    "rwthplots.styles.color.bordeaux",
    "rwthplots.styles.color.divergent",
    "rwthplots.styles.color.extended",
    "rwthplots.styles.color.green",
    "rwthplots.styles.color.magenta",
    "rwthplots.styles.color.maygreen",
    "rwthplots.styles.color.orange",
    "rwthplots.styles.color.petrol",
    "rwthplots.styles.color.purple",
    "rwthplots.styles.color.red",
    "rwthplots.styles.color.standard",
    "rwthplots.styles.color.turquoise",
    "rwthplots.styles.color.violett",
    "rwthplots.styles.color.yellow",
]

MISC_STYLES = [
    "rwthplots.styles.misc.colorblind",
    "rwthplots.styles.misc.grid",
    "rwthplots.styles.misc.latex-sans",
    "rwthplots.styles.misc.no-latex",
    "rwthplots.styles.misc.pgf",
    "rwthplots.styles.misc.sans",
]

JOURNAL_STYLES = [
    "rwthplots.styles.journals.acm",
    "rwthplots.styles.journals.aps",
    "rwthplots.styles.journals.elsevier",
    "rwthplots.styles.journals.ieee",
    "rwthplots.styles.journals.nature",
    "rwthplots.styles.journals.springer",
]

SIZE_STYLES = [
    "rwthplots.styles.size.a4",
    "rwthplots.styles.size.a4-half",
    "rwthplots.styles.size.letter",
    "rwthplots.styles.size.letter-half",
    "rwthplots.styles.size.ieee-column",
    "rwthplots.styles.size.ieee-page",
    "rwthplots.styles.size.nature-column",
    "rwthplots.styles.size.nature-page",
    "rwthplots.styles.size.science-column",
    "rwthplots.styles.size.elsevier-column",
    "rwthplots.styles.size.elsevier-page",
    "rwthplots.styles.size.springer-column",
    "rwthplots.styles.size.aps-column",
    "rwthplots.styles.size.aps-page",
    "rwthplots.styles.size.acm-column",
]

ALL_STYLES = BASE_STYLES + COLOR_STYLES + MISC_STYLES + JOURNAL_STYLES + SIZE_STYLES


@pytest.mark.parametrize("style", ALL_STYLES)
def test_style_loads(style):
    """Every style must load via its fully-qualified dotted name."""
    plt.style.use(style)


def test_styles_in_available_after_import():
    """After 'import rwthplots', all styles must appear in plt.style.available."""
    import rwthplots  # noqa: F401
    for style in ALL_STYLES:
        assert style in plt.style.available, f"{style!r} missing from plt.style.available"


def test_style_combination_base_and_color():
    plt.style.use(["rwthplots.styles.rwth-word", "rwthplots.styles.color.blue"])


def test_style_combination_base_and_misc():
    plt.style.use(["rwthplots.styles.rwth-word", "rwthplots.styles.misc.grid"])


def test_style_combination_base_color_misc():
    plt.style.use([
        "rwthplots.styles.rwth-word",
        "rwthplots.styles.color.orange",
        "rwthplots.styles.misc.no-latex",
    ])

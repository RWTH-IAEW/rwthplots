# test/test_style_installation.py
import matplotlib.pyplot as plt
import pytest

@pytest.mark.parametrize("style", [
    "rwthplots.styles.rwth-latex",
    "rwthplots.styles.rwth-word",
])
def test_installed_style(style):
    # Should load without raising
    plt.style.use(style)

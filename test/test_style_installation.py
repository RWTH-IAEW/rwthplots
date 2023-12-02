import matplotlib.pyplot as plt
import pytest


@pytest.mark.parametrize("style", ["rwth-latex", "rwth-word"])
def test_installed_style(style):
    installed_styles = plt.style.available

    assert "rwth-latex" in installed_styles

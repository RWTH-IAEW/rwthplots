import RWTHPlots
import matplotlib.pyplot as plt

import pytest


@pytest.mark.parametrize("color_map_name", ['extended_RWTH_discrete',
                                            'blue_RWTH_discrete',
                                            'black_RWTH_discrete',
                                            'rolling_RWTH_discrete',
                                            'green_RWTH_discrete'])
def test_cmap_rwth_cmap(color_map_name):
    """Test to initialize the rwth_cmap"""

    plt.set_cmap(color_map_name)

    assert color_map_name == plt.get_cmap().name

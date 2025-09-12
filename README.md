# Colormap with RWTH colors for Matplotlib
Adding RWTH Aachen University’s corporate design colors and ready-to-use Matplotlib style sheets (Word/LaTeX/PowerPoint).

## Getting Started

These are the corporate design colors at RWTH Aachen University.

# Installation via

* (simplest) pip install from gitlab (requires gitlab credentials
    * open terminal
    ```sh
    pip install git+https://gitlab.iaew.rwth-aachen.de/aev/RWTHPlots.git
    ```

* (also ok) clone folder from gitlab and navigate to the repository then
  * open terminal
    ```sh
    git clone https://gitlab.iaew.rwth-aachen.de/aev/RWTHPlots.git
    cd RWTHPlots
    uv pip install -e .
      ```

* (advanced) alternatively using a ssh-key
  * open terminal
    ```sh
    pip install git+ssh://git@gitlab.iaew.rwth-aachen.de/aev/RWTHPlots.git
    ``` 

Finally open python console to check succesful installation

```python
import matplotlib.pyplot as plt

# List installed styles
print([s for s in plt.style.available if s.startswith("rwthplots")])

# Use RWTH LaTeX style
plt.style.use("rwthplots.styles.rwth-latex")

# Or RWTH Word style
plt.style.use("rwthplots.styles.rwth-word")
```

## Usage
```python
from rwthplots.cmap import rwth_cmap
import matplotlib.pyplot as plt
import matplotlib

# Register and use extended RWTH discrete colormap
matplotlib.colormaps.register(rwth_cmap("extended_RWTH_discrete"))
plt.set_cmap("extended_RWTH_discrete")
```

## Styles

rwthplots.styles.rwth-latex → optimized for LaTeX integration (.pgf export works nicely).
rwthplots.styles.rwth-word → optimized for Word and Office figures.
rwthplots.styles.rwth-pptx → optimized for PowerPoint figures.
(optional) add your own custom .mplstyle files under rwthplots/styles/.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* in python script with plotting
  ```python
  from RWTHPlots.cmap import rwth_cmap
  
  matplotlib.colormaps.register(rwth_cmap('extended_RWTH_discrete'))
  plt.set_cmap('extended_RWTH_discrete')
  
  ```
* then set cmap for each python plot created with matplotlib to 'extended_RWTH_discrete'

### Hints
Also consider to export files as .pgf to be used with LaTeX: https://jwalton.info/Matplotlib-latex-PGF/

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact
Steffen Kortmann - [s.kortmann@iaew.rwth-aachen.de](mailto:s.kortmann@iaew.rwth-aachen.de)

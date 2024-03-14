# Colormap with RWTH colors for Matplotlib
Adding formatting with RWTH Aachen University colous to matplotlib

<!-- GETTING STARTED -->
## Getting Started

These are the corporate design colors at RWTH Aachen University.

### Installation

| ⚠️ Warning                                                            | 
|-----------------------------------------------------------------------|
| You need to use pip <=23.0.1, otherwise post-installation hook fails! |
| There are known issues that LaTeX cannot be displayed via PyCharm due to backend problems, but it works by using the 'rwth-word' style first and inspect the figure and if it is ready for export, ``plt.savefig()`` works easily. |

Also consider to export files as .pgf to be used with LaTeX: https://jwalton.info/Matplotlib-latex-PGF/

# Installation via

* (simplest) pip install from gitlab (requires gitlab credentials
    * open terminal
    ```sh
    pip install git+https://gitlab.iaew.rwth-aachen.de/aev/RWTHPlots.git
    ```

* (also ok) clone folder from gitlab and navigate to the repository then
  * open terminal
    ```sh
    pip install --upgrade pip==23.0.1
    pip install -e .
    ```

* (advanced) alternatively using a ssh-key
  * open terminal
    ```sh
    pip install git+ssh://git@gitlab.iaew.rwth-aachen.de/aev/RWTHPlots.git
    ``` 

Finally open python console to check succesful installation

```python
import matplotlib.pyplot as plt
plt.style.available

# for simple usage
import matplotlib.pyplot as plt
plt.style.use('rwth-latex')
```


<!-- USAGE EXAMPLES -->
## Usage


### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* in python script with plotting
  ```python
  from RWTHPlots.cmap import rwth_cmap
  
  matplotlib.colormaps.register(rwth_cmap('extended_RWTH_discrete'))
  plt.set_cmap('extended_RWTH_discrete')
  
  ```
* then set cmap for each python plot created with matplotlib to 'extended_RWTH_discrete'

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Steffen Kortmann - steffen.kortmann@rwth-aachen.de

<p align="right">(<a href="#readme-top">back to top</a>)</p>


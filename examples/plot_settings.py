import os

import matplotlib.pyplot as plt
import numpy as np
import rwthplots  # noqa: F401 – registers colormaps and styles
import rwthplots.rwth_matplotlib_layout as layout

os.makedirs("figures", exist_ok=True)

fig, ax = plt.subplots(figsize=(layout.cm2in * 20, layout.cm2in * 12))

x = np.linspace(0, 2 * np.pi, 400)
ax.plot(x, np.sin(x))

ax.set_xlabel(r"$x$ (rad)")
ax.set_ylabel(r"$\sin(x)$")

fig.tight_layout()
fig.savefig("figures/sine_for_ppt.png")
fig.savefig("figures/sine_for_ppt.svg")
plt.close(fig)

import matplotlib.pyplot as plt
import numpy as np
import rwthplots.rwth_matplotlib_layout as layout

# --- 1.  BUILD THE FIGURE ----------------------------------------------------
fig, ax = plt.subplots(figsize=(layout.cm2in*20,layout.cm2in*12))

x = np.linspace(0, 2*np.pi, 400)
ax.plot(x, np.sin(x))

# ax.set_title("Sine Wave", color="#00549F")  # blue title, 20 pt, bold via rcParams
ax.set_xlabel(r"$x$ (rad)")
ax.set_ylabel(r"$\sin(x)$")

fig.tight_layout()
# --- 2.  EXPORT --------------------------------------------------------------
fig.savefig("figures/sine_for_ppt.png")
fig.savefig("figures/sine_for_ppt.svg")

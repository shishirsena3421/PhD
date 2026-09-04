import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colorbar import ColorbarBase

# Create a figure with a narrow axis for the colorbar
fig, ax = plt.subplots(figsize=(0.1, 8))
fig.subplots_adjust(left=0.1, right=0.45, top=0.95, bottom=0.05)

# Define the colormap: blue (bottom) -> green -> yellow -> red (top)
# matching the jet-like colormap in the image
cmap = plt.cm.jet

# Define the value range
vmin = 0.00
vmax = 0.68

norm = mcolors.Normalize(vmin=vmin, vmax=vmax)

# Draw the colorbar
cb = ColorbarBase(
    ax,
    cmap=cmap,
    norm=norm,
    orientation='vertical'
)

# Set ticks only at top and bottom
cb.set_ticks([vmin, vmax])
cb.set_ticklabels([f'{vmin:.2f}', f'{vmax:.2f}'])
cb.ax.tick_params(labelsize=11)

plt.savefig('colorbar_output.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.show()
print("Colorbar saved as colorbar_output.png")

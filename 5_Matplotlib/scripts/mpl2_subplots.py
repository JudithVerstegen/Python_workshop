import numpy as np
from matplotlib import pyplot as plt

# Create some data
x1 = np.arange(-np.pi, np.pi, 0.2)
y1 = np.sin(x1)
x2 = np.arange(-np.pi, 0, 0.2)
y2 = np.cos(x2)

# Initiate a figure
# A figure with two subplots 
f, axarr = plt.subplots(2, sharex=True)
# subplots are stored in an array
line = axarr[0].plot(x1, y1)
axarr[0].set_title('plot 1')
axarr[1].plot(x2, y2)
axarr[1].set_title('plot 2')
f.suptitle('super title', fontsize=16)

# Axis label
axarr[1].set_xlabel('x')
axarr[0].set_ylabel('sin(x)')
axarr[1].set_ylabel('cos(x)')

# Axis ticks and tick labels
xticks = axarr[1].get_xticks()
print(xticks)
new_ticks = np.arange(-np.pi, np.pi + 0.1, 0.25 * np.pi)
new_labels = [r"$-\pi$", r"$-\frac{3}{4}\pi$",
            r"$-\frac{1}{2}\pi$", r"$-\frac{1}{4}\pi$",
            "$0$", r"$\frac{1}{4}\pi$",
            r"$\frac{1}{2}\pi$", r"$\frac{3}{4}\pi$",
            r"$2\pi$"]
axarr[1].set_xticks(new_ticks)
axarr[1].set_xticklabels(new_labels)

plt.show()

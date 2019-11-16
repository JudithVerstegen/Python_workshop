import numpy as np
from matplotlib import pyplot as plt

# Create some data
x = np.arange(-np.pi, np.pi, 0.2)
y = np.sin(x)
# Plot x against y
plt.plot(x,y)
# Show in an interactive plot
plt.show()

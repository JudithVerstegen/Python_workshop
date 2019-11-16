from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0,6,1)
y1 = np.arange(0,3,0.5)
y2 = np.arange(0,12,2)

f, axarr = plt.subplots(1)
one = axarr.plot(x, y1, 'r--', label='gradual line')
two = axarr.plot(x, y2, 'b:', label='steep line')
# legend with location, customized
axarr.legend(loc=2, bbox_to_anchor=(0,1.1), ncol=2)
plt.show()

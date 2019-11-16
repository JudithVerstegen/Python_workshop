from matplotlib import pyplot as plt
from matplotlib import colors as cls
import numpy as np
import os

np.random.seed(seed=10)
x = np.random.random(20)
y = np.random.random(20)
total_range = cls.Normalize(vmin=-1.0, vmax=1.0)

f, axarr = plt.subplots(1)
# scatter polt of random x and y values
# colored by the difference between the pairs
scat = axarr.scatter(x,y, c=x-y, s=35, \
                     label='random dots', \
                     norm=total_range)
axarr.set_xlim([0,1])
axarr.set_ylim([0,1])
# colormap legend normalized
cb = plt.colorbar(scat, spacing='proportional')
cb.set_label('difference between x and y')
# Save the figure to disk
data_dir = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', '2017_2018',
'data')
filename = os.path.join(data_dir, 'random.png')
plt.savefig(filename, dpi=300, format='png')



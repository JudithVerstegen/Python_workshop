from matplotlib import pyplot as plt
import ogr
import os

#############
# Reading a shapefile
in_path = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'workshops_conferences', '2019_2020', \
'ILS_Python', 'materials', 'data', 'gps_track_projected.shp')

# Get the correct driver and open file for reading
driver = ogr.GetDriverByName('ESRI Shapefile')
track = driver.Open(in_path, 0)

# Get the layer
layer = track.GetLayer(0)

# Create the plot
f, axarr = plt.subplots(1)

# Access single features in the places layer
# And plot them
x = []
y = []
elev = []
for feat in layer:
    pt = feat.geometry()
    x.append(pt.GetX())
    y.append(pt.GetY())
    elevation = round(feat.GetField('ele'), 1)
    elev.append(elevation)

del track
axarr.scatter(x, y, c=elev, cmap='Spectral', lw = 0, s = 5)
axarr.set_xlabel('x coordinate')
axarr.set_ylabel('y coordinate')

# Making the axes' units equal      
plt.axis('equal')
plt.show()

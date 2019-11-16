import matplotlib.pyplot as plt
import ogr
import os

#############
# Reading a shapefile
in_path = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', '2017_2018',
'data', 'shapefiles', 'track_reprojected.shp')

# Get the correct driver and open file for reading
driver = ogr.GetDriverByName('ESRI Shapefile')
track = driver.Open(in_path, 0)

# Get the layer
layer = track.GetLayer(0)

# Create the plot
# Not really necessary with one subplot
f, axarr = plt.subplots(1)

# Access single features in the places layer
# And plot them
for feat in layer:
    pt = feat.geometry()
    x = pt.GetX()
    y = pt.GetY()
    # No indexing for axarr, because only one subplot
    axarr.plot(x, y, 'ro')

# Make the axes' units equal
plt.axis('equal')
plt.show()


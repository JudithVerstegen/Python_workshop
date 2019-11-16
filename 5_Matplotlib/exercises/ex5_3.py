from matplotlib import pyplot as plt
import gdal
import numpy as np
import ogr
import os

#############
# Reading a shapefile
data_dir = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'workshops_conferences', '2019_2020', \
'ILS_Python', 'materials', 'data')
in_vector = os.path.join(data_dir, 'gps_track_projected.shp')
in_raster = os.path.join(data_dir, 'clipped_dem.tif')

# Create the plot
# Not really necessary with one subplot
f, axarr = plt.subplots(1)

# open the raster and read out the data in a numpy array
rast_data_source = gdal.Open(in_raster)
in_band = rast_data_source.GetRasterBand(1)
data = in_band.ReadAsArray()

geoTransform = rast_data_source.GetGeoTransform()
minx = geoTransform[0]
maxy = geoTransform[3]
maxx = minx + geoTransform[1] * \
       rast_data_source.RasterXSize
miny = maxy + geoTransform[5] * \
       rast_data_source.RasterYSize

# use imshow to plot the raster
im = axarr.imshow(data, extent=(minx, maxx, miny, maxy))
# add the legend
cb = plt.colorbar(im, spacing='proportional')
cb.set_label('elevation raster (m)')

# Get the correct driver and open vector file for reading
driver = ogr.GetDriverByName('ESRI Shapefile')
track = driver.Open(in_vector, 0)

# Get the layer
layer = track.GetLayer(0)

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

# Make the scatter plot and catch the object for the legend
scat = axarr.scatter(x, y, c=elev, cmap='Spectral_r', lw = 0, s = 5)
# Include the legend
cb = plt.colorbar(scat, spacing='proportional')
# Set the labels of the legend and the axes
cb.set_label('elevation gps (m)')
axarr.set_xlabel('x coordinate')
axarr.set_ylabel('y coordinate')
axarr.tick_params(axis='both', labelsize=8)
axarr.set_aspect('equal')

# Solve the problem with not enough space on left hand side
f.subplots_adjust(left=0.14)
# Save the figure to disk
plt.savefig(os.path.join(data_dir, 'elevations.png'), \
dpi=300, format='png')

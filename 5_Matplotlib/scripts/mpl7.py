import gdal
from matplotlib import pyplot as plt
import numpy as np
import os

# path to the raster
data_dir = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', '2017_2018',
'data')
in_fn = os.path.join(data_dir, 'rasters', 'clipped_dem.tif')

# open the raster and read out the data in a numpy array
rast_data_source = gdal.Open(in_fn)
in_band = rast_data_source.GetRasterBand(1)
data = in_band.ReadAsArray()

geoTransform = rast_data_source.GetGeoTransform()
minx = geoTransform[0]
maxy = geoTransform[3]
maxx = minx + geoTransform[1] * \
       rast_data_source.RasterXSize
miny = maxy + geoTransform[5] * \
       rast_data_source.RasterYSize

# create the figure
f, axarr = plt.subplots(1)
# use imshow to plot the raster with the correct coordinates
im = axarr.imshow(data, extent=(minx, maxx, miny, maxy))
# add the legend
cb = plt.colorbar(im, spacing='proportional')
cb.set_label('elevation (m)')
plt.show()


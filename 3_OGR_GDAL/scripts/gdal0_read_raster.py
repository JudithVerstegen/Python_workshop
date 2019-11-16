import gdal
import numpy as np
import os

#############
data_dir = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', 'data')

# Path to the raster
in_path = os.path.join(data_dir, 'rasters', \
    'clipped_dem.tif')

# Open the raster
rast_data_source = gdal.Open(in_path)

# Get metadata at data_source level
print('Nr of bands:', rast_data_source.RasterCount)
cols = rast_data_source.RasterXSize
rows = rast_data_source.RasterYSize
print('Size:', cols, rows)

# Select (the only) band and get meta data at band level
srcband = rast_data_source.GetRasterBand(1)
srcband.ComputeStatistics(0)
print('Minimum is:', srcband.GetMinimum())
print('Maximum is:', srcband.GetMaximum())

# Create empty array and catch the data in it
data = np.empty((rows, cols))
srcband.ReadAsArray(buf_obj=data)
print(data)








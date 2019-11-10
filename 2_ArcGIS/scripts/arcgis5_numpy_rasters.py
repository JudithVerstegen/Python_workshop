# Import modules
import arcpy
import numpy as np
import os

# Set workspace
wd = os.getcwd()
arcpy.env.workspace = os.path.join(wd, 'data', 'rasters')

# Get input Raster properties
in_ras = arcpy.Raster('clipped_dem.tif')

# Convert Raster to numpy array
arr = arcpy.RasterToNumPyArray(in_ras, \
                               nodata_to_value=-999)

# Calculate some summary statistics
print('raster size is: ', arr.shape)
# Mask the no data values
arr = np.ma.masked_where(arr == -999, arr)
print('mean elevation in my area is: ', np.mean(arr))

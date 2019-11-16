import gdal
import numpy as np
import os
import osr

#############
data_dir = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', '2017_2018', \
'data')
# Path to the new raster file
out_fn = os.path.join(data_dir, 'rasters', 'test.tif')
# Spatial reference system
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326) # WGS84
# Create the data
data = np.arange(0,100).reshape(10,10)

# Define properties of the new raster
originX = 4
originY = 52
pixelWidth = 1
pixelHeight = -1

# Create the output file and add the properties
driver = gdal.GetDriverByName('GTiff')
out_ds = driver.Create(out_fn, data.shape[1], 
                        data.shape[0], 1, gdal.GDT_UInt32)
out_ds.SetGeoTransform((originX, pixelWidth, 0, \
                        originY, 0, pixelHeight))
out_ds.SetProjection(srs.ExportToWkt())

# Add the data
outband = out_ds.GetRasterBand(1)
outband.WriteArray(data)
out_ds.FlushCache()


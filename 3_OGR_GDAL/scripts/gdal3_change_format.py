import gdal
import numpy as np
import os
import osr

#############
data_dir = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', '2017_2018', \
'data')
# Path to the old and new raster file
in_fn = os.path.join(data_dir, 'rasters', 'test.tif')
out_fn = os.path.join(data_dir, 'rasters', 'test.asc')

driver = gdal.GetDriverByName('AAIGrid')
in_ds = gdal.Open(in_fn)
out_ds = driver.CreateCopy(out_fn, in_ds)
del out_ds







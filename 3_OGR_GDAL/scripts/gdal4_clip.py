import gdal
import os

data_dir = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', '2017_2018', \
'data')
# Path to the raster
in_fn = os.path.join(data_dir, 'rasters', 'test.tif')
out_fn = os.path.join(data_dir, 'rasters', \
                        'clipped_test.tif')
# Input: clip coordinates (max x and max y)
coordx = 10
coordy = 50

# Open the raster
rast_data_source = gdal.Open(in_fn)
    
# Get object that can translate coordinates 
# to raster indices
# BEHAVIOR OF InvGeoTransform depends on gdal version
gt = rast_data_source.GetGeoTransform()
inv_gt = gdal.InvGeoTransform(gt)

# Get the indices of the coordinates of your clip
x1, y1= gdal.ApplyGeoTransform(inv_gt, coordx, coordy)
# make integers of these indices
x1 = int(x1)
y1 = int(y1)
print('column numbers are', x1, y1)
# for x nr of columns is the same as we clip from the x origin
out_columns = x1
# for y not
out_rows = rast_data_source.RasterYSize - y1

# Create empty output raster (clipped size)
out_driver = gdal.GetDriverByName('GTiff')
# Rasters can be overwritten (cannot delete)
out_ds = out_driver.Create(out_fn, out_columns, 
                                    out_rows, 1)
out_ds.SetProjection(rast_data_source.GetProjection())
# Geotransfor can remain the same, except the y origin!
out_gt = list(gt)
out_gt[3] = coordy
print(out_gt)
out_ds.SetGeoTransform(out_gt)

# Get data from the source raster and write to the new one
in_band = rast_data_source.GetRasterBand(1)
out_band = out_ds.GetRasterBand(1)
data = in_band.ReadAsArray(0, y1, out_columns, out_rows)
out_band.WriteArray(data)
out_ds.FlushCache()
print('done')
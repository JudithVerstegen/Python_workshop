import gdal
import os

#############
# path to the shapefile
data_dir = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'workshops_conferences', '2019_2020', \
'ILS_Python', 'materials', 'data', )

# Path to the tif and new raster file
in_path = os.path.join(data_dir, 'clipped_dem.tif')
out_path = os.path.join(data_dir, 'clipped_dem.asc')

# Save the tif as an asc
in_ds = gdal.Open(in_path)
driver = gdal.GetDriverByName('AAIGrid')
out_ds = driver.CreateCopy(out_path, in_ds)
del out_ds

# print the data 
in_band = in_ds.GetRasterBand(1)
data = in_band.ReadAsArray()
print(data)
print(type(data))
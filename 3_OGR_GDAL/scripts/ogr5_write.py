import ogr
import os

# reading a shapefile
in_path = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', \
'data', 'naturalearthdata', 'ne_10m_populated_places.shp')

# get the correct driver
in_driver = ogr.GetDriverByName('ESRI Shapefile')
places_source = in_driver.Open(in_path, 0) 

# write the data to a geojson
out_file = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', \
'data', 'naturalearthdata', 'ne_10m_populated_places.geojson')
out_driver = ogr.GetDriverByName('GeoJSON')
out_ds  = out_driver.CopyDataSource(places_source,out_file)
del out_ds
import ogr
import os

#############
# path to the shapefile
in_path = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'workshops_conferences', '2019_2020', \
'ILS_Python', 'materials', 'data', 'gps_track_projected.shp')

# get the correct driver and open the shapefile
driver = ogr.GetDriverByName('ESRI Shapefile')
data_source = driver.Open(in_path, 0) 
print('Opened %s' % (in_path))

# path to the new file
out_path = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'workshops_conferences', '2019_2020', \
'ILS_Python', 'materials', 'data', 'gps_track_projected.geojson')

# write the data to a geojson
out_driver = ogr.GetDriverByName('GeoJSON')
out_ds = out_driver.CopyDataSource(data_source, out_path)
del out_ds
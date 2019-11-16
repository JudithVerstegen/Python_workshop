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

# get the Layer class object
layer = data_source.GetLayer(0)

# print the number of features
feature_count = layer.GetFeatureCount()
print("Number of features in %s: %d" % \
      (os.path.basename(in_path),feature_count))
      
# access single features
for feat in layer:
    # get and print elevation attribute
    elevation = feat.GetField('ele')
    print(elevation)

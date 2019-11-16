import ogr
import os

#############
# reading the places shapefile
in_path = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', '2017_2018', \
'data', 'naturalearthdata', 'ne_10m_populated_places.shp')

# reading the countries shapefile
in_path2 = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', '2017_2018', \
'data', 'naturalearthdata', 'ne_10m_admin_0_countries.shp')

# get the correct driver
driver = ogr.GetDriverByName('ESRI Shapefile')

# 0 means read-only. 1 means writeable.
places_source = driver.Open(in_path, 0) 
countries_source = driver.Open(in_path2, 0) 

# Check to see if shapefile is found.
if countries_source is None:
    print('Could not open %s' % (in_path2))

print('Opened %s' % (in_path2))
# get the Layer class objects
places_layer = places_source.GetLayer(0)
countries_layer = countries_source.GetLayer(0)
# set a filter to the countries layer
countries_layer.SetAttributeFilter("NAME = 'Germany'")
# get the feature (should be only one!)
feature_count = countries_layer.GetFeatureCount()
print("Number of features in %s: %d" % \
      (os.path.basename(in_path2),feature_count))
feat =  countries_layer.GetNextFeature()
germany = feat.geometry().Clone()
print(germany)

# now filter the features in the places layer
places_layer.SetSpatialFilter(germany)
# access single features in the places layer
for feat in places_layer:
    pt = feat.geometry()
    x = pt.GetX()
    y = pt.GetY()
    name = feat.GetField('NAME')
    print(name, x, y)
    
import ogr
import os

#############
# reading a shapefile
in_path = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', '2017_2018', \
'data', 'naturalearthdata', 'ne_10m_populated_places.shp')

# get the correct driver
driver = ogr.GetDriverByName('ESRI Shapefile')

# 0 means read-only. 1 means writeable.
data_source = driver.Open(in_path, 0) 

# Check to see if shapefile is found.
if data_source is None:
    print('Could not open %s' % (in_path))

print('Opened %s' % (in_path))
# get the Layer class object
layer = data_source.GetLayer(0)
# get reference system info
spatial_ref = layer.GetSpatialRef()
print(spatial_ref)
# get info about the attributes (fields)
attributes = layer.GetLayerDefn()
for i in range(attributes.GetFieldCount()):
    print(attributes.GetFieldDefn(i).GetName())

# get info about the features
feature_count = layer.GetFeatureCount()
print("Number of features in %s: %d" % \
      (os.path.basename(in_path),feature_count))
# access single features
for feat in layer:
    pt = feat.geometry()
    x = pt.GetX()
    y = pt.GetY()
    name = feat.GetField('NAME')
    pop = feat.GetField('POP_MAX')
    country = feat.GetField('ADM0NAME')
    if country == 'Germany': print(name, pop, x, y)

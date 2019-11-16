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
# set a filter 
layer.SetAttributeFilter("ADM0NAME = 'Germany'")
# access single features
for feat in layer:
    pt = feat.geometry()
    x = pt.GetX()
    y = pt.GetY()
    name = feat.GetField('NAME')
    pop = feat.GetField('POP_MAX')
    print(name, pop, x, y)
    
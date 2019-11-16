import os
from qgis.core import *
import qgis.utils

# path to shapefile
shape_file = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'workshops_conferences', '2019_2020', \
'ILS_Python', 'materials', 'data', 'gps_track_projected.shp')

# load the shapefile
layer = iface.addVectorLayer(shape_file, "shape:", "ogr")
if not layer:
    print("Shapefile failed to load!")

# Check for editing rights (capabilities)
caps = layer.dataProvider().capabilities()
print(caps)
caps_string = layer.dataProvider().capabilitiesString()
print(caps_string)

# Changing a single attribute value
fid = 10   # INDEX of the feature we will modify
if caps & QgsVectorDataProvider.ChangeAttributeValues:
    # field index : new value
    attrs = {1:12}
    # Note the dictionary of dictionaries!
    layer.dataProvider().changeAttributeValues({fid:attrs})

# Change it back
if caps & QgsVectorDataProvider.ChangeAttributeValues:
    attrs = {1:0}
    # Note the dictionary of dictionaries!
    layer.dataProvider().changeAttributeValues({fid:attrs})

QgsProject.instance().removeMapLayer(layer.id())


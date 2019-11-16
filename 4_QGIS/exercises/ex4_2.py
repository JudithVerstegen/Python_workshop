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

# Adding a field (attribute)
if caps & QgsVectorDataProvider.AddAttributes:
    # Adding as a list of items, each with
    # the name and the data type of the field
    res = layer.dataProvider().addAttributes(
        [QgsField("elediff", QVariant.Double)])
        
# update to propagate the changes  
layer.updateFields()

# Changing a attribute values of this field
if caps & QgsVectorDataProvider.ChangeAttributeValues:
    prev_ele = 0
    for feat in layer.getFeatures():
        fid = feat.id()   # INDEX of the feature we will modify
        print(fid)
        # compute the elevation difference
        if fid == 0:
            diff = 0
        else:
            diff = feat['ele'] - prev_ele
        # field index : new value
        attrs = {6:diff}
        # Note the dictionary of dictionaries!
        layer.dataProvider().changeAttributeValues({fid:attrs})
        prev_ele = feat['ele']
        
# update to propagate the changes  
layer.updateFields()

#QgsProject.instance().removeMapLayer(layer.id())


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
        [QgsField("mytext", QVariant.String),
        QgsField("myint", QVariant.Int)])

# update to propagate the changes  
layer.updateFields()

# Now remove the fields again because we do not need them
# Hereto, we need the field index
# Unfortunately backward counting (-1 and -2) does not work
if caps & QgsVectorDataProvider.DeleteAttributes:
    res = layer.dataProvider().deleteAttributes([6, 7])

# update to propagate the changes  
layer.updateFields()    

QgsProject.instance().removeMapLayer(layer.id())


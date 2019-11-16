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

# Adding a feature
if caps & QgsVectorDataProvider.AddFeatures:
    feat = QgsFeature(layer.fields())
    # Set a single attribute by key or by index:
    feat.setAttribute('ele', 7)
    feat.setAttribute(3, 7)
    # Set the FID
    
    feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(381770,5727771)))
    (res, outFeats) = layer.dataProvider().addFeatures([feat])

# Deleting the feature
if caps & QgsVectorDataProvider.DeleteFeatures:
    res = layer.dataProvider().deleteFeatures([428])

QgsProject.instance().removeMapLayer(layer.id())


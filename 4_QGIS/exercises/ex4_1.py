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

# Feature selection with expression
exp = QgsExpression('$id < 11')
# Note that the field track_se_1 contains the id too
# So, another solution would be:
#exp = QgsExpression('track_se_1 < 11')
request = QgsFeatureRequest(exp)
selection = layer.getFeatures(request)

# Check elevations
for feature in selection:
    print("Feature ID: %d " % feature.id(), \
        "elevation: %d " % feature['ele'])
    
QgsProject.instance().removeMapLayer(layer.id())


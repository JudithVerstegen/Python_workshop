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
else:
    print('layer', layer)
    for feat in layer.getFeatures():
        print('feature', feat)
  
QgsProject.instance().removeMapLayer(layer.id())    

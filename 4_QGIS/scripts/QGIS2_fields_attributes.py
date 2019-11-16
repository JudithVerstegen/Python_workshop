import os
from qgis.core import *
import qgis.utils

# path to shapefile
shape_file = os.path.join('C:\\', 'Users', 'verstege', \
'Documents', 'education', 'python_in_GIS', '2017_2018', \
'data', 'shapefiles', 'track_points.shp')

# load the shapefile
layer = iface.addVectorLayer(shape_file, "shape:", "ogr")
if not layer:
    print("Shapefile failed to load!")

# Show field names of this shapefile    
for field in layer.fields():
    print(field.name(), field.typeName())

# Loop over all features
features = layer.getFeatures()
for feature in features:
    # retrieve id and attribute values
    print("Feature ID: %d " % feature.id())
    attributes = feature.attributes()
    # attributes is a list
    for field, attr in zip(layer.fields(), attributes):
        print(field.name(), ':', attr)
    # I do this because looping over all takes long
    if feature.id() == 5: break

# Feature selection with expression
exp = QgsExpression('ele > 100')
request = QgsFeatureRequest(exp)
selection = layer.getFeatures(request)

# Check elevations
for feat in selection:
    print(feat['ele'])
    
QgsProject.instance().removeMapLayer(layer.id())


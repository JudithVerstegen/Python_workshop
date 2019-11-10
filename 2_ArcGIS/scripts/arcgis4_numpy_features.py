# Import modules
import arcpy
import datetime
import numpy as np
import os

# Set workspace
wd = os.getcwd()
arcpy.env.workspace = os.path.join(wd, 'data',\
                                   'shapefiles')
# FeatureClassToNumPyArray
arr = arcpy.da.FeatureClassToNumPyArray('track_reprojected.shp', \
                                        ('FID', 'ele', 'time_str'))

# Calclate some things using numpy and datetime:
# How long did the hike take (assuming the points are ordered)?
print(datetime.datetime.strptime(arr['time_str'][-1], '%H:%M:%S') -\
      datetime.datetime.strptime(arr['time_str'][0], '%H:%M:%S'))
# What was the mean elevation along my track?
print(arr['ele'].mean())

# An array with information about buildings
arr_new = np.array([('cinama', 'cultural', 30),\
                    ('mall', 'commercial', 15)],\
                   dtype=[('name', 'U15'), ('type', 'U15'),\
                          ('height', 'i4')])

# Define a location and check if the table already exists
fn = os.path.join(wd, 'data', 'new_table.dbf')
if arcpy.Exists(fn):
    arcpy.Delete_management(fn)

# NumPyArrayToTable
arcpy.da.NumPyArrayToTable(arr_new, fn)

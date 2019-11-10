# Import modules
import arcpy
import numpy as np
import os

# Set workspace
wd = os.path.join('C:\\', 'Users', 'verstege', 'Documents', \
                  'workshops_conferences', '2019_2020', 'ILS_Python', \
                  'materials')
arcpy.env.workspace = os.path.join(wd, 'data')

# FeatureClassToNumPyArray
arr = arcpy.da.FeatureClassToNumPyArray('gps_track_projected.shp', \
                                    ('FID', 'ele', 'clipped_de'))

# Calculate the row-by-row difference as an array
diff = arr['ele'] - arr['clipped_de']

# Compute mean and standard deviation of this array
print('mean difference is: ', np.mean(diff))
print('sd difference is: ', np.std(diff))


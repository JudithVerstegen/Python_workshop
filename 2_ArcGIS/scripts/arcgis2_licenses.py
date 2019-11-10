# Import modules
import arcpy
import os

# Set workspace
wd = os.getcwd()
arcpy.env.workspace = os.path.join(wd, 'data',\
                                   'shapefiles')

# Check out extension
if arcpy.CheckExtension('Spatial') == 'Available':
    arcpy.CheckOutExtension('Spatial')
else:
    # Print error message
    print('Required extension not available')

# Define output location and check existence
out_fn = os.path.join(wd, 'data', 'rasters', 'dens')
if arcpy.Exists(out_fn):
    arcpy.Delete_management(out_fn)
# Run the PointDensity tool
out_ras = arcpy.sa.PointDensity('track_reprojected.shp', \
                                None, 100)
# Save the output 
out_ras.save(out_fn)

# check in extension (give it back)
arcpy.CheckInExtension('Spatial')

print('done')

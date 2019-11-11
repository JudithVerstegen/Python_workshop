# Import modules
import arcpy
import os

# Set workspace
wd = os.path.join('C:\\', 'Users', 'verstege', 'Documents', \
                  'workshops_conferences', '2019_2020', 'ILS_Python', \
                  'materials')
in_shape = os.path.join(wd, 'data', 'gps_track_projected.shp')
in_raster = os.path.join(wd, 'data', 'clipped_dem.tif')
arcpy.env.workspace = os.path.join(wd, 'data')

# Check out extension
if arcpy.CheckExtension('Spatial') == 'Available':
    arcpy.CheckOutExtension('Spatial')
else:
    # Print error message
    print('Required extension not available')

# Define output location and check existence
out_table = os.path.join(wd, 'data', 'elev_table.dbf')
if arcpy.Exists(out_table):
    arcpy.Delete_management(out_table)
    
# Run the Sample tool
out = arcpy.sa.Sample(in_raster, in_shape, \
                      out_table, 'NEAREST', 'FID')
print(out) # Note that this is the file name
# Run Join Field to join the output to the shapefile
# Looking at the table, you find that the shape id is track_repr
arcpy.management.JoinField(in_shape, 'FID', out, 'gps_track_')

# check in extension (give it back)
arcpy.CheckInExtension('Spatial')

print('done')

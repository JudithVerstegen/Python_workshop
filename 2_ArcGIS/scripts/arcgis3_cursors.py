# Import modules
import arcpy
import os

# Set workspace
wd = os.getcwd()
arcpy.env.workspace = os.path.join(wd, 'data',\
                                   'shapefiles')

### search cursor ###
# Create a search cursor to retrieve features
se_cursor = arcpy.da.SearchCursor('track_reprojected.shp',\
                                 ['FID', 'ele'])
# Loop over all features
for row in se_cursor:
    print('ID: ' + str(row[0]) + \
          ', original elevation: ' + str(row[1]))

### insert cursor ###
# A list of values that will be used to construct new rows
# Give the attribute values for the fields in the cursor
row_values = [(80.1, (383625.0, 5727588.0)),\
              (78.3, (383725.0, 5727588.0))]

# Create an insert cursor
ins_cursor = arcpy.da.InsertCursor('track_reprojected.shp',\
                               ['ele', 'SHAPE@XY'])

# Insert new rows 
for row in row_values:
    ins_cursor.insertRow(row)

# Delete cursor object
del ins_cursor

### update cursor ###
# Create an update cursor
upd_cursor = arcpy.da.UpdateCursor('track_reprojected.shp',\
                                 ['FID', 'track_se_1'])
# Loop for updating the track_se1 fields of new features
for row in upd_cursor:
    if (row[1] == 0) and (row[0] != 0):
        row[1] = row[0]
        # Update the cursor with the updated list
        upd_cursor.updateRow(row)

# Deleting the inserted features again
upd_cursor.reset()
for row in upd_cursor:
    if (row[0] == 428) or (row[0] == 429):
        upd_cursor.deleteRow()

del upd_cursor

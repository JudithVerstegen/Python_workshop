# Import modules
import arcpy
import datetime
import numpy as np
import os

# Define inputs and outputs
wd = os.getcwd()
vector_input = arcpy.GetParameterAsText(0)
time_field = arcpy.GetParameterAsText(1)
new_field_name = 'speed'

# Get the two required fields as structured numpy array
arr = arcpy.da.FeatureClassToNumPyArray(vector_input, \
                                        ('SHAPE@XY', time_field))
print(arr.shape)

# initiate list for speeds
speeds = []
prev_coords = 0
prev_time = 0
# Loop over all features and calculate the speed
for i in range(0, arr.shape[0]):
    # Get the time and coordinates of the point
    this_coords = arr[i][0]
    this_time = datetime.datetime.strptime(arr[i][1], '%H:%M:%S')
    if prev_time == 0:
        speed = 0
    else:
        # First calculate the distance between this point and prev
        x_diff = abs(this_coords[0] - prev_coords[0])
        y_diff = abs(this_coords[1] - prev_coords[1])
        distance = np.sqrt(np.square(x_diff) + np.square(y_diff))
        # Convert to km (for speed in km/h)
        distance_km = distance / 1000.0
        # Second, calculate the time between this point and prev
        time_diff = this_time - prev_time
        time_diff_h = time_diff.total_seconds() / 3600.0
        # Prevent division by zero
        if time_diff_h == 0.0:
            speed = 0
        else:
            # Calculate speed
            speed = distance_km / time_diff_h
    speeds.append(speed)
    # Make this point the previous point for the next round
    prev_coords = this_coords
    prev_time = this_time

# Check if a 'speed' field already exists, if yes, delete it
field_names = [f.name for f in arcpy.ListFields(vector_input)]
if new_field_name in field_names:
    print('exists')
    arcpy.DeleteField_management(vector_input, [new_field_name])
 
# Add the speed field to the vector file
# Precision and scale: max 6 digits of wich two decimals
arcpy.AddField_management(vector_input, new_field_name, 'FLOAT', \
                          field_scale=2, field_precision=6)

# Create an update cursor
upd_cursor = arcpy.da.UpdateCursor(vector_input,[new_field_name])
# Loop for updating the track_se1 fields of new features
for row, speed in zip(upd_cursor, speeds):
    row[0] = speed
    # Update the row with cursor
    upd_cursor.updateRow(row)

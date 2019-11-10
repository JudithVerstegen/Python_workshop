# Import modules
import arcpy
import os

# Define inputs and outputs
wd = os.getcwd()
vector_input = arcpy.GetParameterAsText(0)
raster_input = arcpy.GetParameterAsText(1)
raster_output = os.path.join(arcpy.GetParameterAsText(2), \
                             arcpy.GetParameterAsText(3))

# Check existence
if arcpy.Exists(raster_output):
    arcpy.Delete_management(raster_output)

# Get the extent 
desc = arcpy.Describe(vector_input)
extent = desc.extent
# This oject contains (XMin,YMin,XMax,YMax,ZMin,ZMax,MMin,MMax)
# We need the first four as input for Clip
extent_string = str(extent.XMin) + ' ' + str(extent.YMin) + ' ' +  \
                str(extent.XMax) + ' ' + str(extent.YMax) 
print(extent_string)

# Clip the raster
arcpy.Clip_management (raster_input, extent_string, raster_output, \
                     maintain_clipping_extent = 'NO_MAINTAIN_EXTENT')



#import modules
import arcpy
import os

#set workspace
wd = os.getcwd()
arcpy.env.workspace = os.path.join(wd, 'data',\
                                   'shapefiles') 

#set up a describe object for each fc in folder
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
    desc = arcpy.Describe(fc)
    #print the file name and its ref system
    print(fc, desc.spatialReference.name)

print('done')

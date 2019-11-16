import ogr

#drivers
driver = ogr.GetDriver(1)
print(driver)

cnt = ogr.GetDriverCount()
formats_list = []  # Empty List

for i in range(cnt):
    driver = ogr.GetDriver(i)
    driver_name = driver.GetName()
    if not driver_name in formats_list:
        formats_list.append(driver_name)

formats_list.sort() # Sorting the list of drivers

for i in formats_list:
    print(i)


from matplotlib import pyplot as plt

#############

# data
lu_types = ['urban', 'cropland', 'pasture', 'forest']
positions = [1,2,3,4]
areas = [1000, 20000, 7000, 3000]

# Create the plot
f, (ax0, ax1) = plt.subplots(1, 2)

# Plot the bar chart
ax0.bar(positions, areas)
ax0.set_xticks(positions)
ax0.set_xticklabels(lu_types)
ax0.set_xlabel("land use type")
ax0.set_ylabel("area (ha)")

# plot the pie chart
ax1.pie(areas, labels=lu_types)
plt.show()

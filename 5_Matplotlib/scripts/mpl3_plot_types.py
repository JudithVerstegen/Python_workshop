from matplotlib import pyplot as plt

x = [1,2,3,4,5]
y = [6,7,8,9,10]

# New: define nr of rows and columns
# And we unpack them directly
f, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2)
ax0.plot(x, y, 'r--')
ax1.scatter(x, y, c=y, cmap='bwr', s = 35)
ax2.bar(x, y, color='k')
ax3.barh(x, y, color='y')
plt.show()

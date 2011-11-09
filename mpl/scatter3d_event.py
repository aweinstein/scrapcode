from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def on_hover(event):
    #print dir(event)
    print event.xdata

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1, 2, 3]
y = [1, 5, 4]
z = [3, 5, 6]
ax.scatter(x, y, z)
ax.plot([1,2], [1,5], [3,5])
ax.plot([2,3], [5,4], [5,6])
ax.plot([3,1], [4,1], [6,3])
#cid = fig.canvas.mpl_connect('motion_notify_event', on_hover)

plt.show()

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
import matplotlib.pyplot as plt
import numpy as np

def get_3d_point(xd, yd, ax):
    p = (xd, yd)
    edges = ax.tunit_edges()
    ldists = [(proj3d.line2d_seg_dist(p0, p1, p), i) for \
              i, (p0, p1) in enumerate(edges)]
    ldists.sort()
    # nearest edge
    edgei = ldists[0][1]

    p0, p1 = edges[edgei]

    # scale the z value to match
    x0, y0, z0 = p0
    x1, y1, z1 = p1
    d0 = np.hypot(x0-xd, y0-yd)
    d1 = np.hypot(x1-xd, y1-yd)
    dt = d0 + d1
    z = d1/dt * z0 + d0/dt * z1
    return proj3d.inv_transform(xd, yd, z, ax.M)

def on_hover(event):
    xd , yd = event.xdata, event.ydata
    if xd and yd:
        x, y, z = get_3d_point(xd, yd, ax)
        print x, y, z

def on_hover_x(event):
    epsilon = 2e-1
    xd, yd = event.xdata, event.ydata
    if xd and yd:
        xd, yd, zd = get_3d_point(xd, yd, ax)
        x_match = np.nonzero(np.abs(x - xd) < epsilon)[0]
        y_match = np.nonzero(np.abs(y - yd) < epsilon)[0]
        z_match = np.nonzero(np.abs(z - zd) < epsilon)[0]
        if len(x_match) > 0 and len(y_match) > 0 and len(z_match) >0:
            x0, y0, z0 = x[x_match[0]], y[y_match[0]], z[z_match[0]]
            print x0, y0, z0
            s = '%.2f %.2f %.2f' % (x0, y0, z0)
            #fig.canvas.draw()
            

        
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3]
y = [1, 5, 4]
z = [3, 5, 6]
ax.scatter(x, y, z)
ax.plot([1,2], [1,5], [3,5])
ax.plot([2,3], [5,4], [5,6])
ax.plot([3,1], [4,1], [6,3])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
## ax.set_xlim(min(x)-1, max(x)+1)
## ax.set_ylim(min(y)-1, max(y)+1)
## ax.set_zlim(min(z)-1, max(z)+1)
#t = ax.text(0.5, 0.5, 0.5, '', color='r')

cid = fig.canvas.mpl_connect('motion_notify_event', on_hover)

plt.show()

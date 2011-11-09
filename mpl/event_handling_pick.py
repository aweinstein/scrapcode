from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt


text_objs = defaultdict(lambda: None)
def on_pick(event):
    ind = event.ind[0]
    x0, y0 = x[ind], y[ind]
    print ind, x0, y0
    if text_objs[ind] is None:
        s = '%.2f %.2f' % (x0, y0)
        text_objs[ind] = plt.text(x[ind], y[ind], s, color='g')
    else:
        text_objs[ind].remove()
        del(text_objs[ind])
    fig.canvas.draw()
    

def on_hover(event):
    epsilon = 2e-3
    xd, yd = event.xdata, event.ydata
    if xd and yd:
        x_match = np.nonzero(np.abs(x - xd) < epsilon)[0]
        y_match = np.nonzero(np.abs(y - yd) < epsilon)[0]

        if len(x_match) > 0 and len(y_match) > 0:
            x0, y0 = x[x_match[0]], y[y_match[0]]
            print x0, y0
            s = '%.2f %.2f' % (x0, y0)
            t.set_text(s)
            t.set_x(x0)
            t.set_y(y0)
            fig.canvas.draw()
    

x = np.random.rand(100)
y = np.random.rand(100)

## x = np.array([1, 2, 3])
## y = np.array([3, 7, 9])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y, picker=True)

cid_1 = fig.canvas.mpl_connect('pick_event', on_pick)
#cid_2 = fig.canvas.mpl_connect('motion_notify_event', on_hover)

t = plt.text(0.5, 0.5, '', color='r')

plt.show()

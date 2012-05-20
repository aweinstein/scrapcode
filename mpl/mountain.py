import sys
import gtk, gobject
import matplotlib
matplotlib.use('GTKAgg') #Agg rendering to a GTK canvas (requires PyGTK)
import pylab as p
import numpy as np
import time
from matplotlib.patches import Circle

ax = p.subplot(111)
canvas = ax.figure.canvas

# for profiling
tstart = time.time()

height = lambda x: np.sin(3*x)/3.0

x_min, x_max = -1.2, 0.6
x = np.linspace(x_min, x_max, 100)
line = p.plot(x, height(x))
p.axis('scaled')
p.xlim((x_min,x_max))
p.ylim((-0.4,0.5))

def animate(*args):

    if animate.background is None:
        animate.background = canvas.copy_from_bbox(ax.bbox)
    canvas.restore_region(animate.background)

    # Draw circle
    r = 0.05
    x = x_min + 0.02*animate.cnt
    y = height(x) + r
    cir = Circle((x, y), r, animated=True)
    ax.add_patch(cir)
    ax.draw_artist(cir)
    
    # just redraw the axes rectangle
    canvas.blit(ax.bbox)

    if animate.cnt==1500:
        # print the timing info and quit
        print 'FPS:' , animate.cnt/(time.time()-tstart)
        sys.exit()

    animate.cnt += 1
    time.sleep(0.05)
    return True

animate.cnt = 0
animate.background = None

gobject.idle_add(animate)


p.show()


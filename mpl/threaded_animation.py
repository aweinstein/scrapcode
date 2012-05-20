#!/usr/bin/env python   
import time
import threading
import Queue

import gtk, gobject
import matplotlib
matplotlib.use('GTKAgg') #Agg rendering to a GTK canvas (requires PyGTK)
import pylab as p
import numpy as np
from matplotlib.patches import Circle

class Producer(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.running = True
        self.q = q
        print 'Producer thread started'
        
    def stop(self):
        """Stop the thread execution."""
        self.running = False
        print 'Producer thread stoped'

    def run(self):
        x = 0
        d = 'up'
        inc = 0.01
        dt = 0.002 # sleep for dt seconds, can we go down to 0.002
        while self.running:
            start = time.time()
            if d == 'up':
                x += inc
            else:
                x -= inc
            if x >= 0.5:
                d = 'down'
            if x <= -1.2:
                d = 'up'
            print q.qsize()
            self.q.put(x)
            s = dt - (time.time() - start)
            if s > 0:
                time.sleep(s)
            else:
                print 'Going too fast!'


height = lambda x: np.sin(3*x)/3.0

def animate(*args):
    if animate.background is None:
        animate.background = canvas.copy_from_bbox(ax.bbox)
    canvas.restore_region(animate.background)

    # Draw circle
    r = 0.05
    x = q.get(True)
    y = height(x) + r
    cir = Circle((x, y), r, animated=True)
    ax.add_patch(cir)
    ax.draw_artist(cir)
    
    # just redraw the axes rectangle
    canvas.blit(ax.bbox)

    return True



if __name__ == "__main__":

    q = Queue.Queue()
    producer = Producer(q)
    producer.setDaemon(True)
    producer.start()


    ax = p.subplot(111)
    canvas = ax.figure.canvas
    x_min, x_max = -1.2, 0.6
    x = np.linspace(x_min, x_max, 100)
    line = p.plot(x, height(x))
    p.axis('scaled')
    p.xlim((x_min,x_max))
    p.ylim((-0.4,0.5))
    p.xticks(())
    p.yticks(())

    animate.cnt = 0
    animate.background = None
    gobject.idle_add(animate)
    p.show()

    try:
        while(1):
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    #print ' '
    producer.stop()
    #plotter.stop()

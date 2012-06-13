# From http://www.scipy.org/Cookbook/Matplotlib/Arrows

from pylab import *
import numpy as np

x = arange(10)
y = x

# Plot junk and then a filled region
plot(x, y)

# Now lets make an arrow object
arr = Arrow(2, 2, 1, 1, edgecolor='white')

# Get the subplot that we are currently working on
ax = gca()

# Now add the arrow
ax.add_patch(arr)

# We should be able to make modifications to the arrow.
# Lets make it green.
arr.set_facecolor('g')

figure()
A = np.random.rand(5,5)
#pcolor(A)
imshow(A, interpolation='nearest')

arr = Arrow(2, 2, 1, 1, edgecolor='white')
ax = gca()
ax.add_patch(arr)

show()

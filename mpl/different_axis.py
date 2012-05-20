## from mpl_toolkits.axes_grid.axislines import SubplotZero
## import matplotlib.pyplot as plt
## import numpy as np

## fig = plt.figure(1)
## ax = SubplotZero(fig, 111)
## fig.add_subplot(ax)

## for direction in ["xzero", "yzero"]:
##     ax.axis[direction].set_axisline_style("-|>")
##     ax.axis[direction].set_visible(True)

## for direction in ["left", "right", "bottom", "top"]:
##     ax.axis[direction].set_visible(False)

## ax.set_xticks([])
## ax.set_yticks([])

## x = np.linspace(0, 2., 100)
## ax.plot(x, np.sin(x*np.pi))

## #fig.savefig('different_axis.pdf')
## plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import Subplot

fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

ax.axis["right"].set_visible(False)
ax.axis["left"].set_visible(False)
ax.axis["top"].set_visible(False)
ax.axis["bottom"].set_visible(False)
x = np.linspace(0, 2., 100)
ax.plot(x, np.sin(x*np.pi))
plt.tight_layout()

fig.savefig('different_axis.pdf')
#plt.show()

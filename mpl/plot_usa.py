# http://www.packtpub.com/article/plotting-geographical-data-using-basemap

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

# Lambert Conformal map of USA lower 48 states
m = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64,urcrnrlat=49, 
	    projection='lcc', lat_1=33, lat_2=45,lon_0=-95, resolution='h',
	    area_thresh=10000)
# draw the coastlines of continental area
m.drawcoastlines()
# draw country boundaries
m.drawcountries(linewidth=2)
# draw states boundaries (America only)
m.drawstates()

# fill the background (the oceans)
m.drawmapboundary(fill_color='aqua')
# fill the continental area
# we color the lakes like the oceans
m.fillcontinents(color='coral',lake_color='aqua')

# draw parallels and meridians
m.drawparallels(np.arange(25,65,20),labels=[1,0,0,0])
m.drawmeridians(np.arange(-120,-40,20),labels=[0,0,0,1])

plt.show()

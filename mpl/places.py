"""Plotting data on a map.

Based on http://sciblogs.co.nz/seeing-data/2011/08/12/plotting-geographic-data-on-a-world-map-with-python/"""

import codecs

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

def get_data():
    #lines = open('places.org').readlines()
    lines = codecs.open('places.org', encoding='utf-8').readlines()
    lats = []
    lngs = []
    names = []
    dates = []
    for line in lines[2:-1]:
        fields = line.split('|')[1:-1]
        f = [f.strip() for f in fields]
        names.append(f[0])
        dates.append(f[1])
        lats.append(float(f[2]))
        lngs.append(float(f[3]))

    return names, dates, lats, lngs

names, dates, lats, lngs = get_data()
plt.figure(figsize=(10,10))
m = Basemap(llcrnrlon=min(lngs)-1, llcrnrlat=min(lats)-1, 
            urcrnrlon=max(lngs)+1, urcrnrlat=max(lats)+1, 
            projection='lcc', lat_1=min(lats), lat_2=max(lats),
            lon_0=np.mean(lngs), resolution='f')

#set a background colour
m.drawmapboundary(fill_color='#85A6D9')

# draw coastlines, country boundaries, fill continents.
m.fillcontinents(color='white',lake_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawcountries(color='#6D5F47', linewidth=.4)
m.drawstates()

# compute the native map projection coordinates for cities
x,y = m(lngs,lats)

m.scatter(
    x,
    y,
    s=40,
    c='red', #color
    marker='o', #symbol
    alpha=0.9, #transparency
    zorder = 2, #plotting order
    )

yoffset = 9000
for name, date, xpt, ypt in zip(names, dates, x, y):
    plt.text(xpt, ypt+yoffset, name, color='blue', size='small', 
             horizontalalignment='center', verticalalignment='center')
    plt.text(xpt, ypt-yoffset, date, color='blue', size='small', 
             horizontalalignment='center', verticalalignment='center')

plt.gcf().subplots_adjust(bottom=0.0, top=1.0, left=0.0, right=1.0)

plt.savefig('map.png')
#plt.show()

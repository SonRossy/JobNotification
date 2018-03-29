'''import matplotlib.pyplot as plt
#echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc to fix framework problem

x=[1,2,3,4,5,6,7]
y=[50,39,70,31,54,60,28]
plt.plot(x,y)
plt.show()'''

from mpl_toolkits.basemap import Basemap

import matplotlib.pyplot as plt
import numpy as np


class Map:
    #lon=0
    #lat=0
    x=0
    y=0
    my_map = Basemap(projection='merc', lat_0=0, lon_0=-100,
        resolution = 'h', area_thresh = .001,
                     llcrnrlon=-73.750482, llcrnrlat=41.126574,
                     urcrnrlon=-69.374912, urcrnrlat=42.945720)
    def __init__(self,lon,lat,town):

        Map.my_map.drawcoastlines()
        Map.my_map.drawcountries()
        Map.my_map.fillcontinents(color='coral')
        Map.my_map.drawmapboundary()
        Map.my_map.drawstates(color='0.5')
        Map.my_map.drawmeridians(np.arange(0, 360, 30))
        Map.my_map.drawparallels(np.arange(-90, 90, 30))

        self.lon = lon#-71.009288
        self.lat = lat#42.0232864
        Map.x,Map.y = Map.my_map(lon, lat)
        Map.my_map.plot(Map.x, Map.y, 'bo', markersize=4)
        plt.text(Map.x + 5000, Map.y + 2500, town,fontsize=6)

    def clearMap(self):
        plt.clf()
        plt.close('all')

    def ShowMap(self):
        plt.show()








from matplotlib import pyplot as plt
from matplotlib import colormaps
from matplotlib.path import Path
from matplotlib.patches import PathPatch

import numpy
import geopandas as gpd
from geopandas import GeoDataFrame
import shapely
from shapely.wkt import loads
import cartagen as c4
from shapely import LineString, Polygon, Point

roads = [
    loads('LINESTRING (286089.52405599627 6248772.534121353, 286109.76992505457 6248731.41758182)'), 
    loads('LINESTRING (286109.76992505457 6248731.41758182, 286132.596661726 6248689.85888561)'), 
    loads('LINESTRING (286278.6978140813 6248768.849275752, 286132.596661726 6248689.85888561)'), 
    loads('LINESTRING (286050.01378114644 6248841.53758973, 286012.1115879562 6248809.991385799, 285964.71245709277 6248767.5919077685)'), 
    loads('LINESTRING (286043.410346802 6248856.410345533, 286050.01378114644 6248841.53758973)'), 
    loads('LINESTRING (286193.30147481844 6248936.185014079, 286166.8323964377 6248922.044527316, 286050.6804344021 6248858.427795238, 286043.410346802 6248856.410345533)'), 
    loads('LINESTRING (286109.55973062315 6249105.509890551, 286089.89724353276 6249094.90517431, 285968.9053079529 6249028.369140927, 285953.3130256142 6249022.502651624)'), 
    loads('LINESTRING (286045.15102391044 6248675.689724563, 286082.13440729363 6248708.751578872, 286109.76992505457 6248731.41758182)'), 
    loads('LINESTRING (286089.52405599627 6248772.534121353, 286050.01378114644 6248841.53758973)'), 
    loads('LINESTRING (285883.66796555324 6248859.034596473, 285930.32203498075 6248898.996753626, 285983.7601517755 6248946.754749412, 285990.710373667 6248951.8131763935)'), 
    loads('LINESTRING (286045.15102391044 6248675.689724563, 285964.71245709277 6248767.5919077685)'), 
    loads('LINESTRING (285931.55302612646 6249062.851215578, 285953.3130256142 6249022.502651624)'), 
    loads('LINESTRING (285990.710373667 6248951.8131763935, 285998.05915342394 6248939.378501368)'), 
    loads('LINESTRING (285964.71245709277 6248767.5919077685, 285958.1561478852 6248773.793326144, 285883.66796555324 6248859.034596473)'), 
    loads('LINESTRING (285998.05915342394 6248939.378501368, 286043.410346802 6248856.410345533)'), 
    loads('LINESTRING (285953.3130256142 6249022.502651624, 285990.710373667 6248951.8131763935)'), 
    loads('LINESTRING (285883.66796555324 6248859.034596473, 285857.8648549033 6248889.775741089, 285829.48208630865 6248920.654884074, 285805.804698632 6248950.951365177)'), 
    loads('LINESTRING (285805.804698632 6248950.951365177, 285798.1003110676 6248945.12798313, 285751.4490925499 6248904.708531565, 285669.78340136725 6248831.996485747)'), 
    loads('LINESTRING (285749.92143442703 6248740.246798143, 285688.87379425025 6248808.369255772)'), 
    loads('LINESTRING (285749.92143442703 6248740.246798143, 285883.66796555324 6248859.034596473)'), 
    loads('LINESTRING (285964.71245709277 6248767.5919077685, 285854.96471502236 6248670.69261535, 285834.2816002494 6248652.780098297, 285829.29275294684 6248649.710147816)'), 
    loads('LINESTRING (285829.29275294684 6248649.710147816, 285819.8370605577 6248659.090144048, 285794.4968361917 6248688.463793473, 285749.92143442703 6248740.246798143)'), 
    loads('LINESTRING (285931.55302612646 6249062.851215578, 285882.33351039106 6249020.287978957, 285805.804698632 6248950.951365177)'), 
    loads('LINESTRING (285805.804698632 6248950.951365177, 285802.73442099674 6248957.6283479985, 285780.793396034 6249086.517534094, 285779.6717179423 6249097.465114155)'), 
    loads('LINESTRING (286132.596661726 6248689.85888561, 286163.85963143973 6248631.003792429, 286191.8932352562 6248580.194084003, 286195.5607374094 6248575.19389688)'), 
    loads('LINESTRING (285909.2774482713 6248557.6558126025, 285914.8688419994 6248561.489620024, 286045.15102391044 6248675.689724563)'), 
    loads('LINESTRING (285950.03087383206 6248511.024400408, 285909.2774482713 6248557.6558126025)'), 
    loads('LINESTRING (285909.2774482713 6248557.6558126025, 285851.1299980136 6248622.903464245, 285829.29275294684 6248649.710147816)'), 
    loads('LINESTRING (285733.1341502332 6248564.751060144, 285829.29275294684 6248649.710147816)'), 
    loads('LINESTRING (285998.05915342394 6248939.378501368, 286004.875070027 6248941.24138955, 286149.1598265071 6249020.074088908)'), 
    loads('LINESTRING (286089.52405599627 6248772.534121353, 286097.2334406795 6248777.44438131, 286133.9875294727 6248796.9655364845, 286188.27852573525 6248827.3834608365, 286236.22634042945 6248852.746283269)'), 
    loads('LINESTRING (285608.46535564004 6248617.308566212, 285749.92143442703 6248740.246798143)'), 
    loads('LINESTRING (286036.8690901173 6248413.379314062, 285982.6936437093 6248473.780490931, 285950.03087383206 6248511.024400408)'), 
    loads('LINESTRING (285931.55302612646 6249062.851215578, 285914.39819657785 6249093.184215673, 285909.4778423428 6249105.3280800525)'), 
    loads('LINESTRING (285870.4942923505 6248521.085021825, 285910.1884989869 6248473.991800982, 285950.03087383206 6248511.024400408)'), 
    loads('LINESTRING (285870.4942923505 6248521.085021825, 285909.2774482713 6248557.6558126025)'), 
    loads('LINESTRING (285816.45182881487 6248473.477415074, 285856.15873036184 6248507.467190041, 285870.4942923505 6248521.085021825)'), 
]

rgdf = gpd.GeoDataFrame([{'geometry': g, 'importance': 1} for g in roads])
strokes = c4.strokes_roads(rgdf, ['importance'])
slist = strokes.to_dict('records')

cmap = colormaps['tab20']
colors = cmap(numpy.linspace(0, 1, len(slist)))

fig = plt.figure(1, (8, 8))

sub1 = fig.add_subplot(111)
sub1.axes.get_xaxis().set_visible(False)
sub1.axes.get_yaxis().set_visible(False)

for i, s in enumerate(slist):
    path = Path(numpy.asarray(s['geometry'].coords)[:, :2])
    sub1.add_patch(PathPatch(path, facecolor="none", edgecolor=colors[i], linewidth=1))

sub1.autoscale_view()
plt.show()
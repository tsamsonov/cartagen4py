from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

import numpy
import geopandas as gpd
import shapely
from shapely.wkt import loads
import cartagen4py as c4

line = loads('LineString (-187600.83164941068389453 5374344.11075404845178127, -187569.47361484216526151 5374348.59047327283769846, -187545.95508891576901078 5374353.07019249629229307, -187519.07677357134525664 5374362.02963094506412745, -187501.1578966750530526 5374375.46878861729055643, -187484.3589495847991202 5374393.38766551297158003, -187478.75930055469507352 5374413.54640202131122351, -187476.51944094264763407 5374435.94499814230948687, -187477.63937074868590571 5374460.58345387410372496, -187483.23901977876084857 5374488.58169902488589287, -187482.11908997275168076 5374506.50057592149823904, -187469.79986210656352341 5374528.89917204156517982, -187454.12084482228965499 5374546.81804893724620342, -187435.08203811998828314 5374555.7774873860180378, -187409.32365258157369681 5374552.41769796796143055, -187394.76456510333810002 5374533.37889126501977444, -187393.64463529732893221 5374512.10022495128214359, -187404.84393335750792176 5374490.82155863661319017, -187419.40302083574351855 5374470.6628221282735467, -187429.48238908991334029 5374443.78450678382068872, -187433.96210831397911534 5374413.54640202131122351, -187437.32189773203572258 5374385.54815687146037817, -187435.08203811998828314 5374362.02963094506412745, -187429.48238908991334029 5374342.99082424212247133, -187413.80337180563947186 5374318.35236851032823324, -187394.76456510333810002 5374298.19363200198858976, -187370.12610937093268149 5374283.63454452343285084, -187344.36772383251809515 5374274.67510607559233904, -187320.84919790615094826 5374274.67510607559233904, -187297.33067197975469753 5374280.27475510537624359, -187281.65165469550993294 5374294.83384258393198252, -187279.41179508346249349 5374308.2730002561584115, -187282.77158450151910074 5374325.07194734644144773, -187296.21074217374552973 5374338.51110501866787672, -187319.72926810014178045 5374342.99082424212247133, -187342.12786422049975954 5374344.11075404845178127, -187364.52646034085773863 5374359.78977133240550756, -187376.84568820704589598 5374378.82857803534716368, -187388.04498626722488552 5374401.22717415541410446, -187393.64463529732893221 5374416.90619143936783075, -187391.40477568528149277 5374449.38415581453591585, -187377.96561801305506378 5374469.54289232287555933, -187365.64639014686690643 5374487.46176921855658293, -187345.48765363855636679 5374500.90092689078301191, -187324.2089873242075555 5374504.26071630883961916, -187307.41004023392451927 5374504.26071630883961916, -187286.13137391957570799 5374494.18134805466979742, -187273.81214605338755064 5374478.50233077071607113, -187255.8932691570953466 5374450.50408561993390322, -187242.45411148486891761 5374429.22541930619627237, -187222.29537497655837797 5374411.3065424095839262, -187203.25656827425700612 5374404.58696357347071171, -187173.01846351174754091 5374401.22717415541410446, -187148.38000777937122621 5374404.58696357347071171)')
fig = plt.figure(1, (8, 20))
width = { 0: 2, 1: 6, 2: 12 }

#############################################################

tolerance = 10

sub1 = fig.add_subplot(311)
sub1.set_title('a) Tolerance = {0}'.format(tolerance), pad=10, family='sans-serif')
sub1.axes.get_xaxis().set_visible(False)
sub1.axes.get_yaxis().set_visible(False)

left, right = None, None
lines = c4.detect_pastiness(line, tolerance)
right = shapely.offset_curve(line, tolerance)
left = shapely.offset_curve(line, -tolerance)

path1 = Path(numpy.asarray(right.coords)[:, :2])
path2 = Path(numpy.asarray(left.coords)[:, :2])
sub1.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))
sub1.add_patch(PathPatch(path2, facecolor="none", edgecolor='gray', linewidth=1))

for i, l in enumerate(lines):
    path3 = Path(numpy.asarray(l['geometry'].coords)[:, :2])
    sub1.add_patch(PathPatch(path3, facecolor="none", edgecolor='red', linewidth=width[l['paste']]))

sub1.autoscale_view()

#############################################################

tolerance = 20

sub2 = fig.add_subplot(312)
sub2.set_title('b) Tolerance = {0}'.format(tolerance), pad=10, family='sans-serif')
sub2.axes.get_xaxis().set_visible(False)
sub2.axes.get_yaxis().set_visible(False)

left, right = None, None
lines = c4.detect_pastiness(line, tolerance)
right = shapely.offset_curve(line, tolerance)
left = shapely.offset_curve(line, -tolerance)

path1 = Path(numpy.asarray(right.coords)[:, :2])
path2 = Path(numpy.asarray(left.coords)[:, :2])
sub2.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))
sub2.add_patch(PathPatch(path2, facecolor="none", edgecolor='gray', linewidth=1))

for i, l in enumerate(lines):
    path3 = Path(numpy.asarray(l['geometry'].coords)[:, :2])
    sub2.add_patch(PathPatch(path3, facecolor="none", edgecolor='red', linewidth=width[l['paste']]))

sub2.autoscale_view()

#############################################################

tolerance = 50

sub3 = fig.add_subplot(313)
sub3.set_title('c) Tolerance = {0}'.format(tolerance), pad=10, family='sans-serif')
sub3.axes.get_xaxis().set_visible(False)
sub3.axes.get_yaxis().set_visible(False)

left, right = None, None
lines = c4.detect_pastiness(line, tolerance)
right = shapely.offset_curve(line, tolerance)
left = shapely.offset_curve(line, -tolerance)

path1 = Path(numpy.asarray(right.coords)[:, :2])
path2 = Path(numpy.asarray(left.coords)[:, :2])
sub3.add_patch(PathPatch(path1, facecolor="none", edgecolor='gray', linewidth=1))
sub3.add_patch(PathPatch(path2, facecolor="none", edgecolor='gray', linewidth=1))

for i, l in enumerate(lines):
    path3 = Path(numpy.asarray(l['geometry'].coords)[:, :2])
    sub3.add_patch(PathPatch(path3, facecolor="none", edgecolor='red', linewidth=width[l['paste']]))

sub3.autoscale_view()

plt.show()
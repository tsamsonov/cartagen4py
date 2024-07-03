from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

import numpy
import geopandas as gpd
import shapely
from shapely.wkt import loads
import cartagen4py as c4

polygons1 = [
    loads('Polygon ((282499.15896787942619994 6246577.45513126626610756, 282490.77501181280240417 6246584.85843994375318289, 282482.2314042717916891 6246593.62964459881186485, 282490.8307609727489762 6246601.28479254059493542, 282508.38265443232376128 6246582.0720604807138443, 282527.38259279477642849 6246574.57894805353134871, 282522.90069882478564978 6246562.99362337775528431, 282507.38949021481676027 6246570.3551049679517746, 282499.15896787942619994 6246577.45513126626610756))'),
    loads('Polygon ((282655.09644928277703002 6246492.13325823657214642, 282645.66182592819677666 6246497.70539804641157389, 282630.29273740161443129 6246506.74087824299931526, 282614.46691543055931106 6246516.07784821186214685, 282600.92191640194505453 6246524.36352359503507614, 282574.44550930592231452 6246539.72169733326882124, 282561.50967246165964752 6246547.55462960060685873, 282554.21213717135833576 6246550.70576493721455336, 282539.01402264443458989 6246556.39611408114433289, 282526.85409722098847851 6246561.19171635527163744, 282522.90069882478564978 6246562.99362337775528431, 282527.38259279477642849 6246574.57894805353134871, 282537.56672388414153829 6246570.53220799658447504, 282541.82962066592881456 6246567.66746176220476627, 282548.50818032352253795 6246566.64199272263795137, 282557.01622470672009513 6246563.95423283521085978, 282595.82197823619935662 6246540.75954940635710955, 282642.08107663987902924 6246513.65402083192020655, 282662.01539257436525077 6246501.90759082045406103, 282655.09644928277703002 6246492.13325823657214642))'),
    loads('Polygon ((282724.9445644092047587 6246450.56480667740106583, 282704.39857288071652874 6246463.22027701325714588, 282675.94321050320286304 6246479.93589389137923717, 282661.0308829503483139 6246488.66990009602159262, 282655.09644928277703002 6246492.13325823657214642, 282662.01539257436525077 6246501.90759082045406103, 282683.16633796418318525 6246489.55988507438451052, 282702.34056207479443401 6246478.11313065979629755, 282713.44319861702388152 6246472.55069546867161989, 282721.71548622305272147 6246484.31005388684570789, 282729.23046403838088736 6246495.91290224902331829, 282740.53477766981814057 6246507.84208715613931417, 282756.07100765727227554 6246522.22946271020919085, 282763.9184963388252072 6246528.81524563021957874, 282773.43231260468019173 6246535.71494169533252716, 282781.55684216966619715 6246520.70530943106859922, 282775.06089339515892789 6246516.40881332661956549, 282769.02253053092863411 6246511.65871283784508705, 282765.39986920647788793 6246508.74781729094684124, 282763.13670071098022163 6246506.75741036795079708, 282757.70669044705573469 6246501.70667825825512409, 282752.58262288302648813 6246496.2014596750959754, 282747.76273128011962399 6246490.54592775274068117, 282743.24701529974117875 6246484.74008328560739756, 282739.03635820018826053 6246478.63184136152267456, 282734.82924173708306625 6246471.91525936406105757, 282731.07882701617199928 6246464.8971685990691185, 282727.93498816550709307 6246457.88262739777565002, 282724.9445644092047587 6246450.56480667740106583))'),
    loads('Polygon ((282879.62448553048307076 6246555.34597144741564989, 282873.19368120637955144 6246539.7951055783778429, 282862.87660719844279811 6246540.64751519076526165, 282862.11750612751347944 6246540.79518154915422201, 282851.04573704744689167 6246541.03480982314795256, 282840.13090262992773205 6246540.36278807651251554, 282833.16057510464452207 6246539.40957946423441172, 282826.79417820833623409 6246538.91616435814648867, 282821.03788638167316094 6246537.81793704908341169, 282814.98271993017988279 6246535.95750293880701065, 282808.32362817507237196 6246533.6372651094570756, 282801.51554384717019275 6246530.85987795237451792, 282794.70834648195886984 6246527.93039985373616219, 282788.0554456384270452 6246524.54554338939487934, 282781.55684216966619715 6246520.70530943106859922, 282773.43231260468019173 6246535.71494169533252716, 282782.50445522315567359 6246540.33067507669329643, 282791.12608908745460212 6246544.18331148568540812, 282803.83329420804511756 6246549.58070843946188688, 282804.13658232754096389 6246549.58247862476855516, 282818.21654101350577548 6246553.61904090642929077, 282834.12682696391129866 6246555.84115317184478045, 282850.04152954171877354 6246557.30280190519988537, 282860.04916507570305839 6246557.51324677187949419, 282879.62448553048307076 6246555.34597144741564989))'),
    loads('Polygon ((283021.72929129039403051 6246422.48502456583082676, 283006.62223733041901141 6246412.51137781981378794, 282996.51805312314536422 6246429.03042147681117058, 282993.76124092983081937 6246433.72918115649372339, 282990.69938289921265095 6246438.73034878727048635, 282987.63752139458665624 6246443.73151816893368959, 282984.11457360477652401 6246449.79463978577405214, 282979.9806537606054917 6246456.61466257553547621, 282975.84672752034384757 6246463.43468866031616926, 282971.86619681783486158 6246469.95142911653965712, 282968.19158489210531116 6246476.01368007343262434, 282964.21368208341300488 6246482.07416901551187038, 282959.6265622602077201 6246488.58738833107054234, 282954.73790920100873336 6246494.79467312432825565, 282949.39519954315619543 6246500.84722575545310974, 282944.05776311468798667 6246505.98726222664117813, 282938.41791383072268218 6246510.97344665694981813, 282932.17236449004849419 6246515.80401246342808008, 282925.77692555275280029 6246520.32952065020799637, 282918.77666653011692688 6246524.54732111934572458, 282911.17158728680806234 6246528.4574119821190834, 282903.87419279507594183 6246531.60883167013525963, 282896.73107964056544006 6246534.30486994236707687, 282889.74313010642072186 6246536.39344007987529039, 282883.21363347989972681 6246537.87630946841090918, 282873.19368120637955144 6246539.7951055783778429, 282879.62448553048307076 6246555.34597144741564989, 282891.16530048317508772 6246552.67556576523929834, 282905.90384541935054585 6246547.74239273741841316, 282918.82440746936481446 6246542.49442702438682318, 282930.53884589835070074 6246536.02268873155117035, 282943.01764657499734312 6246528.49074704758822918, 282952.00686361943371594 6246521.24266938120126724, 282957.20145983475958928 6246514.58087353128939867, 282970.01252240582834929 6246502.03183384146541357, 282984.38570757978595793 6246481.58315044641494751, 283021.72929129039403051 6246422.48502456583082676))'),
]

polygons2 = [
    loads('Polygon ((282544.57456752733560279 6246397.01512306649237871, 282535.39514282363234088 6246402.42301416397094727, 282520.02605429704999551 6246411.45849436055868864, 282504.20023232599487528 6246420.79546432942152023, 282490.65523329738061875 6246429.08113971259444952, 282495.82767515687737614 6246439.45806225761771202, 282531.81439353531459346 6246418.37163694947957993, 282551.49351081892382354 6246406.78945565037429333, 282544.57456752733560279 6246397.01512306649237871))'),    
    loads('Polygon ((282614.42268265376333147 6246355.44667150732129812, 282593.87669112527510151 6246368.10214184317737818, 282565.42132874776143581 6246384.81775872129946947, 282550.50900119490688667 6246393.55176492594182491, 282544.57456752733560279 6246397.01512306649237871, 282551.49351081892382354 6246406.78945565037429333, 282572.64445620874175802 6246394.44174990430474281, 282591.81868031935300678 6246382.99499548971652985, 282602.92131686158245429 6246377.43256029859185219, 282611.19360446761129424 6246389.19191871676594019, 282618.70858228293946013 6246400.79476707894355059, 282630.01289591437671334 6246412.72395198605954647, 282645.54912590183084831 6246427.11132754012942314, 282653.39661458338377997 6246433.69711046013981104, 282662.91043084923876449 6246440.59680652525275946, 282671.03496041422476992 6246425.58717426098883152, 282664.53901163971750066 6246421.29067815653979778, 282658.50064877548720688 6246416.54057766776531935, 282654.8779874510364607 6246413.62968212086707354, 282652.6148189555387944 6246411.63927519787102938, 282647.18480869161430746 6246406.58854308817535639, 282642.06074112758506089 6246401.0833245050162077, 282637.24084952467819676 6246395.42779258266091347, 282632.72513354429975152 6246389.62194811552762985, 282628.51447644474683329 6246383.51370619144290686, 282624.62810869567329064 6246376.92328989040106535, 282620.77717204915825278 6246368.78818622417747974, 282614.42268265376333147 6246355.44667150732129812))'),    
    loads('Polygon ((282671.03496041422476992 6246425.58717426098883152, 282662.91043084923876449 6246440.59680652525275946, 282679.16334696544799954 6246451.58865401428192854, 282683.74234324105782434 6246454.5401196014136076, 282688.6106868609203957 6246457.80904643889516592, 282693.47903208428760991 6246461.07797682099044323, 282699.38905576622346416 6246464.85212903656065464, 282706.02968864951981232 6246469.26846224907785654, 282712.67032455647131428 6246473.68480198923498392, 282719.01437556889140978 6246477.93516051582992077, 282729.81791436165804043 6246465.01373123470693827, 282671.03496041422476992 6246425.58717426098883152))'),    
    loads('Polygon ((282692.77713823242811486 6246286.64091852214187384, 282676.06748780253110453 6246284.64786658994853497, 282671.767015871766489 6246294.06458360888063908, 282671.52470307162730023 6246294.79897062946110964, 282666.32070542144356295 6246304.57444507908076048, 282660.39816730207530782 6246313.76731002051383257, 282656.15882531477836892 6246319.3817603038623929, 282652.61584265826968476 6246324.69417423661798239, 282648.84354257601080462 6246329.17867542523890734, 282644.26021987030981109 6246333.55125004705041647, 282638.98053153156070039 6246338.22585138026624918, 282633.22921160253463313 6246342.80692229326814413, 282627.34565068519441411 6246347.31286157667636871, 282621.14028236753074452 6246351.46156582608819008, 282614.42268265376333147 6246355.44667150732129812, 282620.77717204915825278 6246368.78818622417747974, 282630.71740226808469743 6246363.92637870740145445, 282641.20800424186745659 6246357.27355153579264879, 282650.69325164629844949 6246349.93775437865406275, 282650.84307467954931781 6246349.6740502342581749, 282661.24807016475824639 6246339.36506674345582724, 282670.96510756964562461 6246326.57232794258743525, 282680.02092343772528693 6246313.4039425402879715, 282685.09727740212110803 6246304.77679431717842817, 282692.77713823242811486 6246286.64091852214187384))'),    
    loads('Polygon ((282684.08596880937693641 6246255.42172588501125574, 282680.29520304797915742 6246270.22376361768692732, 282676.06748780253110453 6246284.64786658994853497, 282692.77713823242811486 6246286.64091852214187384, 282696.64471869438420981 6246273.9888960113748908, 282700.90974828385515139 6246258.88756886497139931, 282704.91712923173326999 6246247.1903488002717495, 282710.04368864244315773 6246233.83241230808198452, 282692.42565348459174857 6246230.3665693262591958, 282687.66011938446899876 6246243.36348050832748413, 282684.08596880937693641 6246255.42172588501125574))'),    
]

entries1 = [
    loads('Point (283014.17576431040652096 6246417.49820119328796864)'),
    loads('Point (282486.0454146628617309 6246597.02487691771239042)'),
]

entries2 = [
    loads('Point (282493.24145422712899745 6246434.26960098557174206)'),
    loads('Point (282724.41614496527472511 6246471.47444587573409081)'),
    loads('Point (282701.23467106348834932 6246232.09949081763625145)'),
]

structural = [
    loads('Point (282718.53675920091336593 6246463.61226381175220013)')
]

# fig = plt.figure(1, (12, 12))

f, axs = plt.subplots(3, 1, figsize=(12, 16), gridspec_kw={'height_ratios': [1, 1, 3]})

#############################################################

# sub1 = fig.add_subplot(311)
axs[0].set_title('densify=10.0 sigma=5.0 without structural point', pad=10, family='sans-serif')
axs[0].axes.get_xaxis().set_visible(False)
axs[0].axes.get_yaxis().set_visible(False)

# sub2 = fig.add_subplot(312)
axs[1].set_title('densify=10.0 sigma=5.0 with structural point', pad=10, family='sans-serif')
axs[1].axes.get_xaxis().set_visible(False)
axs[1].axes.get_yaxis().set_visible(False)

# sub3 = fig.add_subplot(313)
axs[2].set_title('densify=10.0 sigma=5.0 with multiple entries', pad=10, family='sans-serif')
axs[2].axes.get_xaxis().set_visible(False)
axs[2].axes.get_yaxis().set_visible(False)

generalized1 = c4.spinalize_polygons(polygons1, 10.0, 5.0, entries1)
generalized2 = c4.spinalize_polygons(polygons1, 10.0, 5.0, entries1, structural)
generalized3 = c4.spinalize_polygons(polygons2, 10.0, 5.0, entries2)

for s in structural:
    coords = s.coords[0]
    axs[1].plot(coords[0], coords[1], linestyle="", marker='o', color="black")

for polygon in polygons1:
    poly = Path.make_compound_path(Path(numpy.asarray(polygon.exterior.coords)[:, :2]),*[Path(numpy.asarray(ring.coords)[:, :2]) for ring in polygon.interiors])
    axs[0].add_patch(PathPatch(poly, facecolor="lightgray", edgecolor='gray'))
    axs[1].add_patch(PathPatch(poly, facecolor="lightgray", edgecolor='gray'))

for polygon in polygons2:
    poly = Path.make_compound_path(Path(numpy.asarray(polygon.exterior.coords)[:, :2]),*[Path(numpy.asarray(ring.coords)[:, :2]) for ring in polygon.interiors])
    axs[2].add_patch(PathPatch(poly, facecolor="lightgray", edgecolor='gray'))

for g in generalized1:
    path = Path(numpy.asarray(g.coords)[:, :2])
    axs[0].add_patch(PathPatch(path, facecolor="none", edgecolor='red', linewidth=1))

for g in generalized2:
    path = Path(numpy.asarray(g.coords)[:, :2])
    axs[1].add_patch(PathPatch(path, facecolor="none", edgecolor='red', linewidth=1))

for g in generalized3:
    path = Path(numpy.asarray(g.coords)[:, :2])
    axs[2].add_patch(PathPatch(path, facecolor="none", edgecolor='red', linewidth=1))

for e in entries1:
    coords = e.coords[0]
    axs[0].plot(coords[0], coords[1], linestyle="", marker='o', color="red")
    axs[1].plot(coords[0], coords[1], linestyle="", marker='o', color="red")

for e in entries2:
    coords = e.coords[0]
    axs[2].plot(coords[0], coords[1], linestyle="", marker='o', color="red")

axs[0].autoscale_view()
axs[1].autoscale_view()
axs[2].autoscale_view()

plt.show()
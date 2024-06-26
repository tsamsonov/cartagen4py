from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

import numpy
import geopandas as gpd
import shapely
from shapely.wkt import loads
import cartagen4py as c4

buildings = [
    loads('POLYGON ((483057.0001325076 6044715.46326518, 483053.9911464997 6044721.610737422, 483057.5754359291 6044723.185334679, 483059.72542895144 6044718.836751607, 483061.66199559974 6044719.398557046, 483060.5869339536 6044717.186506892, 483057.0001325076 6044715.46326518))'), 
    loads('POLYGON ((483171.73067271145 6044767.782133036, 483173.531642804 6044769.08967847, 483176.13120330864 6044765.030768621, 483175.52836410323 6044764.446273002, 483177.41714487784 6044762.1837528255, 483175.3122402412 6044760.435314047, 483173.7097833733 6044762.098196121, 483172.95875071577 6044761.516224115, 483170.0753812122 6044766.32341632, 483171.73067271145 6044767.782133036))'), 
    loads('POLYGON ((483105.32055118814 6044811.587025419, 483106.76477616996 6044809.332075808, 483103.4642585212 6044807.009197152, 483101.2941480392 6044810.168647503, 483104.7403462389 6044812.340356994, 483105.32055118814 6044811.587025419))'), 
    loads('POLYGON ((483104.5039601318 6044798.367422216, 483094.6527179778 6044794.37175113, 483092.37464560085 6044799.912087187, 483095.8158084017 6044801.786501303, 483092.7917327151 6044807.042156996, 483097.8806417652 6044809.929365149, 483104.5039601318 6044798.367422216))'), 
    loads('POLYGON ((483142.1782609609 6044808.431834565, 483141.8894178646 6044808.882825581, 483139.00601593126 6044813.6900332235, 483145.15746150253 6044818.046039145, 483148.9149366745 6044812.331797865, 483142.1782609609 6044808.431834565))'), 
    loads('POLYGON ((483234.89086754667 6044750.945189177, 483235.6242848181 6044750.486624118, 483240.3211739695 6044747.730183541, 483236.06100859726 6044741.260398631, 483234.0866723846 6044738.468923797, 483229.25921056326 6044742.2684126785, 483234.89086754667 6044750.945189177))'), 
    loads('POLYGON ((483240.3211739695 6044747.730183541, 483241.79052437807 6044746.961700034, 483237.67603477 6044740.340744607, 483236.06100859726 6044741.260398631, 483240.3211739695 6044747.730183541))'), 
    loads('POLYGON ((483098.3686514658 6044847.539992377, 483105.72794331907 6044835.668090232, 483104.37658435403 6044834.650251181, 483097.01729153056 6044846.522150829, 483098.3686514658 6044847.539992377))'), 
    loads('POLYGON ((483106.61675895256 6044818.107375301, 483113.21026127273 6044822.3071898315, 483117.5504781167 6044815.988275172, 483112.0044006726 6044812.365402377, 483111.7130410366 6044812.667744236, 483110.6631039522 6044811.942160351, 483109.073199646 6044814.34828218, 483106.61675895256 6044818.107375301))'), 
    loads('POLYGON ((483128.8589503981 6044836.017797892, 483124.81995683233 6044833.856183282, 483121.37142234127 6044840.30862671, 483121.9692330464 6044840.595833392, 483120.3893867485 6044843.596560537, 483123.6823773161 6044845.473495658, 483125.1291182548 6044843.367183282, 483125.8776396122 6044843.8005158715, 483130.3534771165 6044836.735812908, 483128.8589503981 6044836.017797892))'), 
    loads('POLYGON ((483115.83538780437 6044837.280341479, 483121.37142234127 6044840.30862671, 483124.81995683233 6044833.856183282, 483125.82714079326 6044832.054739282, 483120.60007494414 6044829.764657445, 483119.01268513204 6044832.3194346, 483115.83538780437 6044837.280341479))'), 
    loads('POLYGON ((483161.34087954287 6044819.554784112, 483155.3501976635 6044815.9395075, 483151.7583064368 6044813.918988647, 483148.9149366745 6044812.331797865, 483145.15746150253 6044818.046039145, 483151.1556872388 6044822.107269101, 483157.45533959445 6044826.460747283, 483161.34087954287 6044819.554784112))'), 
    loads('POLYGON ((483079.7071106999 6044760.873352173, 483077.4265233104 6044766.26501583, 483083.7160418289 6044770.023928969, 483087.03146913846 6044764.465958939, 483084.78844561946 6044763.314610256, 483084.3564359738 6044764.065414287, 483080.3225149269 6044762.201091747, 483080.75452482456 6044761.450288072, 483079.7071106999 6044760.873352173))'), 
    loads('POLYGON ((483107.42293936125 6044813.186842711, 483109.16355339176 6044810.926847308, 483106.76477616996 6044809.332075808, 483105.32055118814 6044811.587025419, 483107.42293936125 6044813.186842711))'), 
    loads('POLYGON ((483130.6090203363 6044808.034034065, 483127.56735730194 6044812.24916695, 483125.84435347153 6044815.549705131, 483127.0424869818 6044816.272764664, 483127.33133107953 6044815.821773763, 483130.4761179819 6044817.701223285, 483133.36204111023 6044813.042664639, 483134.8037439027 6044810.639061716, 483130.6090203363 6044808.034034065))'), 
    loads('POLYGON ((483083.11633892223 6044804.679077217, 483081.70479533303 6044808.866449537, 483084.83951237344 6044810.151320628, 483086.84634746565 6044806.102506898, 483083.11633892223 6044804.679077217))'), 
    loads('POLYGON ((483210.89663125953 6044690.837229467, 483208.16373625735 6044687.017861997, 483192.8199110532 6044700.06647091, 483192.23720472516 6044700.671152347, 483201.02362804476 6044711.821900184, 483197.07777593815 6044715.160275464, 483190.2309632467 6044722.265297914, 483187.90264700353 6044724.832675909, 483183.01755713107 6044733.98594851, 483189.5005818837 6044740.417896265, 483201.7022280462 6044725.638476998, 483219.3869723985 6044710.765665825, 483223.1846212015 6044707.429806574, 483210.89663125953 6044690.837229467))'), 
    loads('POLYGON ((483142.7452454111 6044780.616987641, 483147.5501263576 6044775.479700332, 483141.6850358256 6044770.524080259, 483137.485506864 6044776.394508247, 483142.7452454111 6044780.616987641))'), 
    loads('POLYGON ((483093.1897420853 6044734.177057238, 483100.39103695785 6044739.25863552, 483102.2697728708 6044736.401549589, 483095.0659646853 6044731.171327485, 483093.1897420853 6044734.177057238))'), 
    loads('POLYGON ((483140.9423733881 6044700.355098594, 483127.1583237527 6044717.986430303, 483129.5621100949 6044719.878473403, 483130.91345437674 6044720.896295404, 483144.3985999802 6044703.121351666, 483143.19796505576 6044702.249657222, 483140.9423733881 6044700.355098594))'), 
    loads('POLYGON ((483223.3437616396 6044734.339924972, 483228.316898136 6044730.389271281, 483220.75371669483 6044721.4480342595, 483216.0920678544 6044726.285512336, 483218.20703898 6044728.628522268, 483218.64658542944 6044728.323655383, 483223.3437616396 6044734.339924972))'), 
    loads('POLYGON ((483099.8682070101 6044848.555311461, 483107.37820758845 6044836.82953296, 483105.72794331907 6044835.668090232, 483098.3686514658 6044847.539992377, 483099.8682070101 6044848.555311461))'), 
    loads('POLYGON ((483097.48400406 6044821.534031089, 483094.7888364298 6044819.944299052, 483093.2064700234 6044822.796365772, 483096.499447036 6044824.673306711, 483097.48400406 6044821.534031089))'), 
    loads('POLYGON ((483109.073199646 6044814.34828218, 483110.6631039522 6044811.942160351, 483109.16355339176 6044810.926847308, 483107.42293936125 6044813.186842711, 483109.073199646 6044814.34828218))'), 
    loads('POLYGON ((483058.9413361998 6044690.004361436, 483053.9981878555 6044686.966001866, 483052.5640247624 6044689.815496949, 483057.5021463714 6044692.556565563, 483058.9413361998 6044690.004361436))'), 
    loads('POLYGON ((483027.10834972584 6044762.36309812, 483023.44632483885 6044773.7258671485, 483027.3320450408 6044775.592739422, 483052.74877314846 6044788.393771067, 483055.47899179836 6044783.291831341, 483058.78187207115 6044776.990624751, 483042.4653241705 6044767.603369862, 483030.23298835737 6044763.053391764, 483027.10834972584 6044762.36309812))'), 
    loads('POLYGON ((483061.66199559974 6044719.398557046, 483059.72542895144 6044718.836751607, 483057.5754359291 6044723.185334679, 483064.4576883069 6044726.934156859, 483067.4792393115 6044721.529911549, 483067.33104614017 6044721.53243334, 483066.42931672005 6044720.80432982, 483066.28112356056 6044720.80685159, 483061.66199559974 6044719.398557046))'), 
    loads('POLYGON ((483055.43046857446 6044727.831213265, 483061.41350762954 6044731.000581244, 483061.9861689115 6044729.801318467, 483062.73467752436 6044730.2346509, 483064.4576883069 6044726.934156859, 483057.5754359291 6044723.185334679, 483055.43046857446 6044727.831213265))'), 
    loads('POLYGON ((483092.1069642058 6044722.7463748325, 483077.6993907521 6044712.285927175, 483074.52211343485 6044717.246751961, 483064.3243086347 6044710.283193461, 483061.73728278605 6044715.085278778, 483073.8817160446 6044723.20523448, 483086.7545662068 6044730.569335204, 483092.1069642058 6044722.7463748325))'), 
    loads('POLYGON ((483075.5772112642 6044727.042312979, 483072.5355498616 6044731.25738828, 483066.092842343 6044727.20371142, 483063.9353083043 6044731.106359119, 483079.5158726978 6044740.803439787, 483085.0215054804 6044733.275246795, 483075.5772112642 6044727.042312979))'), 
    loads('POLYGON ((483061.41350762954 6044731.000581244, 483058.38943571475 6044736.2561831325, 483053.90592496627 6044734.102125064, 483052.61491991195 6044736.651819506, 483056.9527521 6044738.957047618, 483057.23908332223 6044738.357415822, 483062.4761345918 6044741.242100556, 483075.34145885386 6044748.160291117, 483079.5158726978 6044740.803439787, 483063.9353083043 6044731.106359119, 483062.73467752436 6044730.2346509, 483061.9861689115 6044729.801318467, 483061.41350762954 6044731.000581244))'), 
    loads('POLYGON ((483051.57253823796 6044736.372176055, 483042.79416225024 6044751.985297166, 483045.33356482134 6044753.131612279, 483053.2557056222 6044757.011453305, 483056.28732946294 6044752.2017829735, 483068.25595968484 6044758.689179684, 483068.8537631257 6044758.976387347, 483071.596534219 6044754.6176964985, 483059.0301046609 6044747.843099387, 483062.18980363215 6044741.841732717, 483056.9527521 6044738.957047618, 483052.61491991195 6044736.651819506, 483051.718217829 6044736.221007424, 483051.57253823796 6044736.372176055))'), 
    loads('POLYGON ((483045.33356482134 6044753.131612279, 483041.74435093405 6044760.0324295815, 483045.4743339106 6044761.455869712, 483061.79590166657 6044771.140407851, 483065.3876184544 6044764.388221262, 483053.2557056222 6044757.011453305, 483045.33356482134 6044753.131612279))'), 
    loads('POLYGON ((483092.1069642058 6044722.7463748325, 483097.75322420575 6044714.76972676, 483080.2084635903 6044702.875794964, 483064.03268064436 6044693.040197529, 483062.3147043292 6044696.637971736, 483068.9055805965 6044700.689115598, 483070.3774522442 6044700.069311393, 483081.3111859805 6044706.722951552, 483077.6993907521 6044712.285927175, 483092.1069642058 6044722.7463748325))'), 
    loads('POLYGON ((483076.57640775223 6044698.476927384, 483084.36037784896 6044702.953824446, 483099.20497914834 6044712.960743081, 483104.8487117394 6044704.835452673, 483082.2075802499 6044689.608433236, 483082.64210077235 6044689.006281912, 483075.4433713921 6044684.073364044, 483073.5772088796 6044687.673658739, 483080.6202045469 6044692.163163077, 483076.57640775223 6044698.476927384))'), 
    loads('POLYGON ((483075.34145885386 6044748.160291117, 483062.4761345918 6044741.242100556, 483062.18980363215 6044741.841732717, 483059.0301046609 6044747.843099387, 483071.596534219 6044754.6176964985, 483075.34145885386 6044748.160291117))'), 
    loads('POLYGON ((483029.50699906633 6044755.185159507, 483028.7987052173 6044757.130181995, 483044.1782949828 6044763.70827564, 483042.4653241705 6044767.603369862, 483058.78187207115 6044776.990624751, 483061.79590166657 6044771.140407851, 483045.4743339106 6044761.455869712, 483041.74435093405 6044760.0324295815, 483029.50699906633 6044755.185159507))'), 
    loads('POLYGON ((483096.7768934701 6044753.445705255, 483092.1604210931 6044760.958789463, 483097.4000118249 6044763.99210823, 483092.7885635301 6044771.802497061, 483087.39826133876 6044768.623047379, 483085.8108729142 6044771.177800914, 483083.7160418289 6044770.023928969, 483077.4265233104 6044766.26501583, 483077.14270682633 6044767.0132977795, 483074.7466072818 6044774.339906729, 483072.4936695409 6044781.366703478, 483070.00719355507 6044792.114748905, 483072.68977718946 6044792.961243324, 483088.0493464834 6044798.350101392, 483090.13664136606 6044799.058031549, 483092.37464560085 6044799.912087187, 483094.6527179778 6044794.37175113, 483104.5039601318 6044798.367422216, 483105.9959637177 6044798.9367902065, 483109.57759867696 6044791.589972285, 483107.62592436513 6044790.136284896, 483111.96109964827 6044783.520100163, 483113.2621539414 6044781.564974856, 483111.90828753717 6044780.398495349, 483118.1121330976 6044770.330624685, 483115.11555967305 6044768.448658151, 483115.8313801609 6044766.949568982, 483112.5233313864 6044764.1807621755, 483112.66398065264 6044763.73229697, 483111.4608257633 6044762.711944694, 483096.7768934701 6044753.445705255))'), 
    loads('POLYGON ((483078.0505133942 6044829.448034678, 483087.54473305494 6044812.335647403, 483089.91584811383 6044812.295292565, 483092.7917327151 6044807.042156996, 483095.8158084017 6044801.786501303, 483092.37464560085 6044799.912087187, 483090.13664136606 6044799.058031549, 483087.27333005215 6044805.054402699, 483086.84634746565 6044806.102506898, 483084.83951237344 6044810.151320628, 483081.70479533303 6044808.866449537, 483083.11633892223 6044804.679077217, 483083.254475945 6044804.081962208, 483071.03463936324 6044800.275263143, 483068.9473457263 6044799.567328335, 483068.17885705805 6044806.717573691, 483068.9374290838 6044807.7455025045, 483070.4244036197 6044808.01758055, 483066.5188222174 6044822.507088568, 483078.0505133942 6044829.448034678))'), 
    loads('POLYGON ((483082.43365671404 6044834.42895115, 483096.7177160998 6044811.287378718, 483097.0166200621 6044811.430982431, 483097.8806417652 6044809.929365149, 483092.7917327151 6044807.042156996, 483089.91584811383 6044812.295292565, 483087.54473305494 6044812.335647403, 483078.0505133942 6044829.448034678, 483077.18900069164 6044831.098301989, 483082.43365671404 6044834.42895115))'), 
    loads('POLYGON ((483071.03463936324 6044800.275263143, 483083.254475945 6044804.081962208, 483083.11633892223 6044804.679077217, 483086.84634746565 6044806.102506898, 483087.27333005215 6044805.054402699, 483085.62810322904 6044804.190256791, 483088.0493464834 6044798.350101392, 483072.68977718946 6044792.961243324, 483071.03463936324 6044800.275263143))'), 
    loads('POLYGON ((483084.78844561946 6044763.314610256, 483087.03146913846 6044764.465958939, 483089.9148833117 6044759.658795069, 483092.1604210931 6044760.958789463, 483096.7768934701 6044753.445705255, 483086.8879885458 6044747.220336333, 483082.27905406605 6044755.179352275, 483080.13912058505 6044760.12254864, 483079.7071106999 6044760.873352173, 483080.75452482456 6044761.450288072, 483080.3225149269 6044762.201091747, 483084.3564359738 6044764.065414287, 483084.78844561946 6044763.314610256))'), 
    loads('POLYGON ((483023.22562098654 6044804.508607155, 483037.5327358119 6044809.023318186, 483040.484060477 6044808.229649895, 483047.5093018842 6044794.133170573, 483024.0366829568 6044782.339876796, 483022.5221610227 6044789.20541362, 483027.8998851591 6044791.641670377, 483024.9386074685 6044800.613500492, 483023.22562098654 6044804.508607155))'), 
    loads('POLYGON ((483110.7704894864 6044660.574024422, 483106.71666980366 6044666.293196495, 483100.71605589736 6044662.0833616005, 483096.38093188446 6044668.699450213, 483095.78313366754 6044668.412247353, 483082.64210077235 6044689.006281912, 483096.28353233763 6044697.992840808, 483110.0198312339 6044677.537321054, 483119.4640967709 6044683.7701829765, 483125.25346933433 6044675.493737441, 483116.266359923 6044669.996549601, 483118.84831295215 6044664.897180813, 483111.2075214428 6044660.120519456, 483110.7704894864 6044660.574024422))'), 
    loads('POLYGON ((483110.6631039522 6044811.942160351, 483111.7130410366 6044812.667744236, 483112.0044006726 6044812.365402377, 483115.9000297531 6044806.054063313, 483119.51435428584 6044800.639661312, 483109.7786044192 6044794.709058521, 483107.49048228876 6044799.654806121, 483106.63652234327 6044801.7510153195, 483105.8880055015 6044801.317683139, 483102.8664506961 6044806.721990296, 483103.4642585212 6044807.009197152, 483106.76477616996 6044809.332075808, 483109.16355339176 6044810.926847308, 483110.6631039522 6044811.942160351))'), 
    loads('POLYGON ((483113.7771534575 6044785.719547619, 483109.7786044192 6044794.709058521, 483119.51435428584 6044800.639661312, 483122.69415138743 6044795.827421663, 483121.9456342592 6044795.394091143, 483113.7771534575 6044785.719547619))'), 
    loads('POLYGON ((483133.04281097226 6044802.937104642, 483128.0945434971 6044799.601451917, 483121.29791019013 6044809.679453793, 483123.5484954713 6044811.276744148, 483122.9758372711 6044812.476021962, 483124.1764852062 6044813.347730006, 483123.7495066046 6044814.395836985, 483124.6437050717 6044814.677997099, 483123.63903792365 6044816.62808586, 483124.5382667834 6044817.207542924, 483126.03530507185 6044818.074205603, 483127.0424869818 6044816.272764664, 483125.84435347153 6044815.549705131, 483127.56735730194 6044812.24916695, 483130.6090203363 6044808.034034065, 483133.79384452326 6044803.519082784, 483133.04281097226 6044802.937104642))'), 
    loads('POLYGON ((483115.9000297531 6044806.054063313, 483121.29791019013 6044809.679453793, 483128.0945434971 6044799.601451917, 483122.69415138743 6044795.827421663, 483119.51435428584 6044800.639661312, 483115.9000297531 6044806.054063313))'), 
    loads('POLYGON ((483134.06005068467 6044801.730258647, 483133.04281097226 6044802.937104642, 483133.79384452326 6044803.519082784, 483134.5172104292 6044802.465930707, 483134.66288969025 6044802.314759574, 483134.06005068467 6044801.730258647))'), 
    loads('POLYGON ((483134.5172104292 6044802.465930707, 483133.79384452326 6044803.519082784, 483130.6090203363 6044808.034034065, 483134.8037439027 6044810.639061716, 483137.975990341 6044805.380866386, 483138.2623182099 6044804.781227452, 483134.66288969025 6044802.314759574, 483134.5172104292 6044802.465930707))'), 
    loads('POLYGON ((483182.759417432 6044753.766119763, 483185.37909790233 6044750.896392559, 483186.10748553695 6044750.140537053, 483187.7627766503 6044751.599248085, 483191.98238994007 6044746.917990236, 483192.5852290377 6044747.502483568, 483193.89884130744 6044746.29059033, 483182.13846117305 6044734.59567908, 483172.9406527028 6044742.930260377, 483170.7529719815 6044745.049174563, 483178.2431597635 6044749.679706112, 483182.759417432 6044753.766119763))'), 
    loads('POLYGON ((483206.300116702 6044769.572435074, 483206.9029582976 6044770.1569289155, 483215.09612216876 6044763.772374024, 483222.71914976416 6044758.7357405415, 483210.45373780257 6044743.480891307, 483209.8659968094 6044743.788282508, 483203.22972854576 6044737.061577326, 483193.89884130744 6044746.29059033, 483192.5852290377 6044747.502483568, 483204.780155855 6044758.595235708, 483200.2540907172 6044762.686963962, 483206.300116702 6044769.572435074))'), 
    loads('POLYGON ((483191.54865979933 6044773.838324612, 483196.0624197296 6044777.7760947775, 483203.95921058976 6044771.396592771, 483198.82751154335 6044765.982449954, 483191.54865979933 6044773.838324612))'), 
    loads('POLYGON ((483176.64598438743 6044760.412601306, 483185.3745772783 6044768.144544497, 483193.2411725162 6044759.981289391, 483194.5497540578 6044758.472099484, 483185.37909790233 6044750.896392559, 483182.759417432 6044753.766119763, 483176.64598438743 6044760.412601306))'), 
    loads('POLYGON ((483185.3745772783 6044768.144544497, 483191.54865979933 6044773.838324612, 483198.82751154335 6044765.982449954, 483193.2411725162 6044759.981289391, 483185.3745772783 6044768.144544497))'), 
    loads('POLYGON ((483195.6228700337 6044778.0809622295, 483187.19316236203 6044770.492620562, 483180.3437827221 6044777.449031845, 483188.1756820356 6044784.750185724, 483195.6228700337 6044778.0809622295))'), 
    loads('POLYGON ((483167.86505178426 6044767.104507025, 483163.34376273915 6044762.720784527, 483158.69967010594 6044768.598787787, 483163.2108969589 6044772.38792487, 483167.86505178426 6044767.104507025))'), 
    loads('POLYGON ((483182.3611362684 6044791.540294742, 483182.6600409561 6044791.683895216, 483188.1932950779 6044785.790720898, 483178.5579058158 6044777.033373016, 483173.1803926086 6044783.36995539, 483171.72864125064 6044785.178965679, 483180.6079647094 6044793.057059643, 483182.3611362684 6044791.540294742))'), 
    loads('POLYGON ((483171.72864125064 6044785.178965679, 483173.1803926086 6044783.36995539, 483178.5579058158 6044777.033373016, 483179.86649240146 6044775.524182401, 483174.9056429903 6044771.44532812, 483174.3204148049 6044771.901365567, 483171.00228238694 6044768.53798885, 483162.9950120186 6044777.149698539, 483171.72864125064 6044785.178965679))'), 
    loads('POLYGON ((483173.763594165 6044800.310779742, 483180.4622863892 6044793.208231384, 483180.6079647094 6044793.057059643, 483171.72864125064 6044785.178965679, 483162.9950120186 6044777.149698539, 483156.8790322409 6044783.647535949, 483156.58767509245 6044783.949878321, 483161.2571659319 6044788.3310913965, 483173.763594165 6044800.310779742))'), 
    loads('POLYGON ((483173.763594165 6044800.310779742, 483161.2571659319 6044788.3310913965, 483154.55594635766 6044795.284973109, 483157.5701467745 6044798.20746854, 483168.99142076395 6044807.380522943, 483173.763594165 6044800.310779742))'), 
    loads('POLYGON ((483161.2571659319 6044788.3310913965, 483156.58767509245 6044783.949878321, 483156.8790322409 6044783.647535949, 483154.6183856458 6044781.455667802, 483147.6232929819 6044788.5632333355, 483154.55594635766 6044795.284973109, 483161.2571659319 6044788.3310913965))'), 
    loads('POLYGON ((483147.6232929819 6044788.5632333355, 483154.6183856458 6044781.455667802, 483147.6958049492 6044775.328529441, 483147.5501263576 6044775.479700332, 483142.7452454111 6044780.616987641, 483141.29097290436 6044782.277344484, 483147.6232929819 6044788.5632333355))'), 
    loads('POLYGON ((483137.485506864 6044776.394508247, 483141.6850358256 6044770.524080259, 483129.9548745407 6044760.61283664, 483129.05565109703 6044760.0333838295, 483123.9770155607 6044766.513525753, 483127.58145672065 6044769.277283326, 483127.8728143789 6044768.974942418, 483131.3290637692 6044771.741222041, 483131.33660932904 6044772.187165066, 483135.69208640786 6044775.532897517, 483136.131638049 6044775.228033163, 483137.485506864 6044776.394508247))'), 
    loads('POLYGON ((483129.05565109703 6044760.0333838295, 483124.102379088 6044756.400450145, 483121.851807714 6044754.803169814, 483117.6648477999 6044761.416815377, 483123.9770155607 6044766.513525753, 483129.05565109703 6044760.0333838295))'), 
    loads('POLYGON ((483117.6648477999 6044761.416815377, 483121.851807714 6044754.803169814, 483109.69722749625 6044746.088662662, 483105.6509120431 6044752.253831407, 483113.0079672425 6044757.778829546, 483117.6648477999 6044761.416815377))'), 
    loads('POLYGON ((483105.6509120431 6044752.253831407, 483109.69722749625 6044746.088662662, 483105.1935813096 6044742.745450831, 483101.1472642416 6044748.910615174, 483105.6509120431 6044752.253831407))'), 
    loads('POLYGON ((483101.1472642416 6044748.910615174, 483105.1935813096 6044742.745450831, 483100.39103695785 6044739.25863552, 483093.1897420853 6044734.177057238, 483089.4372930474 6044740.188518595, 483101.1472642416 6044748.910615174))'), 
    loads('POLYGON ((483111.61331976124 6044727.915879118, 483104.22143440513 6044737.855229364, 483111.12635160255 6044742.941845765, 483118.0610786313 6044732.266816856, 483111.61331976124 6044727.915879118))'), 
    loads('POLYGON ((483104.2512609221 6044722.093604702, 483102.7466970007 6044720.781007187, 483094.76454891724 6044730.879078004, 483095.0659646853 6044731.171327485, 483102.2697728708 6044736.401549589, 483104.22143440513 6044737.855229364, 483111.61331976124 6044727.915879118, 483104.2512609221 6044722.093604702))'), 
    loads('POLYGON ((483120.858955447 6044722.4056659555, 483109.90253913496 6044714.414242825, 483104.2512609221 6044722.093604702, 483111.61331976124 6044727.915879118, 483118.0610786313 6044732.266816856, 483120.76125365135 6044734.153820109, 483126.4125252145 6044726.474437145, 483122.8106169481 6044723.859339299, 483120.858955447 6044722.4056659555))'), 
    loads('POLYGON ((483114.9786401133 6044707.785500503, 483114.07690816437 6044707.057403011, 483109.13642597594 6044712.940388279, 483121.2934749462 6044721.803510488, 483120.858955447 6044722.4056659555, 483122.8106169481 6044723.859339299, 483125.5659258158 6044720.243882834, 483127.9697124317 6044722.135926853, 483129.5621100949 6044719.878473403, 483127.1583237527 6044717.986430303, 483124.60383032134 6044715.948262964, 483114.9786401133 6044707.785500503))'), 
    loads('POLYGON ((483119.5308176512 6044749.043763969, 483127.4978631392 6044738.053767222, 483122.8510509961 6044735.010384413, 483122.4115009007 6044735.315246721, 483115.0271662263 6044745.700556074, 483119.5308176512 6044749.043763969))'), 
    loads('POLYGON ((483115.0271662263 6044745.700556074, 483122.4115009007 6044735.315246721, 483120.76125365135 6044734.153820109, 483118.0610786313 6044732.266816856, 483111.12635160255 6044742.941845765, 483115.0271662263 6044745.700556074))'), 
    loads('POLYGON ((483126.2825285476 6044753.835602765, 483135.14627673925 6044743.276397907, 483127.4978631392 6044738.053767222, 483119.5308176512 6044749.043763969, 483126.2825285476 6044753.835602765))'), 
    loads('POLYGON ((483128.4663129035 6044690.159253855, 483127.45160039584 6044691.514730356, 483114.9786401133 6044707.785500503, 483124.60383032134 6044715.948262964, 483127.1583237527 6044717.986430303, 483140.9423733881 6044700.355098594, 483139.88993196236 6044699.480880938, 483136.42113195715 6044695.971395187, 483128.4663129035 6044690.159253855))'), 
    loads('POLYGON ((483140.9367080408 6044673.739850809, 483135.1372904504 6044681.42172042, 483143.09965210065 6044687.679788741, 483136.42113195715 6044695.971395187, 483139.88993196236 6044699.480880938, 483140.9423733881 6044700.355098594, 483143.19796505576 6044702.249657222, 483148.70100393303 6044694.5728105595, 483151.56445972977 6044697.3491516225, 483157.6854147785 6044691.148673746, 483140.9367080408 6044673.739850809))'), 
    loads('POLYGON ((483128.4663129035 6044690.159253855, 483136.42113195715 6044695.971395187, 483143.09965210065 6044687.679788741, 483135.1372904504 6044681.42172042, 483128.4663129035 6044690.159253855))'), 
    loads('POLYGON ((483164.85833255097 6044668.277125529, 483153.9822162511 6044656.269847298, 483141.2255467585 6044673.288866691, 483159.17237238906 6044691.42073316, 483165.732864087 6044684.915391376, 483156.3788986487 6044675.261195472, 483161.0481002497 6044670.869714885, 483165.727596374 6044675.845453942, 483164.273345476 6044677.505794992, 483172.5874581364 6044687.029003649, 483177.4048503824 6044682.634984963, 483164.85833255097 6044668.277125529))'), 
    loads('POLYGON ((483241.79052437807 6044746.961700034, 483247.36650219024 6044743.595519556, 483243.4027204122 6044737.120691549, 483237.67603477 6044740.340744607, 483241.79052437807 6044746.961700034))'), 
    loads('POLYGON ((483247.36650219024 6044743.595519556, 483258.81734911574 6044737.006748784, 483254.1151127896 6044730.693202497, 483250.7516560715 6044724.654227946, 483250.0182417357 6044725.1127929315, 483234.47588045785 6044735.191114686, 483237.67603477 6044740.340744607, 483243.4027204122 6044737.120691549, 483247.36650219024 6044743.595519556))'), 
    loads('POLYGON ((483228.73217291344 6044754.916052064, 483234.89086754667 6044750.945189177, 483229.25921056326 6044742.2684126785, 483227.8902340127 6044740.21007352, 483223.3437616396 6044734.339924972, 483218.64658542944 6044728.323655383, 483218.20703898 6044728.628522268, 483212.0684847134 6044733.788539459, 483228.73217291344 6044754.916052064))'), 
    loads('POLYGON ((483229.25921056326 6044742.2684126785, 483234.0866723846 6044738.468923797, 483232.86840555945 6044736.556708736, 483228.9197385122 6044730.973761024, 483228.316898136 6044730.389271281, 483223.3437616396 6044734.339924972, 483227.8902340127 6044740.21007352, 483229.25921056326 6044742.2684126785))'), 
    loads('POLYGON ((483179.6705092581 6044685.124115227, 483174.7074400731 6044689.669306274, 483176.66916691745 6044691.717547512, 483179.4445714463 6044689.291257341, 483182.91590198193 6044692.949369754, 483184.9578902991 6044690.981635051, 483179.6705092581 6044685.124115227))'), 
    loads('POLYGON ((483157.45533959445 6044826.460747283, 483151.1556872388 6044822.107269101, 483147.6920837446 6044827.6678226795, 483154.43632337387 6044832.01373621, 483157.45533959445 6044826.460747283))'), 
    loads('POLYGON ((483101.12617979234 6044826.527545385, 483105.92122764565 6044829.568448636, 483108.5283815585 6044825.955476927, 483103.4344303102 6044822.770972666, 483102.8491950213 6044823.227007975, 483101.12617979234 6044826.527545385))'), 
    loads('POLYGON ((483103.4344303102 6044822.770972666, 483108.5283815585 6044825.955476927, 483110.17361468764 6044826.81962065, 483113.21026127273 6044822.3071898315, 483106.61675895256 6044818.107375301, 483104.73549228586 6044820.815839974, 483103.4344303102 6044822.770972666))'), 
    loads('POLYGON ((483112.57239728357 6044828.414394363, 483119.64783955325 6044817.290793446, 483117.5504781167 6044815.988275172, 483113.21026127273 6044822.3071898315, 483110.17361468764 6044826.81962065, 483112.57239728357 6044828.414394363))'), 
    loads('POLYGON ((483097.01729153056 6044846.522150829, 483104.37658435403 6044834.650251181, 483103.025225701 6044833.632412038, 483105.92122764565 6044829.568448636, 483101.12617979234 6044826.527545385, 483092.0212368849 6044840.362133111, 483091.011530541 6044842.01492605, 483097.01729153056 6044846.522150829))'), 
    loads('POLYGON ((483091.7223320231 6044840.218528756, 483102.8491950213 6044823.227007975, 483097.9034422188 6044820.039979062, 483097.48400406 6044821.534031089, 483096.499447036 6044824.673306711, 483093.2064700234 6044822.796365772, 483094.7888364298 6044819.944299052, 483098.0665559628 6044812.156567911, 483097.0166200621 6044811.430982431, 483096.7177160998 6044811.287378718, 483082.43365671404 6044834.42895115, 483091.7223320231 6044840.218528756))'), 
    loads('POLYGON ((483119.01268513204 6044832.3194346, 483120.60007494414 6044829.764657445, 483125.3597237603 6044821.951680158, 483124.3097844473 6044821.226097149, 483124.5961137602 6044820.626457592, 483123.09656011837 6044819.611145939, 483119.64783955325 6044817.290793446, 483112.57239728357 6044828.414394363, 483119.01268513204 6044832.3194346))'), 
    loads('POLYGON ((483105.42436132254 6044852.772802838, 483115.3882875584 6044837.139260623, 483115.83538780437 6044837.280341479, 483119.01268513204 6044832.3194346, 483112.57239728357 6044828.414394363, 483107.37820758845 6044836.82953296, 483099.8682070101 6044848.555311461, 483105.2736511857 6044852.6266762735, 483105.42436132254 6044852.772802838))'), 
    loads('POLYGON ((483134.9622052097 6044820.003910956, 483130.4761179819 6044817.701223285, 483127.33133107953 6044815.821773763, 483127.0424869818 6044816.272764664, 483126.03530507185 6044818.074205603, 483124.5961137602 6044820.626457592, 483124.3097844473 6044821.226097149, 483125.3597237603 6044821.951680158, 483130.9032975273 6044825.425899843, 483134.9622052097 6044820.003910956))'), 
    loads('POLYGON ((483151.1556872388 6044822.107269101, 483145.15746150253 6044818.046039145, 483139.00601593126 6044813.6900332235, 483138.8603365568 6044813.841204625, 483136.98914188397 6044817.144268615, 483134.29396847275 6044815.554549518, 483135.00727426365 6044813.906802446, 483133.36204111023 6044813.042664639, 483130.4761179819 6044817.701223285, 483134.9622052097 6044820.003910956, 483135.1053694889 6044819.70409104, 483147.6920837446 6044827.6678226795, 483151.1556872388 6044822.107269101))'), 
    loads('POLYGON ((483154.43632337387 6044832.01373621, 483147.6920837446 6044827.6678226795, 483135.1053694889 6044819.70409104, 483134.9622052097 6044820.003910956, 483130.9032975273 6044825.425899843, 483130.18244448875 6044826.627702934, 483128.9893396389 6044826.201940149, 483125.82714079326 6044832.054739282, 483124.81995683233 6044833.856183282, 483128.8589503981 6044836.017797892, 483132.74954740994 6044829.409137224, 483138.29564409883 6044833.032003852, 483138.43880847644 6044832.732183441, 483149.6792104069 6044839.97538696, 483154.43632337387 6044832.01373621))'), 
    loads('POLYGON ((483105.42436132254 6044852.772802838, 483113.21099719225 6044857.3984012455, 483118.67391908885 6044847.343055783, 483118.3750135561 6044847.199452226, 483120.3893867485 6044843.596560537, 483121.9692330464 6044840.595833392, 483121.37142234127 6044840.30862671, 483115.83538780437 6044837.280341479, 483115.3882875584 6044837.139260623, 483105.42436132254 6044852.772802838))'), 
    loads('POLYGON ((483118.90278395766 6044860.870119797, 483126.8271740168 6044847.35295277, 483123.6823773161 6044845.473495658, 483120.3893867485 6044843.596560537, 483118.3750135561 6044847.199452226, 483118.67391908885 6044847.343055783, 483113.21099719225 6044857.3984012455, 483118.90278395766 6044860.870119797))'), 
    loads('POLYGON ((483149.6792104069 6044839.97538696, 483138.43880847644 6044832.732183441, 483138.29564409883 6044833.032003852, 483134.98525385687 6044838.887333818, 483139.4738683854 6044841.338673509, 483146.3537323519 6044844.9388323985, 483149.3903666608 6044840.426379828, 483149.6792104069 6044839.97538696))'), 
    loads('POLYGON ((483146.3537323519 6044844.9388323985, 483139.4738683854 6044841.338673509, 483125.6445196762 6044865.067422509, 483125.94342593284 6044865.211026107, 483134.7873697987 6044862.23531729, 483143.03328136506 6044850.199577315, 483146.3537323519 6044844.9388323985))'), 
    loads('POLYGON ((483134.98525385687 6044838.887333818, 483134.842089262 6044839.187154377, 483129.2209348653 6044848.650427688, 483126.8271740168 6044847.35295277, 483118.90278395766 6044860.870119797, 483125.6445196762 6044865.067422509, 483139.4738683854 6044841.338673509, 483134.98525385687 6044838.887333818))'), 
    loads('POLYGON ((483064.03268064436 6044693.040197529, 483058.9413361998 6044690.004361436, 483057.5021463714 6044692.556565563, 483057.0726517813 6044693.456008641, 483062.3147043292 6044696.637971736, 483064.03268064436 6044693.040197529))'), 
    loads('POLYGON ((483118.47642522544 6044774.339066855, 483116.9768801606 6044773.32375945, 483114.81684244954 6044777.077792192, 483116.16819379595 6044778.095623029, 483118.47642522544 6044774.339066855))'), 
]

fig = plt.figure(1, (12, 10))

#############################################################

sub1 = fig.add_subplot(111)
sub1.set_title('buffer=1.0 edge_length=1.0', pad=10, family='sans-serif')
sub1.axes.get_xaxis().set_visible(False)
sub1.axes.get_yaxis().set_visible(False)

generalized = c4.morphological_amalgamation(buildings, 1.0, 1.0)

for building in buildings:
    poly = Path.make_compound_path(Path(numpy.asarray(building.exterior.coords)[:, :2]),*[Path(numpy.asarray(ring.coords)[:, :2]) for ring in building.interiors])
    sub1.add_patch(PathPatch(poly, facecolor="gray", edgecolor='none'))

for g in generalized:
    poly = Path.make_compound_path(Path(numpy.asarray(g.exterior.coords)[:, :2]),*[Path(numpy.asarray(ring.coords)[:, :2]) for ring in g.interiors])
    sub1.add_patch(PathPatch(poly, facecolor="none", edgecolor='red', linewidth=1.5))

sub1.autoscale_view()
plt.show()
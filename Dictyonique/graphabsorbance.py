import numpy as np
import matplotlib.pyplot as plt

time1 = [0,913.5,1827,2740.5,3654,4567.5,5481,6394.5,7308,8221.5,9135,10048.6,10962.1,11875.6,12789.1,13702.6,14616.1,15529.6,16443.1,17356.6,18270.1,19183.6,20097.1,21010.6,21924.1,22837.6,23751.1,24664.6,25578.1,26491.6,27405.1,28318.6,29232.1,30145.6,31059.1,31972.6,32886.1,33799.6,34713.1,35627.1,36540.6,37454.1,38367.6,39281.1,40194.6]

A5=[0,-0.0002999901772,0.005500018597,0.00830000639,0.01180002093,0.01240000129,0.01480001211,0.01560002565,0.01930001378,0.01850000024,0.01860001683,0.02090001106,0.02300000191,0.02300000191,0.02350002527,0.02220001817,0.02430000901,0.02350002527,0.02380001545,0.0258000195,0.02900001407,0.02900001407,0.02620002627,0.03060001135,0.02880001068,0.02810001373,0.03100001812,0.03020000458,0.03010001779,0.02910000086,0.03080001473,0.03280001879,0.03150001168,0.03220000863,0.03210002184,0.03570002317,0.03480002284,0.03460001945,0.03500002623,0.03830000758,0.0353000164,0.03510001302,0.03610000014,0.03620001674,0.03910002112]
A6=[0,0.0002999901772,0.006099998951,0.009599983692,0.01209998131,0.01499998569,0.02049997449,0.01929998398,0.02499997616,0.02390000224,0.02359998226,0.0284999907,0.03019997478,0.03099998832,0.03069999814,0.03339999914,0.0325999856,0.03409999609,0.03439998627,0.03209999204,0.03549998999,0.03629997373,0.03189998865,0.03419998288,0.0338999927,0.03339999914,0.03419998288,0.03739997745,0.0352999866,0.03659999371,0.03759998083,0.03929999471,0.03639999032,0.03759998083,0.04379999638,0.0339999795,0.03949999809,0.03759998083,0.03819999099,0.05289998651,0.03999999166,0.04259997606,0.04279997945,0.04399999976,0.0434999764]
A7=[0,-0.01609998941,-0.002499997616,0.01679998636,0.05789995193,0.1126999855,0.2217999697,0.3588000536,0.3981000185,0.3684999943,0.3368999958,0.3142999411,0.2687000036,0.2107000351,0.2611000538,0.2968000174,0.2635999918,0.3068000078,0.3603999615,0.3954000473,0.3906999826,0.4638999701,0.3848999739,0.3580000401,0.3458000422,0.3530999422,0.3300999403,0.3451999426,0.3552000523,0.3344999552,0.3222999573,0.3351000547,0.3223999739,0.3298000097,0.3494000435,0.340299964,0.3513000011,0.3149000406,0.3266999722,0.3576999903,0.3430999517,0.364199996,0.358899951,0.3312000036,0.3680000305]
A8=[0,0.0271999836,-0.0515999794,-0.04700005054,-0.09670007229,-0.09210002422,0.03090000153,0.0515999794,0.1252999306,0.1741999388,0.2250999212,0.1679999828,0.2760999203,0.3198999166,0.2972999811,0.344900012,0.2575999498,0.4068000317,0.3780999184,0.4369000196,0.4491000175,0.317299962,0.2789000273,0.3111000061,0.3229999542,0.3438999653,0.3476999998,0.3442000151,0.3292000294,0.3381999731,0.3349000216,0.3079999685,0.3457000256,0.3315999508,0.3431999683,0.2982000113,0.3521000147,0.3392000198,0.3186999559,0.348099947,0.3457000256,0.3331999779,0.298699975,0.3073999882,0.3513000011]
A9=[0,0.01800000668,0.04140001535,0.03479999304,0.06050002575,0.1001999974,0.1261000633,0.1769000292,0.1871000528,0.1984000206,0.2609000206,0.2417000532,0.2930999994,0.2798000574,0.3015999794,0.3391000032,0.3388999701,0.3378000259,0.3064000607,0.371999979,0.3949999809,0.4175000191,0.4091000557,0.424399972,0.4233000278,0.4105000496,0.4031000137,0.3585000038,0.3658000231,0.3724000454,0.3847000599,0.4392000437,0.3698999882,0.4098000526,0.4733999968,0.4315000772,0.3856999874,0.4076000452,0.4541000128,0.4404000044,0.4313000441,0.4251999855,0.4161000252,0.4289000034,0.4358999729]
A10=[0,0.05680000782,0.07230007648,0.07950007915,0.09200000763,0.1062999964,0.1035000086,0.1129000187,0.114199996,0.1162000895,0.1261000633,0.1169000864,0.128000021,0.1184000969,0.1174000502,0.1290000677,0.1266000271,0.1251000166,0.1157000065,0.1317000389,0.1301000118,0.1304000616,0.1270000935,0.1249001026,0.1275000572,0.121800065,0.1249001026,0.1349000931,0.1297000647,0.128500104,0.1291000843,0.1239000559,0.1258000135,0.1233000755,0.1299999952,0.1351000071,0.1311000586,0.1243000031,0.1289000511,0.1308000088,0.1345000267,0.1339000463,0.1282000542,0.1247000694,0.1308000088]
A11=[0,0.06169998646,0.1069999933,0.1606000662,0.2034000158,0.2281000614,0.2366000414,0.2662000656,0.2666000128,0.2760000229,0.2850999832,0.2949000597,0.2956000566,0.2960000038,0.309300065,0.3120000362,0.3108000755,0.3200000525,0.2924000025,0.3162000179,0.3187000751,0.3203999996,0.3170000315,0.3259000778,0.2926000357,0.32310009,0.3411999941,0.3150000572,0.3323000669,0.3344000578,0.3180000782,0.3288999796,0.3163000345,0.3299000263,0.3173000813,0.3422000408,0.3403999805,0.3259999752,0.3429000378,0.3468000889,0.3439999819,0.3565000296,0.334600091,0.3391000032,0.3468999863]
A12=[0,0.02550005913,0.04460000992,0.06580007076,0.07740008831,0.1098999977,0.1269000769,0.1431000233,0.1612000465,0.1629000902,0.1859000921,0.1825000048,0.2355000973,0.2317000628,0.2233000994,0.2813000679,0.2581000328,0.3142000437,0.298500061,0.3538000584,0.3103001118,0.3250000477,0.337100029,0.3450000286,0.3531000614,0.3049000502,0.3032000065,0.3628000021,0.314800024,0.3436000347,0.3407000303,0.3358000517,0.3434000015,0.3488000631,0.3259000778,0.3652000427,0.388600111,0.3554000854,0.3694000244,0.3904000521,0.3762000799,0.3770000935,0.3627001047,0.3481000662,0.3628000021]
B5 =[0,-0.00339999795,-0.004299998283,-0.008599996567,-0.01249998808,-0.01469999552,-0.01659998298,-0.01749998331,-0.0189999938,-0.01979997754,-0.02199998498,-0.02199998498,-0.02229997516,-0.02300000191,-0.02379998565,-0.02480000257,-0.02599999309,-0.02639999986,-0.02639999986,-0.02779999375,-0.02699998021,-0.0284999907,-0.02979999781,-0.03289997578,-0.03459998965,-0.03819999099,-0.03909999132,-0.0420999825,-0.04439997673,-0.04659998417,-0.05069997907,-0.05480000377,-0.05849999189,-0.06239998341,-0.0664999783,-0.06970000267,-0.07229998708,-0.07559999824,-0.07819998264,-0.08049999177,-0.08359998465,-0.0868999958,-0.08879998326,-0.09029999375,-0.09359999001]
B6 =[0,-0.004299998283,0.0004000067711,0.001599997282,0.00229999423,0.002799987793,-0.0004999935627,-0.0006000101566,-0.003900021315,-0.002000004053,-0.001599997282,-0.002700001001,-0.001200020313,-0.00229999423,-0.0002000033855,-0.0008000135422,0.0004999935627,0.002099990845,0.002999991179,0.005400002003,0.008399993181,0.007599979639,0.008799999952,0.009700000286,0.01060000062,0.01029998064,0.01159998775,0.01319998503,0.0135999918,0.01319998503,0.01609998941,0.01679998636,0.01679998636,0.01800000668,0.01859998703,0.0189999938,0.02069997787,0.02159997821,0.02199998498,0.02279999852,0.02210000157,0.02369999886,0.02369999886,0.02529999614,0.02500000596]
B7 =[0,0.09359997511,0.2328000069,0.3615999818,0.4298999906,0.4717000127,0.5123999715,0.527700007,0.5444000363,0.5573000312,0.5667000413,0.5783999562,0.5861999393,0.5856999755,0.5917000175,0.5952000022,0.6011000276,0.6022999883,0.6046000123,0.6134999394,0.6048000455,0.6127000451,0.617299974,0.6161000133,0.6180999875,0.6144999862,0.6230999827,0.6265999675,0.6333000064,0.630400002,0.6340000033,0.6380999684,0.6347000003,0.6376000047,0.6376000047,0.5746000409,0.6215999722,0.6179999709,0.5933000445,0.6320000291,0.5687000155,0.6008999944,0.6069000363,0.6270000339,0.6085999608]
B8 =[0,-0.01120001078,0.001399993896,0.0191000104,0.0433999896,0.05919998884,0.06589996815,0.08269995451,0.04199999571,0.04219996929,0.04389995337,0.06079995632,0.04989999533,0.0489000082,0.08709996939,0.0816000104,0.02489995956,0.02129995823,0.03209996223,0.01730000973,0.006599962711,0.03020000458,0.04269999266,0.009799957275,0.02349996567,-0.0002000331879,-0.03350001574,-0.03200000525,-0.02630001307,-0.0191000104,-0.008199989796,-0.03339999914,-0.04559999704,-0.07960000634,-0.04530000687,-0.03500002623,-0.1563000083,-0.1287000179,-0.1645000279,-0.1455000043,-0.1521000266,-0.1642000079,-0.1561000049,-0.1455000043,-0.1621000171]
B9 =[0,0.09890002012,0.2328000069,0.3764000535,0.4797000289,0.5386000276,0.5541999936,0.581700027,0.5970000625,0.6259999871,0.6369000077,0.6480000615,0.6248000264,0.6409999728,0.6528000236,0.6565000415,0.6481000781,0.6488999724,0.6564000249,0.6788000464,0.6725999713,0.6795000434,0.6783000827,0.6790000796,0.6903000474,0.6843000054,0.6859000325,0.6754999757,0.6832000613,0.6867000461,0.6673000455,0.682099998,0.6761999726,0.6880000234,0.6933000684,0.6817000508,0.668100059,0.6906999946,0.6961000562,0.6915000081,0.6761999726,0.6791999936,0.6887000203,0.6804999709,0.6889000535]
B10 =[0,0.03170001507,0.05930000544,0.09520000219,0.09429997206,0.1171000004,0.1061999798,0.148999989,0.1324999928,0.1402000189,0.1338999867,0.1338999867,0.1295999885,0.1100000143,0.1183000207,0.1603999734,0.1794999838,0.1222999692,0.1261000037,0.1262999773,0.1269000173,0.1288999915,0.1610000134,0.1071000099,0.1175000072,0.16049999,0.1452999711,0.09869998693,0.07429999113,0.09189999104,0.07669997215,0.05369997025,0.04030001163,0.118900001,0.1158999801,0.0638999939,0.06989997625,-0.002799987793,0.01150000095,-0.02069997787,-0.06029999256,-0.02679997683,-0.06229999661,-0.06740000844,-0.07379999757]
B11 =[0,0.1488000154,0.3018999696,0.385899961,0.4388999343,0.46450001,0.4811000228,0.5035999417,0.4998000264,0.5092999339,0.5282999873,0.5135000348,0.5185999274,0.5429000258,0.5436000228,0.5349000096,0.543299973,0.5440999866,0.5389999747,0.5597999692,0.5498999953,0.5569999814,0.5523999333,0.5646999478,0.5610999465,0.5723000169,0.5690999627,0.5788000226,0.5857999921,0.5688000321,0.5819999576,0.5767999291,0.5746999383,0.5914999843,0.5938000083,0.5907999873,0.5838000178,0.5971999764,0.6046000123,0.600300014,0.6148999333,0.6274999976,0.6040000319,0.5881000161,0.5924000144]
B12 =[0,0.07400000095,0.481400013,0.119599998,0.1941000223,0.2319999933,0.2814000249,0.2588999867,0.3677999973,0.3828999996,0.3495000601,0.3920999765,0.4041000605,0.4299999475,0.4463000298,0.4514000416,0.4565000534,0.412899971,0.4010000229,0.4084999561,0.4411000013,0.4089000225,0.3841999769,0.3995000124,0.4133000374,0.3986999989,0.3747999668,0.3849999905,0.3809000254,0.4223999977,0.3851000071,0.3485000134,0.3817000389,0.3831000328,0.4154000282,0.4096000195,0.4065999985,0.415899992,0.4329999685,0.3868999481,0.5219000578,0.3909000158,0.3980000019,0.3962000608,0.4253000021]

C5=[0,0.001000016928,0.006600022316,0.0109000206,0.01550000906,0.01739999652,0.01970002055,0.02070000768,0.0218000114,0.02070000768,0.02070000768,0.02200001478,0.02240002155,0.02150002122,0.02080002427,0.01990002394,0.01970002055,0.01890000701,0.01980000734,0.01940000057,0.02200001478,0.02050000429,0.01940000057,0.01860001683,0.0177000165,0.01720002294,0.01810002327,0.01800000668,0.01590001583,0.01450002193,0.01540002227,0.01530000567,0.01210001111,0.01210001111,0.01180002093,0.009400010109,0.01050001383,0.00980001688,0.01320001483,0.01410001516,0.01289999485,0.01340001822,0.01260000467,0.01340001822,0.01330000162]
C6= [0,-0.006700009108,-0.00640001893,-0.007400006056,-0.007600009441,-0.006200015545,-0.007600009441,-0.003700017929,-0.00260001421,-0.002100020647,-0.001300007105,-0.001200020313,0.0007999837399,0.0009000003338,0.003199994564,0.001699984074,0.002700001001,0.005499988794,0.005600005388,0.005600005388,0.008100003004,0.006699979305,0.007799983025,0.008100003004,0.008699983358,0.008799999952,0.009199976921,0.01029998064,0.01069998741,0.01339998841,0.01240000129,0.01209998131,0.01279997826,0.01350000501,0.01330000162,0.01260000467,0.01399999857,0.01539999247,0.01389998198,0.01469999552,0.01459997892,0.01330000162,0.0135999918,0.01510000229,0.01559999585]
C7=[0,0.02520000935,0,0.05010002851,0.04919999838,0.06100004911,0,-0.6183999777,0.1050000191,0.1216000319,0.1306000352,0.1587000489,0.1593000293,0.1829000115,0.2142000198,0.2274000049,0.2323000431,0.2441000342,0.252300024,0.2753000259,0.284700036,0.3167000413,0.3133000135,0.3198000193,0.3485000134,0.3313000202,0.3409000039,0.3544000387,0.3898999691,0.3704000115,0.3548000455,0.3684999943,0.380300045,0.4027000666,0.3772000074,0.3730000257,0.4206000566,0.3847000599,0.4093999863,0.3894000053,0.4293999672,0.4024000168,0.4111000299,0.4476000071,0.3832000494]
C8=[0,0.0408000052,0.1002999842,0.1286000311,0.1465000212,0.171600014,0.1929000318,0.209400028,0.2249000371,0.2234999835,0.2191000283,0.2158000171,0.2163999975,0.2162000239,0.2057000101,0.1947000325,0.1875999868,0.1831000149,0.1681999862,0.1588000357,0.1540000141,0.1703999937,0.1656000316,0.1511000097,0.1529000103,0.1537000239,0.146999985,0.1394000351,0.1430999935,0.1483000219,0.1322999895,0.1398000419,0.1459000409,0.1459000409,0.1538000405,0.157099992,0.146299988,0.1383999884,0.1494999826,0.1441999972,0.1491999924,0.157799989,0.1566000283,0.1574000418,0.1544000208]
C9= [0,0.03110003471,0.03640002012,0.05349999666,0.04500001669,0.0625,0.05550003052,0.06950002909,0.07850003242,0.08750003576,0.06920003891,0.07320004702,0.08720004559,0.06830000877,0.07410001755,0.0829000473,0.08360004425,0.07289999723,0.07120001316,0.05630004406,0.08410000801,0.09830003977,0.06430000067,0.07770001888,0.09659999609,0.07390004396,0.08219999075,0.08670002222,0.08710002899,0.08579999208,0.06840002537,0.1007000208,0.07170003653,0.07440000772,0.09090000391,0.07780003548,0.0734000206,0.09340000153,0.07910001278,0.09119999409,0.07920002937,0.057099998,0.06540000439,0.1039000154,0.08550000191]
C10=[0,0.03979998827,0.09360000491,0.1263000071,0.1489000022,0.1759000123,0.1992000043,0.2158000171,0.2265000045,0.2320999801,0.2183000147,0.2298999727,0.230399996,0.2296999991,0.2236000001,0.2215999663,0.2208000124,0.2276000082,0.2019999921,0.18780002,0.1695000231,0.1617999971,0.1552999914,0.1346000135,0.1070999801,0.09760001302,0.0909999907,0.09269997478,0.09809997678,0.08299997449,0.08849999309,0.08839997649,0.09260001779,0.08519998193,0.08709999919,0.09760001302,0.08589997888,0.09699997306,0.09220001101,0.09080001712,0.08349999785,0.09029999375,0.09290000796,0.09709998965,0.09629997611]
C11= [0,0.01660001278,0.02209997177,0.03829997778,0.04019999504,0.04320001602,0.05809998512,0.05549997091,0.0748000145,0.09280002117,0.07260000706,0.08109998703,0.1021000147,0.08859997988,0.1022999883,0.1053000093,0.09289997816,0.1028000116,0.1297000051,0.1043000221,0.1184999943,0.1089000106,0.1322000027,0.1098999977,0.1255999804,0.1147999763,0.1140000224,0.09869998693,0.09359997511,0.09689998627,0.1198999882,0.1139000058,0.1274999976,0.1231999993,0.09009999037,0.106400013,0.106400013,0.09189999104,0.1125000119,0.113499999,0.117200017,0.100300014,0.09280002117,0.09810000658,0.1000000238]
C12=[0,0.05439996719,0.0992000103,0.1592000127,0.1865000129,0.2150999904,0.2297999859,0.2411000133,0.2324000001,0.2426999807,0.2387999892,0.2405999899,0.2318999767,0.2350999713,0.2462000251,0.217599988,0.2074999809,0.1962000132,0.1870999932,0.1825000048,0.1653000116,0.1661000252,0.1449999809,0.1420000196,0.1322000027,0.1299999952,0.1312000155,0.1342999935,0.1171000004,0.1295999885,0.113499999,0.1201999784,0.1297000051,0.1197000146,0.1177999973,0.117299974,0.1255000234,0.1230000257,0.1244999766,0.1227999926,0.1216999888,0.119599998,0.1209999919,0.1287999749,0.121900022]

splote = []
def modif(a):
    a2=[]
    for i in a:
        if i<0:
            a2.append(0)
        else:
            a2.append(i)
    return a2

A5=modif(A5)
A6=modif(A6)
A7=modif(A7)
A8=modif(A8)
A9=modif(A9)
A10=modif(A10)
A11=modif(A11)
A12=modif(A12)
B5=modif(B5)
B6=modif(B6)
B7=modif(B7)
B8=modif(B8)
B9=modif(B9)
B10=modif(B10)
B11=modif(B11)
B12=modif(B12)
C5=modif(C5)
C6=modif(C6)
C7=modif(C7)
C8=modif(C8)
C9=modif(C9)
C10=modif(C10)
C11=modif(C11)
C12=modif(C12)


#AC=[((abs(A5[i])+abs(A6[i]))/2) for i in range(len(A5))]
#BC=[((abs(B5[i])+abs(B6[i]))/2) for i in range(len(B5))]
#CC=[((abs(C5[i])+abs(C6[i]))/2) for i in range(len(C5))]

#A=[((abs(A7[i])+abs(A8[i])+abs(A9[i])+abs(A10[i])+abs(A11[i])+abs(A12[i]))/6) for i in range(len(A7))]
#B=[((abs(B7[i])+abs(B8[i])+abs(B9[i])+abs(B10[i])+abs(B11[i])+abs(B12[i]))/6) for i in range(len(B7))]
#C=[((abs(C7[i])+abs(C8[i])+abs(C9[i])+abs(C10[i])+abs(C11[i])+abs(C12[i]))/6) for i in range(len(C7))]

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)

#for i in A5,A6,A7,A8,A9,A10,A11,A12,B5,B6,B7,B8,B9,B10,B11,B12,C5,C6,C7,C8,C9,C10,C11,C12:
#    if int(i) < 0:
#        i==0

plt.figure(figsize=(16,10), linewidth=(1000))
plt.semilogy(time1, A5, 'r', label='control 1 pH=5.2')#, time1, A2, 'r', time2, A3, 'r', time2, A4, 'r')
plt.semilogy(time1, A6, 'r', label='control 2 pH=5.2')#, time1, B2, 'g', time2, B3, 'g', time2, B4, 'g')
plt.semilogy(time1, B5, 'b', label='control 1 pH=4.3')#, time1, C2, 'b', time2, C3, 'b', time2, C4, 'b')
plt.semilogy(time1, B6, 'b', label='control 2 pH=4.3')#, time1, D2, 'c', time2, D3, 'c', time2, D4, 'c')
plt.semilogy(time1, C5, 'y', label='control 1 pH=3.1')#, time1, E2, 'm', time2, E3, 'm', time2, E4, 'm')
plt.semilogy(time1, C6, 'y', label='control 2 pH=3.1')#, time1, E2, 'm', time2, E3, 'm', time2, E4, 'm')

plt.semilogy(time1, A7, 'm', label='with cells 1 pH=5.2')#, time1, A2, 'r', time2, A3, 'r', time2, A4, 'r')
plt.semilogy(time1, A8, 'm', label='with cells 2 pH=5.2')#, time1, B2, 'g', time2, B3, 'g', time2, B4, 'g')
plt.semilogy(time1, A9, 'm', label='with cells 3 pH=5.2')#, time1, C2, 'b', time2, C3, 'b', time2, C4, 'b')
plt.semilogy(time1, A10, 'm', label='with cells 4 pH=5.2')#, time1, D2, 'c', time2, D3, 'c', time2, D4, 'c')
plt.semilogy(time1, A11, 'm', label='with cells 5 pH=5.2')#, time1, E2, 'm', time2, E3, 'm', time2, E4, 'm')
plt.semilogy(time1, A12, 'm', label='with cells 6 pH=5.2')#, time1, E2, 'm', time2, E3, 'm', time2, E4, 'm')

plt.semilogy(time1, B7, 'c', label='with cells 1 pH=4.3')#, time1, A2, 'r', time2, A3, 'r', time2, A4, 'r')
plt.semilogy(time1, B8, 'c', label='with cells 2 pH=4.3')#, time1, B2, 'g', time2, B3, 'g', time2, B4, 'g')
plt.semilogy(time1, B9, 'c', label='with cells 3 pH=4.3')#, time1, C2, 'b', time2, C3, 'b', time2, C4, 'b')
plt.semilogy(time1, B10, 'c', label='with cells 4 pH=4.3')#, time1, D2, 'c', time2, D3, 'c', time2, D4, 'c')
plt.semilogy(time1, B11, 'c', label='with cells 5 pH=4.3')#, time1, E2, 'm', time2, E3, 'm', time2, E4, 'm')
plt.semilogy(time1, B12, 'c', label='with cells 6 pH=4.3')#, time1, E2, 'm', time2, E3, 'm', time2, E4, 'm')

plt.semilogy(time1, C7, 'k', label='with cells 1 pH=3.1')#, time1, A2, 'r', time2, A3, 'r', time2, A4, 'r')
plt.semilogy(time1, C8, 'k', label='with cells 2 pH=3.1')#, time1, B2, 'g', time2, B3, 'g', time2, B4, 'g')
plt.semilogy(time1, C9, 'k', label='with cells 3 pH=3.1')#, time1, C2, 'b', time2, C3, 'b', time2, C4, 'b')
plt.semilogy(time1, C10, 'k', label='with cells 4 pH=3.1')#, time1, D2, 'c', time2, D3, 'c', time2, D4, 'c')
plt.semilogy(time1, C11, 'k', label='with cells 5 pH=3.1')#, time1, E2, 'm', time2, E3, 'm', time2, E4, 'm')
plt.semilogy(time1, C12, 'k', label='with cells 6 pH=3.1')#, time1, E2, 'm', time2, E3, 'm', time2, E4, 'm')

plt.xlabel('Time in secondes', size=25)
plt.ylabel('log of Absorbance', size=25)
plt.title('log of Absorbance in function of time (s), of Lactobacillus acidophilus for 3 different pH', size=19)
#plt.legend(bbox_to_anchor=(0, 0.607), loc=3, borderaxepad=0.)
plt.legend(loc=4, prop={'size':15})
plt.show()

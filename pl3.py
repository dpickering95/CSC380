#*****************************************************#
# Play List 3 (pl3)                                   #
# Seed Song is spotify:track:4vcoNCrTtunmJ9q8srpVly   #
# "Season 2 Episode 3" by Glass Animals               #
#*****************************************************#

import numpy as np

class pl3:

	def __init__(self):

		self.songNum = 0 ## start counting from 0

		self.song_pool = [['2tZcHwdct0J7hYyEzgc38y', 0], ['71cUqXJ3h1r0Ees6YdENLU', 0], ['4gB5Idv1iw8jgxyEvuwPVA', 0], ['4ooHsDX0LIPHoWrzs0paYX', 0], ['3cBV8V9zlYNraydyF8NpBY', 0], ['4ZLkFtuDGGbPP4XEsx593Y', 0], ['2f5l2vw6KZXb6cbE0nl0pb', 0], ['4nPg1JG5d7WrgGGOmJHrbP', 0], ['4j4OfqOvPCnOoePywhtrc6', 0], ['0L7pQU3DSR8916FVOyjDFB', 0], ['2WMRd3xAb9FwXopCRNWDq1', 0], ['3vlVbJmvSm3x5Hqmnzh8HI', 0], ['0SGccA9exVTuzQY7jwbASF', 0], ['2YKcA5ZkWQfVHd7bMIv4iw', 0], ['7eXESEtK5e9gDz7jLyOVDb', 0], ['3Ve96alMjeaChfLbszJoKZ', 0], ['5gY2yQvNyyfCcukuXtNmDq', 0], ['6ttNSzoCalhgsJhXHiE7tX', 0], ['7kpEXIcmGbHYEpJ4i6MH9v', 0], ['7ddXYLA5CBEgQA7KbqWJIb', 0], ['4j4pPKE3xAblPIbhxScC1j', 0], ['0xxm1WskKZSCvbkGjkSMr2', 0], ['6wtcxwSJs82tpdeIoj93LF', 0], ['3K4gWURajKtVQZk4NuQFWj', 0], ['75fKUcetc638W5uJVF3X7M', 0], ['4Xmi5NF1gh6ACPO5fX9HbQ', 0], ['4O2aCfXPP9FfPoIPixwVBz', 0], ['7rdSgFebCeIdwpfqbUUOjy', 0], ['6d4cLYfy0LmkxQZZaU2luP', 0], ['229SqGbacrLSBfb9XfJczF', 0]]

		self.prob_matrix = [[0.0, 21.84657999999999, 2.0797878999999986, 7.06979999999999, 22.004652000000018, 14.35387000000001, 33.785596999999996, 7.761439999999998, 2.7120300000000017, 62.77172899999999, 22.19549899999999, 17.84230000000001, 43.68707, 5.930880000000001, 18.224759999999996, 11.26847, 27.689587000000014, 32.870870999999994, 24.2692, 21.488899999999997, 27.1157, 14.746510000000004, 23.4066, 26.01461, 40.425958099999995, 1.56792, 29.536099999999998, 7.111634999999994, 4.3096399999999955, 1.26535220000001], [21.84657999999999, 0.0, 22.84320789999999, 16.312779999999997, 43.472072000000004, 33.46471, 12.625017000000005, 15.411139999999993, 21.83254999999999, 81.80634899999998, 42.35091899999998, 36.51688, 24.65351000000001, 22.220299999999988, 36.89913999999998, 29.90904999999999, 49.33080700000001, 51.35429099999998, 15.073979999999986, 4.6262799999999915, 6.3314800000000115, 36.06108999999999, 4.785180000000011, 7.393190000000011, 21.586538100000006, 22.77465999999999, 8.630680000000005, 20.461614999999995, 25.557139999999997, 22.5219322], [2.0797878999999986, 22.84320789999999, 0.0, 7.495987899999992, 22.437135900000015, 16.223917900000007, 35.466190899999994, 8.210347899999999, 4.359757900000001, 64.0973449, 22.476688899999992, 18.890087900000005, 44.308717900000005, 6.287427900000002, 19.272347899999993, 12.282257899999998, 27.314200900000014, 33.828916899999996, 26.139187900000003, 21.1354879, 28.0026879, 14.034297900000002, 22.450387900000003, 25.1823979, 39.749745999999995, 1.0538678999999984, 31.2418879, 6.028822899999996, 3.334347900000003, 1.5611401000000091], [7.06979999999999, 16.312779999999997, 7.495987899999992, 0.0, 28.400852000000008, 21.251269999999998, 28.679797000000004, 1.9916400000000072, 9.392429999999992, 68.86092899999998, 27.767698999999983, 23.7261, 37.699270000000006, 9.467079999999989, 23.966359999999984, 16.94626999999999, 33.927387, 38.78107099999999, 19.29920000000001, 15.170700000000007, 20.74470000000001, 20.326309999999992, 16.912400000000012, 19.64441000000001, 34.211758100000004, 6.90911999999999, 24.401900000000005, 4.458834999999996, 9.597839999999996, 7.053152200000001], [22.004652000000018, 43.472072000000004, 22.437135900000015, 28.400852000000008, 0.0, 12.158782000000006, 53.66705500000001, 28.287212000000014, 23.848622000000017, 42.762276999999976, 2.397553000000023, 15.678952000000008, 63.14958200000002, 27.262292000000016, 10.067212000000023, 17.021122000000016, 6.559064999999997, 12.49378099999998, 43.75005200000002, 40.408352000000015, 48.90755200000002, 13.629162000000012, 42.227252000000014, 44.89126200000002, 61.458610100000016, 22.304732000000016, 49.52675200000001, 27.929687000000012, 23.067212000000012, 22.252004200000005], [14.35387000000001, 33.46471, 16.223917900000007, 21.251269999999998, 12.158782000000006, 0.0, 43.549727000000004, 21.931570000000008, 12.376160000000008, 50.78585899999999, 11.543628999999983, 3.6301700000000015, 57.75420000000001, 15.59301000000001, 5.078429999999983, 8.06354000000001, 17.834117000000006, 20.463000999999984, 34.122270000000015, 35.737970000000004, 39.17877000000001, 9.030380000000005, 37.63247000000001, 40.24048000000001, 54.75382810000001, 15.71585000000001, 39.36797000000001, 21.334905000000006, 18.472570000000005, 15.547222199999998], [33.785596999999996, 12.625017000000005, 35.466190899999994, 28.679797000000004, 53.66705500000001, 43.549727000000004, 0.0, 27.548156999999996, 31.965566999999997, 92.17133199999999, 52.97449799999999, 46.931897000000006, 14.930527000000003, 32.893237, 48.550156999999984, 39.48606699999999, 59.29601000000001, 61.89472599999999, 23.060996999999993, 14.996296999999997, 9.616496999999995, 46.428107, 15.058196999999993, 17.690206999999994, 13.5635551, 35.141676999999994, 10.585697, 32.828632, 35.924157, 34.888949200000006], [7.761439999999998, 15.411139999999993, 8.210347899999999, 1.9916400000000072, 28.287212000000014, 21.931570000000008, 27.548156999999996, 0.0, 9.85741, 70.39948899999999, 29.26405899999999, 25.215740000000007, 36.92237, 10.981439999999996, 25.597999999999992, 18.607909999999997, 34.33394700000001, 40.129431, 17.928840000000005, 14.49114, 20.620340000000002, 21.53395, 16.242040000000003, 18.974050000000002, 33.541398099999995, 8.079679999999996, 23.40354, 5.766475000000003, 10.862000000000002, 8.260792200000008], [2.7120300000000017, 21.83254999999999, 4.359757900000001, 9.392429999999992, 23.848622000000017, 12.376160000000008, 31.965566999999997, 9.85741, 0.0, 63.098499, 23.623468999999993, 15.702330000000007, 45.895360000000004, 3.776850000000001, 17.174589999999995, 10.1267, 29.978957000000015, 32.666841, 22.03143, 24.11113, 27.330930000000002, 17.17854, 25.838630000000002, 28.57064, 43.1379881, 3.8626900000000024, 27.800129999999996, 9.487064999999998, 6.624589999999998, 3.9313821999999905], [62.77172899999999, 81.80634899999998, 64.0973449, 68.86092899999998, 42.762276999999976, 50.78585899999999, 92.17133199999999, 70.39948899999999, 63.098499, 0.0, 41.755430000000004, 53.67202899999999, 103.60785899999999, 65.162049, 47.619569, 54.592859, 38.49814199999998, 30.626058, 82.831929, 81.273629, 86.918629, 54.323218999999995, 83.021929, 85.534319, 101.97040109999999, 63.061809, 87.925829, 68.61869399999999, 63.84008899999999, 62.76379519999998], [22.19549899999999, 42.35091899999998, 22.476688899999992, 27.767698999999983, 2.397553000000023, 11.543628999999983, 52.97449799999999, 29.26405899999999, 23.623468999999993, 41.755430000000004, 0.0, 14.127798999999985, 62.48442899999999, 25.110738999999995, 8.097659, 15.019568999999994, 8.27028800000002, 11.772628000000005, 43.64689899999999, 40.64919899999999, 47.222398999999996, 13.62560899999999, 42.20169899999999, 44.887708999999994, 61.45505709999999, 22.139578999999994, 48.74959899999999, 27.662133999999988, 22.82985899999999, 22.24845119999998], [17.84230000000001, 36.51688, 18.890087900000005, 23.7261, 15.678952000000008, 3.6301700000000015, 46.931897000000006, 25.215740000000007, 15.702330000000007, 53.67202899999999, 14.127798999999985, 0.0, 60.44937000000001, 15.055180000000009, 6.916459999999986, 9.83617000000001, 21.17348700000001, 23.241170999999987, 31.66490000000001, 38.202600000000004, 40.94460000000001, 10.992210000000004, 39.52230000000001, 42.25431000000001, 56.82165810000001, 18.246220000000008, 37.2218, 23.100735000000004, 20.977940000000004, 18.264252199999998], [43.68707, 24.65351000000001, 44.308717900000005, 37.699270000000006, 63.14958200000002, 57.75420000000001, 14.930527000000003, 36.92237, 45.895360000000004, 103.60785899999999, 62.48442899999999, 60.44937000000001, 0.0, 46.20181, 60.83163, 51.84154, 68.90431700000002, 73.337801, 37.50247, 24.29277, 20.71597, 55.57958, 24.13767, 26.89368, 9.439028100000005, 44.17205, 24.887170000000005, 41.848105000000004, 44.94877, 44.30642220000001], [5.930880000000001, 22.220299999999988, 6.287427900000002, 9.467079999999989, 27.262292000000016, 15.59301000000001, 32.893237, 10.981439999999996, 3.776850000000001, 65.162049, 25.110738999999995, 15.055180000000009, 46.20181, 0.0, 19.162719999999993, 12.06901, 33.135027000000015, 34.880511, 20.61228, 24.36658, 27.53978, 19.252370000000006, 25.91908, 28.55547, 43.11431809999999, 5.85096, 25.714979999999997, 9.321394999999994, 8.561240000000005, 5.9717122000000105], [18.224759999999996, 36.89913999999998, 19.272347899999993, 23.966359999999984, 10.067212000000023, 5.078429999999983, 48.550156999999984, 25.597999999999992, 17.174589999999995, 47.619569, 8.097659, 6.916459999999986, 60.83163, 19.162719999999993, 0.0, 9.096089999999993, 15.561947000000021, 17.519431000000004, 38.58116, 38.43285999999999, 40.46306, 10.48594999999999, 39.374359999999996, 41.74204999999999, 55.92139809999999, 18.240479999999994, 42.69625999999999, 22.454474999999988, 20.96619999999999, 18.205992199999983], [11.26847, 29.90904999999999, 12.282257899999998, 16.94626999999999, 17.021122000000016, 8.06354000000001, 39.48606699999999, 18.607909999999997, 10.1267, 54.592859, 15.019568999999994, 9.83617000000001, 51.84154, 12.06901, 9.096089999999993, 0.0, 22.549657000000014, 24.473340999999994, 29.525270000000003, 29.442769999999996, 33.58077, 7.480040000000003, 30.41807, 32.78814, 49.07348809999999, 11.28139, 33.771969999999996, 15.468564999999995, 11.977909999999996, 11.25208219999999], [27.689587000000014, 49.33080700000001, 27.314200900000014, 33.927387, 6.559064999999997, 17.834117000000006, 59.29601000000001, 34.33394700000001, 29.978957000000015, 38.49814199999998, 8.27028800000002, 21.17348700000001, 68.90431700000002, 33.135027000000015, 15.561947000000021, 22.549657000000014, 0.0, 8.424515999999985, 49.956387000000014, 45.45208700000001, 54.39248700000002, 16.98209700000001, 46.16418700000001, 48.244197000000014, 64.8115451, 27.286267000000016, 55.07968700000001, 31.21482200000001, 26.35214700000001, 27.608939200000005], [32.870870999999994, 51.35429099999998, 33.828916899999996, 38.78107099999999, 12.49378099999998, 20.463000999999984, 61.89472599999999, 40.129431, 32.666841, 30.626058, 11.772628000000005, 23.241170999999987, 73.337801, 34.880511, 17.519431000000004, 24.473340999999994, 8.424515999999985, 0.0, 52.566271, 51.36657099999999, 56.843771, 24.587380999999993, 53.187470999999995, 55.849481, 72.41682909999999, 33.264950999999996, 57.66897099999999, 38.88990599999999, 34.02743099999999, 33.21022319999999], [24.2692, 15.073979999999986, 26.139187900000003, 19.29920000000001, 43.75005200000002, 34.122270000000015, 23.060996999999993, 17.928840000000005, 22.03143, 82.831929, 43.64689899999999, 31.66490000000001, 37.50247, 20.61228, 38.58116, 29.525270000000003, 49.956387000000014, 52.566271, 0.0, 15.099699999999995, 20.3315, 36.45911000000001, 16.7852, 19.393210000000003, 35.76255809999999, 25.79812, 13.636699999999994, 22.859635000000008, 26.574840000000005, 25.465152200000013], [21.488899999999997, 4.6262799999999915, 21.1354879, 15.170700000000007, 40.408352000000015, 35.737970000000004, 14.996296999999997, 14.49114, 24.11113, 81.273629, 40.64919899999999, 38.202600000000004, 24.29277, 24.36658, 38.43285999999999, 29.442769999999996, 45.45208700000001, 51.36657099999999, 15.099699999999995, 0.0, 9.363200000000003, 31.434810000000002, 1.9709000000000025, 4.578910000000002, 21.050258099999997, 20.547819999999998, 10.412399999999998, 17.835335000000004, 21.280540000000002, 20.636852200000007], [27.1157, 6.3314800000000115, 28.0026879, 20.74470000000001, 48.90755200000002, 39.17877000000001, 9.616496999999995, 20.620340000000002, 27.330930000000002, 86.918629, 47.222398999999996, 40.94460000000001, 20.71597, 27.53978, 40.46306, 33.58077, 54.39248700000002, 56.843771, 20.3315, 9.363200000000003, 0.0, 39.75961, 8.5857, 11.06771, 16.141058099999995, 27.506819999999998, 6.697200000000004, 23.775935000000004, 30.181340000000006, 27.58365220000001], [14.746510000000004, 36.06108999999999, 14.034297900000002, 20.326309999999992, 13.629162000000012, 9.030380000000005, 46.428107, 21.53395, 17.17854, 54.323218999999995, 13.62560899999999, 10.992210000000004, 55.57958, 19.252370000000006, 10.48594999999999, 7.480040000000003, 16.98209700000001, 24.587380999999993, 36.45911000000001, 31.434810000000002, 39.75961, 0.0, 31.444710000000004, 31.263100000000005, 49.157448099999996, 13.460430000000004, 40.954409999999996, 15.994524999999998, 10.770549999999998, 13.550042199999993], [23.4066, 4.785180000000011, 22.450387900000003, 16.912400000000012, 42.227252000000014, 37.63247000000001, 15.058196999999993, 16.242040000000003, 25.838630000000002, 83.021929, 42.20169899999999, 39.52230000000001, 24.13767, 25.91908, 39.374359999999996, 30.41807, 46.16418700000001, 53.187470999999995, 16.7852, 1.9709000000000025, 8.5857, 31.444710000000004, 0.0, 2.7576100000000006, 19.300158099999997, 22.06212, 9.852499999999996, 17.779235000000007, 21.785640000000004, 22.352752200000012], [26.01461, 7.393190000000011, 25.1823979, 19.64441000000001, 44.89126200000002, 40.24048000000001, 17.690206999999994, 18.974050000000002, 28.57064, 85.534319, 44.887708999999994, 42.25431000000001, 26.89368, 28.55547, 41.74204999999999, 32.78814, 48.244197000000014, 55.849481, 19.393210000000003, 4.578910000000002, 11.06771, 31.263100000000005, 2.7576100000000006, 0.0, 20.413348099999997, 24.75653, 12.210509999999996, 19.347625000000004, 22.085450000000005, 24.86514220000001], [40.425958099999995, 21.586538100000006, 39.749745999999995, 34.211758100000004, 61.458610100000016, 54.75382810000001, 13.5635551, 33.541398099999995, 43.1379881, 101.97040109999999, 61.45505709999999, 56.82165810000001, 9.439028100000005, 43.11431809999999, 55.92139809999999, 49.07348809999999, 64.8115451, 72.41682909999999, 35.76255809999999, 21.050258099999997, 16.141058099999995, 49.157448099999996, 19.300158099999997, 20.413348099999997, 0.0, 39.323878099999995, 22.1818581, 33.7929231, 39.9139981, 39.20660590000001], [1.56792, 22.77465999999999, 1.0538678999999984, 6.90911999999999, 22.304732000000016, 15.71585000000001, 35.141676999999994, 8.079679999999996, 3.8626900000000024, 63.061809, 22.139578999999994, 18.246220000000008, 44.17205, 5.85096, 18.240479999999994, 11.28139, 27.286267000000016, 33.264950999999996, 25.79812, 20.547819999999998, 27.506819999999998, 13.460430000000004, 22.06212, 24.75653, 39.323878099999995, 0.0, 30.878019999999996, 5.624954999999995, 2.7982800000000054, 0.5072722000000109], [29.536099999999998, 8.630680000000005, 31.2418879, 24.401900000000005, 49.52675200000001, 39.36797000000001, 10.585697, 23.40354, 27.800129999999996, 87.925829, 48.74959899999999, 37.2218, 24.887170000000005, 25.714979999999997, 42.69625999999999, 33.771969999999996, 55.07968700000001, 57.66897099999999, 13.636699999999994, 10.412399999999998, 6.697200000000004, 40.954409999999996, 9.852499999999996, 12.210509999999996, 22.1818581, 30.878019999999996, 0.0, 27.241135, 31.63814, 30.584452200000005], [7.111634999999994, 20.461614999999995, 6.028822899999996, 4.458834999999996, 27.929687000000012, 21.334905000000006, 32.828632, 5.766475000000003, 9.487064999999998, 68.61869399999999, 27.662133999999988, 23.100735000000004, 41.848105000000004, 9.321394999999994, 22.454474999999988, 15.468564999999995, 31.21482200000001, 38.88990599999999, 22.859635000000008, 17.835335000000004, 23.775935000000004, 15.994524999999998, 17.779235000000007, 19.347625000000004, 33.7929231, 5.624954999999995, 27.241135, 0.0, 6.4910749999999995, 5.955517200000005], [4.3096399999999955, 25.557139999999997, 3.334347900000003, 9.597839999999996, 23.067212000000012, 18.472570000000005, 35.924157, 10.862000000000002, 6.624589999999998, 63.84008899999999, 22.82985899999999, 20.977940000000004, 44.94877, 8.561240000000005, 20.96619999999999, 11.977909999999996, 26.35214700000001, 34.02743099999999, 26.574840000000005, 21.280540000000002, 30.181340000000006, 10.770549999999998, 21.785640000000004, 22.085450000000005, 39.9139981, 2.7982800000000054, 31.63814, 6.4910749999999995, 0.0, 3.2613922000000066], [1.26535220000001, 22.5219322, 1.5611401000000091, 7.053152200000001, 22.252004200000005, 15.547222199999998, 34.888949200000006, 8.260792200000008, 3.9313821999999905, 62.76379519999998, 22.24845119999998, 18.264252199999998, 44.30642220000001, 5.9717122000000105, 18.205992199999983, 11.25208219999999, 27.608939200000005, 33.21022319999999, 25.465152200000013, 20.636852200000007, 27.58365220000001, 13.550042199999993, 22.352752200000012, 24.86514220000001, 39.20660590000001, 0.5072722000000109, 30.584452200000005, 5.955517200000005, 3.2613922000000066, 0.0]]

		self.AVDIFF = self.avDiff()
		self.track = self.song_pool[self.songNum][0]

	def flag_current_song_done(self):
		print("flag called, songNum = " + str(self.songNum))
		row = self.songNum
		self.song_pool[row][1] = 1

	def get_current_track(self):
		print(self.track)
		return self.track

	def next_track(self, action):
		self.flag_current_song_done()
		if action == 'finish':

			currentSongNum = self.songNum
			row = self.songNum
			thresh1 = (self.AVDIFF/4)

			for i in range(len(self.prob_matrix[row])):
				if row == i:
					continue
				elif self.song_pool[i][1] == 0:
					if self.prob_matrix[row][i] < thresh1:
						self.track = self.song_pool[i][0]
						self.songNum = i
						break

			if self.songNum == currentSongNum:
				temp = self.prob_matrix[row]
				temp.pop(row)
				self.songNum = np.argmin(temp)

		elif action == 'like':

			currentSongNum = self.songNum
			row = self.songNum
			thresh = (self.AVDIFF/3)

			for i in range(len(self.prob_matrix[row])):
				if row == i:
					continue
				elif self.song_pool[i][1] == 0:
					if self.prob_matrix[row][i] < thresh:
						self.track = self.song_pool[i][0]
						self.songNum = i
						break

			if self.songNum == currentSongNum:
				temp = self.prob_matrix[row]
				temp.pop(row)
				self.songNum = np.argmin(temp)

		elif action == 'dislike':

			currentSongNum = self.songNum
			row = self.songNum
			thresh1 = (self.AVDIFF)

			for i in range(len(self.prob_matrix[row])):
				if row == i:
					continue
				elif self.song_pool[i][1] == 0:
					if self.prob_matrix[row][i] > thresh1:
						self.track = self.song_pool[i][0]
						self.songNum = i
						break

			if self.songNum == currentSongNum:
				temp = self.prob_matrix[row]
				temp.pop(row)
				self.songNum = np.argmax(temp)

		elif action == 'skip':

			currentSongNum = self.songNum
			row = self.songNum
			thresh1 = (self.AVDIFF/2)

			for i in range(len(self.prob_matrix[row])):
				if row == i:
					continue
				elif self.song_pool[i][1] == 0:
					if self.prob_matrix[row][i] > thresh1:
						self.track = self.song_pool[i][0]
						self.songNum = i
						break

			if self.songNum == currentSongNum:
				temp = self.prob_matrix[row]
				temp.pop(row)
				self.songNum = np.argmax(temp)

	def avDiff(self):
		## avDiff is the same for all rows
		row = 0
		tot = 0

		for i in range(len(self.prob_matrix[row])):
			tot = tot + self.prob_matrix[row][i]
		return tot/len(self.prob_matrix)

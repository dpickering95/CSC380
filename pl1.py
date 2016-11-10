#*****************************************************#
# Play List 1 (pl1)                                   #
# Seed Song is spotify:track:4US41qlynueHuB4czgwqi8   #
# "Throwing Stones" by Greatful Dead                  #
#*****************************************************#

class pl1:

	def __init__(self):

		self.songNum = 0 ## start counting from 0

		self.song_pool = [['60VcYHxoyOdZyFb1EaKJdN', 1], ['7jqxc3zCMwgi5JpYYWSPnO', 1], ['0fWe4v0BssKanrISjrYQ6T', 1], ['4qtvH9XElVrIYJ4R6dtePd', 1], ['3GtzidVERnat4IUCDtfRFb', 1], ['2x0supcZhd6NEH1nem9DnR', 1], ['2J0gSjejsefbV0TT8x8HxT', 1], ['35Myb6spNkKlRsZQcm95mP', 1], ['5gm95Qm0tUbBhckpCjR6Nc', 1], ['3GrLhTnxkqvG7sWszeCJy1', 1], ['4JwjzS9WFkWlpzGCwh82fn', 1], ['6FRBXNFfkFLONhrBwFenMx', 1], ['2fx1hkMHTVdDim274rwoPa', 1], ['5dBjkXiKkW66h625J6HdAo', 1], ['6Sgb8bxj8LqqW5QKGjzDWg', 1], ['0sDqo9UPzPUtu9wEkI3zRB', 1], ['4pZnAgLfd3tMBzXcUbfdqJ', 1], ['0SDPAqbWH5P5XGBY1wL7Wc', 1], ['0fbg5RN0bV7xqyJ0eaUD32', 1], ['3fwBARTubrCw4DQosyizcP', 1], ['60Rw5qamwihreiPlNM2pcZ', 1], ['2XXGM19E3Zp32Tkr0S4vEA', 1], ['69BhgVzGUe3V4QMFekmttL', 1], ['3rwFEFOQl8tCgJX96qRTX3', 1], ['1c3Q9jT16mm2FKwgxDKjaK', 1], ['64lGOBE0UWUkRXOzMP7Lmr', 1], ['5Ca147MgjWPIaY6WIrMhFO', 1], ['0leJbPzMGogMSlENibTm9B', 1], ['1gCE4LxErCB25MSERdLCZX', 1], ['6CMcrb7oQalm6lCfa1S1WR', 1]]

		self.prob_matrix = [[0.0, 73.41969999999999, 62.5888, 90.28699302, 77.72064999999999, 38.611709999999995, 49.09759999999999, 92.28, 37.1562, 57.457629999999995, 94.47354929999999, 66.95826599999998, 75.81580999999998, 49.3848524, 49.823799999999984, 99.11366, 68.715, 78.12673, 70.13539999999999, 85.77629999999999, 31.171595699999987, 45.91569999999999, 75.05229849999999, 29.50774999999999, 83.00393, 30.332251599999992, 48.5012, 63.36503999999999, 74.75719999999998, 48.72485509999999], 
[73.41969999999999, 0.0, 12.483899999999993, 29.96149302, 8.103749999999994, 35.45201, 29.646700000000006, 33.0007, 38.862899999999996, 18.829929999999997, 34.206849299999995, 14.804566000000005, 15.582709999999995, 26.9281524, 30.32390000000001, 35.534560000000006, 11.043299999999993, 17.929030000000004, 9.628100000000003, 25.361399999999996, 42.99169570000001, 28.816000000000006, 14.686598499999999, 45.60085, 22.164229999999996, 45.520951600000004, 26.119499999999995, 10.611740000000001, 13.518299999999993, 27.489155100000005], 
[62.5888, 12.483899999999993, 0.0, 28.991993019999992, 16.784849999999988, 25.913910000000005, 32.37020000000001, 31.674199999999995, 35.9664, 8.200830000000002, 33.221349299999986, 5.551465999999988, 14.50100999999999, 16.535252400000005, 18.478000000000012, 37.60406, 7.505199999999999, 16.79993, 8.729599999999994, 24.99849999999999, 35.90919570000001, 18.913900000000012, 14.516498499999994, 35.62235000000001, 22.536129999999993, 34.66245160000001, 20.145400000000002, 2.1052399999999913, 13.025199999999987, 18.08305510000001], 
[90.28699302, 29.96149302, 28.991993019999992, 0.0, 21.857743020000004, 51.80828302, 59.09279302, 6.016193019999999, 62.73439301999999, 33.074636979999994, 6.245443719999997, 26.830387020000003, 14.619203020000004, 40.933340619999996, 42.50199302000001, 12.941333020000005, 23.312993019999997, 12.219263019999993, 20.853593019999995, 4.634493020000003, 62.64580268, 44.533906980000005, 15.302505479999997, 60.92324302, 8.06406302, 60.33074142, 47.231406979999996, 28.805753020000004, 16.555793020000007, 42.21913792], 
[77.72064999999999, 8.103749999999994, 16.784849999999988, 21.857743020000004, 0.0, 39.576539999999994, 37.289049999999996, 25.090450000000008, 43.16464999999999, 22.93897999999999, 26.1030993, 18.913843999999997, 7.510459999999999, 31.036402399999993, 34.62485, 27.502990000000008, 15.19724999999999, 9.84272000000001, 10.077849999999994, 17.48835, 47.0999457, 32.92505, 6.583648500000005, 49.7689, 14.118320000000004, 49.629201599999995, 30.22854999999999, 14.779609999999996, 5.798050000000001, 31.598205099999998], 
[38.611709999999995, 35.45201, 25.913910000000005, 51.80828302, 39.576539999999994, 0.0, 11.02211, 55.11571, 13.001509999999993, 19.093920000000004, 56.0536393, 28.594355999999994, 37.45552, 10.906942400000004, 12.729909999999993, 60.944050000000004, 30.148710000000005, 39.78358000000001, 32.60931, 47.42341, 11.432485700000006, 7.554389999999995, 36.8365885, 10.211960000000005, 44.47622, 10.087741600000003, 10.494890000000005, 25.160669999999996, 36.813109999999995, 10.439145099999998], 
[49.09759999999999, 29.646700000000006, 32.37020000000001, 59.09279302, 37.289049999999996, 11.02211, 0.0, 62.333400000000005, 14.569599999999996, 26.420030000000008, 63.3381493, 35.920666, 44.74161, 18.211252400000006, 19.999799999999993, 64.74586000000001, 37.494200000000006, 47.08913000000001, 38.960800000000006, 54.7397, 18.496995700000006, 14.8781, 43.8466985, 21.186150000000005, 51.40433, 21.026251600000002, 12.27560000000001, 30.39904, 42.703, 17.2432551], 
[92.28, 33.0007, 31.674199999999995, 6.016193019999999, 25.090450000000008, 55.11571, 62.333400000000005, 0.0, 64.5222, 36.929829999999995, 4.441549299999995, 32.53226600000001, 19.923410000000004, 44.9788524, 47.08820000000001, 9.013260000000006, 29.094999999999995, 16.244329999999994, 23.833399999999997, 7.979700000000006, 66.43439570000001, 47.582300000000004, 18.6002985, 64.74955, 12.987930000000002, 64.0936516, 50.950799999999994, 32.41644000000001, 20.50700000000001, 45.600855100000004], 
[37.1562, 38.862899999999996, 35.9664, 62.73439301999999, 43.16464999999999, 13.001509999999993, 14.569599999999996, 64.5222, 0.0, 31.766029999999997, 68.96374929999999, 41.26046599999999, 50.235609999999994, 23.801052399999996, 24.018399999999986, 68.42546, 43.1048, 52.51853, 41.8852, 58.20189999999999, 7.974595700000011, 20.200499999999987, 49.44209849999999, 10.737750000000009, 57.037729999999996, 10.109851600000006, 17.503, 36.07863999999999, 46.19719999999999, 22.516655099999994], 
[57.457629999999995, 18.829929999999997, 8.200830000000002, 33.074636979999994, 22.93897999999999, 19.093920000000004, 26.420030000000008, 36.929829999999995, 31.766029999999997, 0.0, 37.23128069999999, 9.50176399999999, 18.501979999999993, 8.492777600000002, 11.727830000000012, 43.795970000000004, 11.628630000000003, 20.8729, 15.365229999999997, 29.75132999999999, 29.93803430000001, 11.56793000000001, 20.140131499999995, 28.26188000000001, 26.619699999999995, 27.415378400000005, 14.266429999999998, 8.284589999999994, 19.27242999999999, 10.086774900000007], 
[94.47354929999999, 34.206849299999995, 33.221349299999986, 6.245443719999997, 26.1030993, 56.0536393, 63.3381493, 4.441549299999995, 68.96374929999999, 37.23128069999999, 0.0, 29.050943300000004, 18.7757593, 45.162703099999995, 44.951349300000004, 10.808289300000009, 25.94234929999999, 16.44521929999999, 27.082949299999996, 10.8798493, 66.87524640000001, 48.763350700000004, 19.547949199999994, 65.1399993, 12.309419299999998, 64.5539023, 51.460850699999995, 33.0511093, 22.7665493, 46.4485058], 
[66.95826599999998, 14.804566000000005, 5.551465999999988, 26.830387020000003, 18.913843999999997, 28.594355999999994, 35.920666, 32.53226600000001, 41.26046599999999, 9.50176399999999, 29.050943300000004, 0.0, 12.778416000000002, 17.71044639999999, 17.300466, 39.77060600000001, 3.7670660000000096, 16.37753600000001, 11.339666000000006, 25.725966, 39.4397897, 21.063693999999998, 16.115692500000005, 37.762516, 20.518136000000002, 36.911045599999994, 23.762193999999987, 5.639225999999998, 15.247065999999998, 18.746249099999996], 
[75.81580999999998, 15.582709999999995, 14.50100999999999, 14.619203020000004, 7.510459999999999, 37.45552, 44.74161, 19.923410000000004, 50.235609999999994, 18.501979999999993, 18.7757593, 12.778416000000002, 0.0, 26.554862399999994, 28.484010000000005, 27.009470000000007, 9.466209999999993, 3.6939400000000076, 8.354809999999993, 12.951509999999997, 48.2806057, 30.067510000000002, 3.3981085000000024, 46.59776, 8.185740000000003, 45.8918616, 32.76500999999999, 14.47465, 4.110610000000002, 27.752665099999998], 
[49.3848524, 26.9281524, 16.535252400000005, 40.933340619999996, 31.036402399999993, 10.906942400000004, 18.211252400000006, 44.9788524, 23.801052399999996, 8.492777600000002, 45.162703099999995, 17.71044639999999, 26.554862399999994, 0.0, 3.5892524000000092, 51.8851924, 19.4556524, 28.8953224, 23.640252399999998, 37.84055239999999, 21.733343300000012, 3.600647600000009, 28.251246099999996, 20.053102400000007, 34.44672239999999, 19.428600800000005, 6.298147599999998, 16.373812399999995, 27.43445239999999, 1.8378027000000055], 
[49.823799999999984, 30.32390000000001, 18.478000000000012, 42.50199302000001, 34.62485, 12.729909999999993, 19.999799999999993, 47.08820000000001, 24.018399999999986, 11.727830000000012, 44.951349300000004, 17.300466, 28.484010000000005, 3.5892524000000092, 0.0, 55.419060000000016, 19.449200000000012, 32.07633000000001, 26.56960000000001, 41.1925, 23.5377957, 5.181899999999999, 31.840498500000006, 21.839349999999996, 36.24013, 20.827451599999993, 7.783399999999988, 19.931240000000003, 30.8402, 3.0470551000000032], 
[99.11366, 35.534560000000006, 37.60406, 12.941333020000005, 27.502990000000008, 60.944050000000004, 64.74586000000001, 9.013260000000006, 68.42546, 43.795970000000004, 10.808289300000009, 39.77060600000001, 27.009470000000007, 51.8851924, 55.419060000000016, 0.0, 36.034060000000004, 23.39307, 29.084660000000003, 14.553560000000012, 68.35593570000002, 54.298040000000015, 24.212638500000008, 70.54629000000001, 20.28027000000001, 70.4405916, 53.121539999999996, 35.78338000000001, 24.58106000000001, 53.50919510000001], 
[68.715, 11.043299999999993, 7.505199999999999, 23.312993019999997, 15.19724999999999, 30.148710000000005, 37.494200000000006, 29.094999999999995, 43.1048, 11.628630000000003, 25.94234929999999, 3.7670660000000096, 9.466209999999993, 19.4556524, 19.449200000000012, 36.034060000000004, 0.0, 13.02713, 7.834599999999997, 21.96469999999999, 41.10719570000001, 22.955100000000012, 12.457298499999995, 39.32235000000001, 16.790929999999992, 38.844451600000006, 25.7016, 7.1992400000000085, 11.73839999999999, 20.631855100000006], 
[78.12673, 17.929030000000004, 16.79993, 12.219263019999993, 9.84272000000001, 39.78358000000001, 47.08913000000001, 16.244329999999994, 52.51853, 20.8729, 16.44521929999999, 16.37753600000001, 3.6939400000000076, 28.8953224, 32.07633000000001, 23.39307, 13.02713, 0.0, 10.637730000000003, 9.34842999999999, 50.624665700000016, 32.33557000000001, 3.2841685000000047, 48.94182000000001, 5.769799999999993, 48.17592160000001, 35.03307, 16.81871000000001, 6.469530000000012, 30.386725100000007], 
[70.13539999999999, 9.628100000000003, 8.729599999999994, 20.853593019999995, 10.077849999999994, 32.60931, 38.960800000000006, 23.833399999999997, 41.8852, 15.365229999999997, 27.082949299999996, 11.339666000000006, 8.354809999999993, 23.640252399999998, 26.56960000000001, 29.084660000000003, 7.834599999999997, 10.637730000000003, 0.0, 16.453099999999992, 42.60779570000001, 25.70170000000001, 7.930898499999998, 42.462950000000006, 15.953529999999995, 42.0690516, 27.234199999999998, 8.693840000000007, 4.730399999999992, 24.904455100000003], 
[85.77629999999999, 25.361399999999996, 24.99849999999999, 4.634493020000003, 17.48835, 47.42341, 54.7397, 7.979700000000006, 58.20189999999999, 29.75132999999999, 10.8798493, 25.725966, 12.951509999999997, 37.84055239999999, 41.1925, 14.553560000000012, 21.96469999999999, 9.34842999999999, 16.453099999999992, 0.0, 58.5926957, 40.2294, 10.997998499999994, 56.76985, 6.143629999999998, 56.521951599999994, 43.40689999999999, 24.43674, 12.723300000000002, 39.1645551], 
[31.171595699999987, 42.99169570000001, 35.90919570000001, 62.64580268, 47.0999457, 11.432485700000006, 18.496995700000006, 66.43439570000001, 7.974595700000011, 29.93803430000001, 66.87524640000001, 39.4397897, 48.2806057, 21.733343300000012, 23.5377957, 68.35593570000002, 41.10719570000001, 50.624665700000016, 42.60779570000001, 58.5926957, 0.0, 18.8521043, 47.882702800000004, 2.7718456999999974, 55.906265700000006, 2.829344100000007, 17.461604300000012, 34.208555700000005, 46.2409957, 21.755340600000004], 
[45.91569999999999, 28.816000000000006, 18.913900000000012, 44.533906980000005, 32.92505, 7.554389999999995, 14.8781, 47.582300000000004, 20.200499999999987, 11.56793000000001, 48.763350700000004, 21.063693999999998, 30.067510000000002, 3.600647600000009, 5.181899999999999, 54.298040000000015, 22.955100000000012, 32.33557000000001, 25.70170000000001, 40.2294, 18.8521043, 0.0, 30.128601500000006, 17.199949999999998, 37.298170000000006, 16.715448399999996, 3.4885000000000113, 18.514660000000006, 29.9991, 2.9032449000000033], 
[75.05229849999999, 14.686598499999999, 14.516498499999994, 15.302505479999997, 6.583648500000005, 36.8365885, 43.8466985, 18.6002985, 49.44209849999999, 20.140131499999995, 19.547949199999994, 16.115692500000005, 3.3981085000000024, 28.251246099999996, 31.840498500000006, 24.212638500000008, 12.457298499999995, 3.2841685000000047, 7.930898499999998, 10.997998499999994, 47.882702800000004, 30.128601500000006, 0.0, 47.0485485, 8.032368499999997, 46.8440469, 32.6691015, 13.835258500000005, 4.087698500000007, 29.3054434], 
[29.50774999999999, 45.60085, 35.62235000000001, 60.92324302, 49.7689, 10.211960000000005, 21.186150000000005, 64.74955, 10.737750000000009, 28.26188000000001, 65.1399993, 37.762516, 46.59776, 20.053102400000007, 21.839349999999996, 70.54629000000001, 39.32235000000001, 48.94182000000001, 42.462950000000006, 56.76985, 2.7718456999999974, 17.199949999999998, 47.0485485, 0.0, 54.044180000000004, 1.1365016000000037, 20.23345000000001, 34.995290000000004, 46.483149999999995, 20.0771051], 
[83.00393, 22.164229999999996, 22.536129999999993, 8.06406302, 14.118320000000004, 44.47622, 51.40433, 12.987930000000002, 57.037729999999996, 26.619699999999995, 12.309419299999998, 20.518136000000002, 8.185740000000003, 34.44672239999999, 36.24013, 20.28027000000001, 16.790929999999992, 5.769799999999993, 15.953529999999995, 6.143629999999998, 55.906265700000006, 37.298170000000006, 8.032368499999997, 54.044180000000004, 0.0, 53.8355216, 40.69266999999999, 21.704890000000002, 12.107330000000005, 34.5249251], 
[30.332251599999992, 45.520951600000004, 34.66245160000001, 60.33074142, 49.629201599999995, 10.087741600000003, 21.026251600000002, 64.0936516, 10.109851600000006, 27.415378400000005, 64.5539023, 36.911045599999994, 45.8918616, 19.428600800000005, 20.827451599999993, 70.4405916, 38.844451600000006, 48.17592160000001, 42.0690516, 56.521951599999994, 2.829344100000007, 16.715448399999996, 46.8440469, 1.1365016000000037, 53.8355216, 0.0, 19.416948400000006, 34.9412116, 45.967651599999996, 19.3986035], 
[48.5012, 26.119499999999995, 20.145400000000002, 47.231406979999996, 30.22854999999999, 10.494890000000005, 12.27560000000001, 50.950799999999994, 17.503, 14.266429999999998, 51.460850699999995, 23.762193999999987, 32.76500999999999, 6.298147599999998, 7.783399999999988, 53.121539999999996, 25.7016, 35.03307, 27.234199999999998, 43.40689999999999, 17.461604300000012, 3.4885000000000113, 32.6691015, 20.23345000000001, 40.69266999999999, 19.416948400000006, 0.0, 19.03415999999999, 30.76859999999999, 6.255744899999992], 
[63.36503999999999, 10.611740000000001, 2.1052399999999913, 28.805753020000004, 14.779609999999996, 25.160669999999996, 30.39904, 32.41644000000001, 36.07863999999999, 8.284589999999994, 33.0511093, 5.639225999999998, 14.47465, 16.373812399999995, 19.931240000000003, 35.78338000000001, 7.1992400000000085, 16.81871000000001, 8.693840000000007, 24.43674, 34.208555700000005, 18.514660000000006, 13.835258500000005, 34.995290000000004, 21.704890000000002, 34.9412116, 19.03415999999999, 0.0, 12.430439999999997, 17.725815100000002], 
[74.75719999999998, 13.518299999999993, 13.025199999999987, 16.555793020000007, 5.798050000000001, 36.813109999999995, 42.703, 20.50700000000001, 46.19719999999999, 19.27242999999999, 22.7665493, 15.247065999999998, 4.110610000000002, 27.43445239999999, 30.8402, 24.58106000000001, 11.73839999999999, 6.469530000000012, 4.730399999999992, 12.723300000000002, 46.2409957, 29.9991, 4.087698500000007, 46.483149999999995, 12.107330000000005, 45.967651599999996, 30.76859999999999, 12.430439999999997, 0.0, 29.210255099999998], 
[48.72485509999999, 27.489155100000005, 18.08305510000001, 42.21913792, 31.598205099999998, 10.439145099999998, 17.2432551, 45.600855100000004, 22.516655099999994, 10.086774900000007, 46.4485058, 18.746249099999996, 27.752665099999998, 1.8378027000000055, 3.0470551000000032, 53.50919510000001, 20.631855100000006, 30.386725100000007, 24.904455100000003, 39.1645551, 21.755340600000004, 2.9032449000000033, 29.3054434, 20.0771051, 34.5249251, 19.3986035, 6.255744899999992, 17.725815100000002, 29.210255099999998, 0.0]]

		self.AVDIFF = self.avDiff()
		self.track = self.song_pool[self.songNum][0]

	def flag_current_song_done(self):
		print("flag called, songNum = " + str(self.songNum))
		row = self.songNum
		self.song_pool[self.songNum][1] = 0
		

	def get_current_track(self):
		print(self.track)
		return self.track
		

	def next_track(self, action):
		self.flag_current_song_done()
		if action == 'finish':
			
			row = self.songNum		
			thresh1 = (self.AVDIFF/2)
			thresh2 = (self.AVDIFF/2)

			for i in range(len(self.prob_matrix[row])):
				if self.song_pool[row] == i:
					continue
				elif self.song_pool[row][1] == 1:
					if self.prob_matrix[row][i] < thresh1 or self.prob_matrix[row][i] > thresh2:
						self.track = self.song_pool[i][0]
						self.songNum = i
						break

	def avDiff(self):
		## avDiff is the same for all rows
		row = 0
		tot = 0

		for i in range(len(self.prob_matrix[row])):
			tot = tot + self.prob_matrix[row][i]
		return tot/len(self.prob_matrix)

		

	



#*****************************************************#
# Play List 7 (pl7)                                   #
# Seed Song is spotify:track:5E30LdtzQTGqRvNd7l6kG5   #
# "Daddy Issues" by The Neighbourhood                 #
#*****************************************************#

import numpy as np

class pl7

	def __init__(self):

		self.songNum = 0 ## start counting from 0

		self.song_pool = [['4AyoAGuhE8gydBPrczuhbl', 0], ['7tKnaB8gsXxyPScxEwzQ9N', 0], ['3gM7tsNjkOnuswaPgncLJY', 0], ['1iyYqtHB4w5Jl2BGx71emK', 0], ['0zU2NTeAeyzTX53RwiTWN5', 0], ['3Y5fO1e3ldJMvGP4wb4jB1', 0], ['0KS9V6ihDVgbotoOov3QZH', 0], ['1AUT0H87ysQgfRtVWWcrTZ', 0], ['2lXheyXftSMWhBvrV3EhAX', 0], ['5d3HKoKvqtN0gRDjt3RcBL', 0], ['573latfTMO7SpGtStVrQx5', 0], ['1Nh3lQFZsnyCmFPCK93avB', 0], ['3mMcONXl666919f7y6tA5j', 0], ['3ym8RPF4EQPqtW0v8G44BT', 0], ['6eemPcEyvaxp7gDhDtY8HT', 0], ['03WmeqPnjaBnm4lfwm8v8z', 0], ['5IhDbkr7TIy9trIOnW8cv1', 0], ['4NXRIJkvnBVOqdTQeUOX6W', 0], ['6YUVY9hQSUnBve3MBRw1wd', 0], ['4xjkURdXzlD9v41aqxKj14', 0], ['3kb72STxc2959ZqsTwu52i', 0], ['5n0CTysih20NYdT2S0Wpe8', 0], ['2tznHmp70DxMyr2XhWLOW0', 0], ['4sebUbjqbcgDSwG6PbSGI0', 0], ['0X0Lz7LwpiIWcdGqVWaxXD', 0], ['12sYWro0wGQpq0rjE0lKcm', 0], ['1Q3t9fWvHUXKsMmpD2XpUu', 0], ['48sc7vBJeNoCEQhxO3zYKA', 0], ['0f8MA1n2bvsg7eGvYZ4lhx', 0], ['4dpEYOPcmHNfvERbiajp3G', 0]]

		self.prob_matrix = [[0.0, 15.722070100000003, 15.246789740000004, 24.189818390000003, 11.196029900000015, 2.8966700999999997, 24.200287800000005, 7.402529899999997, 13.789970100000005, 8.103350099999991, 7.359384900000011, 12.414624100000001, 26.013638399999987, 16.990089900000015, 33.0801701, 64.1724801, 13.025330100000014, 13.415390100000016, 49.3773701, 13.227970100000004, 18.41947009999998, 63.59398290000001, 27.62167010000001, 12.384669089999978, 12.083959899999982, 36.08564090000001, 5.291303300000009, 76.06117010000001, 28.341612099999995, 6.779814000000018], [15.722070100000003, 0.0, 0.5309263600000009, 9.66016771, 5.748099999999989, 15.270600000000004, 9.596520300000002, 21.9284, 5.281299999999999, 23.657479999999996, 10.755454999999992, 27.804554000000007, 41.41543169999999, 1.3123600000000106, 47.308099999999996, 49.65261, 8.55973999999999, 8.965319999999988, 34.8539, 3.427899999999998, 32.765199999999986, 47.898053000000004, 13.24760000000001, 27.80060100999998, 26.713829999999984, 20.377911000000008, 11.765366799999994, 60.36510000000001, 43.731542, 12.357884099999985], [15.246789740000004, 0.5309263600000009, 0.0, 9.30477135, 6.106419639999991, 15.144126360000005, 9.23050194, 22.29731964, 4.88222636, 23.175446359999995, 10.373354639999993, 27.489972360000007, 41.11035133999999, 1.7477596400000102, 47.815626359999996, 49.29231636, 8.167466359999992, 8.653206359999988, 34.51282636, 3.9536263599999986, 33.16412635999998, 48.36957264, 12.749126360000009, 27.47212534999998, 26.828749639999984, 20.847890640000006, 12.272886439999994, 60.839026360000005, 43.41618436, 12.865403739999987], [24.189818390000003, 9.66016771, 9.30477135, 0.0, 15.40384828999999, 22.240367710000005, 0.09235259000000007, 29.58414829, 11.711467709999999, 32.14848771, 19.17858328999999, 36.173213710000006, 49.79357998999999, 8.878988289999988, 56.911867709999996, 41.998957710000006, 16.98550770999999, 17.380447709999988, 27.20806771, 13.030867709999999, 42.42536770999998, 41.47780129, 5.649367710000009, 34.17436669999998, 33.905978289999986, 13.956119290000007, 21.383115089999993, 51.94486771000001, 50.09979371, 19.961632389999988], [11.196029900000015, 5.748099999999989, 6.106419639999991, 15.40384828999999, 0.0, 11.007700000000014, 15.329517699999991, 16.31530000000001, 5.003999999999992, 19.272980000000004, 6.4906650000000035, 23.610654000000018, 37.1662683, 6.571460000000001, 42.54840000000001, 55.38491, 4.2743600000000015, 4.771419999999998, 40.59139999999999, 2.4759999999999915, 27.362099999999995, 53.137446999999995, 18.7899, 23.547898989999993, 22.504269999999995, 25.470528999999996, 6.507933200000004, 65.0194, 39.53764200000001, 7.078015899999997], [2.8966700999999997, 15.270600000000004, 15.144126360000005, 22.240367710000005, 11.007700000000014, 0.0, 22.196120300000004, 7.718199999999997, 11.986500000000005, 10.837879999999991, 7.532055000000011, 14.821154000000002, 28.381631699999986, 16.560560000000013, 34.7407, 63.93941000000001, 13.198860000000014, 13.509920000000015, 49.373900000000006, 12.652500000000003, 20.547399999999982, 62.89345300000001, 27.805000000000014, 12.676201009999978, 11.82882999999998, 35.39971100000001, 4.776366800000009, 73.39030000000001, 28.540141999999996, 4.1924841000000175], [24.200287800000005, 9.596520300000002, 9.23050194, 0.09235259000000007, 15.329517699999991, 22.196120300000004, 0.0, 29.5188177, 11.773820299999999, 32.134240299999995, 19.240852699999994, 36.2655663, 49.88588859999999, 8.80465769999999, 56.8676203, 42.062710300000006, 17.03726029999999, 17.442800299999988, 27.2824203, 12.997220299999999, 42.36172029999999, 41.4154707, 5.683120300000008, 34.25611928999998, 33.87224769999999, 13.893788700000007, 21.324784499999993, 51.882620300000006, 50.192124299999996, 19.917301799999986], [7.402529899999997, 21.9284, 22.29731964, 29.58414829, 16.31530000000001, 7.718199999999997, 29.5188177, 0.0, 19.1843, 15.363879999999993, 14.752965000000009, 19.690954000000005, 33.26296829999998, 22.72156000000001, 38.6393, 71.57501, 20.42786000000001, 20.809720000000013, 56.771699999999996, 18.6563, 21.204799999999985, 69.344747, 34.99720000000001, 17.64219898999998, 16.584569999999985, 41.661429000000005, 10.224833200000006, 76.9287, 33.617942, 9.701315900000013], [13.789970100000005, 5.281299999999999, 4.88222636, 11.711467709999999, 5.003999999999992, 11.986500000000005, 11.773820299999999, 19.1843, 0.0, 21.758779999999998, 7.507554999999995, 24.626654000000006, 38.22813169999999, 6.563660000000009, 46.658, 52.44791, 5.3567599999999915, 5.7874199999999885, 37.614599999999996, 2.7605999999999997, 31.969899999999985, 53.169953, 15.939500000000008, 22.66450100999998, 23.631729999999987, 25.659211000000006, 11.115266799999995, 63.63700000000001, 38.818042, 9.707784099999987], [8.103350099999991, 23.657479999999996, 23.175446359999995, 32.14848771, 19.272980000000004, 10.837879999999991, 32.134240299999995, 15.363879999999993, 21.758779999999998, 0.0, 15.318175000000002, 4.341274000000011, 17.952911699999994, 24.918880000000005, 24.989380000000004, 72.12953, 20.988020000000006, 21.374040000000008, 57.347379999999994, 21.162619999999997, 10.33467999999999, 71.535333, 35.58688, 4.317881009999987, 3.9993099999999897, 44.014431, 13.2326468, 84.00238, 20.268262000000004, 14.721164100000008], [7.359384900000011, 10.755454999999992, 10.373354639999993, 19.17858328999999, 6.4906650000000035, 7.532055000000011, 19.240852699999994, 14.752965000000009, 7.507554999999995, 15.318175000000002, 0.0, 17.11998900000001, 30.737823299999995, 12.029905000000003, 40.20355500000001, 56.928644999999996, 5.791195000000002, 6.056755000000004, 42.10815499999999, 8.229554999999994, 25.493654999999993, 58.652618, 20.457055, 17.220053989999986, 19.176394999999992, 31.130944, 4.660688200000001, 71.120555, 34.34717700000001, 5.2531708999999935], [12.414624100000001, 27.804554000000007, 27.489972360000007, 36.173213710000006, 23.610654000000018, 14.821154000000002, 36.2655663, 19.690954000000005, 24.626654000000006, 4.341274000000011, 17.11998900000001, 0.0, 15.022385699999983, 29.109794000000015, 25.146653999999995, 72.30774400000001, 20.904294000000014, 21.03723400000002, 58.955254000000004, 25.154654000000008, 10.670153999999979, 75.518607, 37.068154000000014, 3.965155010000025, 4.120383999999979, 47.99692500000001, 17.36192080000001, 87.99765400000001, 19.287787999999992, 18.80043810000002], [26.013638399999987, 41.41543169999999, 41.11035133999999, 49.79357998999999, 37.1662683, 28.381631699999986, 49.88588859999999, 33.26296829999998, 38.22813169999999, 17.952911699999994, 30.737823299999995, 15.022385699999983, 0.0, 42.7277283, 10.60433170000001, 86.8040417, 35.9108917, 35.7791517, 72.55553169999999, 38.77073169999999, 12.058231700000004, 89.00222129999999, 50.5498317, 18.935830690000007, 16.811598300000004, 61.61127929999999, 30.947935099999995, 101.4793317, 4.774173700000011, 32.364052400000006], [16.990089900000015, 1.3123600000000106, 1.7477596400000102, 8.878988289999988, 6.571460000000001, 16.560560000000013, 8.80465769999999, 22.72156000000001, 6.563660000000009, 24.918880000000005, 12.029905000000003, 29.109794000000015, 42.7277283, 0.0, 48.18606000000001, 48.863749999999996, 9.826900000000002, 10.270639999999997, 34.084259999999986, 4.32306000000001, 33.63556, 46.69310699999999, 12.425559999999997, 29.09055898999999, 28.024129999999996, 19.171448999999996, 12.643193200000004, 59.162459999999996, 45.03678200000001, 13.235675899999997], [33.0801701, 47.308099999999996, 47.815626359999996, 56.911867709999996, 42.54840000000001, 34.7407, 56.8676203, 38.6393, 46.658, 24.989380000000004, 40.20355500000001, 25.146653999999995, 10.60433170000001, 48.18606000000001, 0.0, 96.61091, 45.870360000000005, 46.18142000000001, 82.0454, 44.16, 17.596100000000014, 94.527953, 60.50950000000001, 28.832501010000016, 23.028330000000015, 66.90701100000001, 36.28926680000001, 106.93100000000001, 7.987641999999999, 37.727784100000015], [64.1724801, 49.65261, 49.29231636, 41.998957710000006, 55.38491, 63.93941000000001, 42.062710300000006, 71.57501, 52.44791, 72.12953, 56.928644999999996, 72.30774400000001, 86.8040417, 48.863749999999996, 96.61091, 0.0, 53.23515, 53.64450999999999, 14.834510000000005, 52.95309, 82.41780999999999, 3.348862999999998, 36.71241, 72.21941100999999, 75.66044, 29.931181, 61.364176799999996, 15.839910000000003, 90.802732, 61.90669409999999], [13.025330100000014, 8.55973999999999, 8.167466359999992, 16.98550770999999, 4.2743600000000015, 13.198860000000014, 17.03726029999999, 20.42786000000001, 5.3567599999999915, 20.988020000000006, 5.791195000000002, 20.904294000000014, 35.9108917, 9.826900000000002, 45.870360000000005, 53.23515, 0.0, 0.49705999999999717, 39.83735999999999, 6.065639999999991, 31.270659999999996, 56.438312999999994, 17.731859999999998, 19.312861009999992, 24.875289999999996, 28.922450999999995, 10.327626800000003, 68.90536, 40.06928200000001, 10.920144099999996], [13.415390100000016, 8.965319999999988, 8.653206359999988, 17.380447709999988, 4.771419999999998, 13.509920000000015, 17.442800299999988, 20.809720000000013, 5.7874199999999885, 21.374040000000008, 6.056755000000004, 21.03723400000002, 35.7791517, 10.270639999999997, 46.18142000000001, 53.64450999999999, 0.49705999999999717, 0.0, 40.214019999999984, 6.431419999999988, 31.52892, 56.855372999999986, 18.228919999999995, 19.371921009999994, 25.15515, 29.333690999999995, 10.638686800000006, 69.32242, 40.32502200000001, 11.2312041], [49.3773701, 34.8539, 34.51282636, 27.20806771, 40.59139999999999, 49.373900000000006, 27.2824203, 56.771699999999996, 37.614599999999996, 57.347379999999994, 42.10815499999999, 58.955254000000004, 72.55553169999999, 34.084259999999986, 82.0454, 14.834510000000005, 39.83735999999999, 40.214019999999984, 0.0, 38.1506, 67.58329999999998, 16.641353000000002, 22.330899999999993, 58.96590100999998, 61.01912999999998, 15.265810999999992, 46.57066679999999, 29.10840000000001, 76.210242, 47.113184099999984], [13.227970100000004, 3.427899999999998, 3.9536263599999986, 13.030867709999999, 2.4759999999999915, 12.652500000000003, 12.997220299999999, 18.6563, 2.7605999999999997, 21.162619999999997, 8.229554999999994, 25.154654000000008, 38.77073169999999, 4.32306000000001, 44.16, 52.95309, 6.065639999999991, 6.431419999999988, 38.1506, 0.0, 29.466499999999986, 50.765953, 16.675500000000007, 25.18250100999998, 24.079729999999987, 23.042271000000003, 8.455266799999995, 62.891000000000005, 41.081642, 8.997784099999988], [18.41947009999998, 32.765199999999986, 33.16412635999998, 42.42536770999998, 27.362099999999995, 20.547399999999982, 42.36172029999999, 21.204799999999985, 31.969899999999985, 10.33467999999999, 25.493654999999993, 10.670153999999979, 12.058231700000004, 33.63556, 17.596100000000014, 82.41780999999999, 31.270659999999996, 31.52892, 67.58329999999998, 29.466499999999986, 0.0, 80.15045299999998, 45.803999999999995, 14.549601010000003, 8.75943, 52.50511099999999, 21.06776679999999, 89.77749999999999, 14.539942000000014, 22.535884099999997], [63.59398290000001, 47.898053000000004, 48.36957264, 41.47780129, 53.137446999999995, 62.89345300000001, 41.4154707, 69.344747, 53.169953, 71.535333, 58.652618, 75.518607, 89.00222129999999, 46.69310699999999, 94.527953, 3.348862999999998, 56.438312999999994, 56.855372999999986, 16.641353000000002, 50.765953, 80.15045299999998, 0.0, 38.776253, 75.43345198999998, 74.40137699999998, 27.751081999999997, 59.1346862, 13.020953000000006, 91.433595, 59.65256889999999], [27.62167010000001, 13.24760000000001, 12.749126360000009, 5.649367710000009, 18.7899, 27.805000000000014, 5.683120300000008, 34.99720000000001, 15.939500000000008, 35.58688, 20.457055, 37.068154000000014, 50.5498317, 12.425559999999997, 60.50950000000001, 36.71241, 17.731859999999998, 18.228919999999995, 22.330899999999993, 16.675500000000007, 45.803999999999995, 38.776253, 0.0, 36.99500100999999, 39.53182999999999, 11.404110999999999, 24.9583668, 51.2543, 54.73514200000001, 25.518484099999995], [12.384669089999978, 27.80060100999998, 27.47212534999998, 34.17436669999998, 23.547898989999993, 12.676201009999978, 34.25611928999998, 17.64219898999998, 22.66450100999998, 4.317881009999987, 17.220053989999986, 3.965155010000025, 18.935830690000007, 29.09055898999999, 28.832501010000016, 72.21941100999999, 19.312861009999992, 19.371921009999994, 58.96590100999998, 25.18250100999998, 14.549601010000003, 75.43345198999998, 36.99500100999999, 0.0, 5.854828990000004, 47.929509989999985, 17.306165789999987, 85.93050100999999, 21.05814301000002, 16.727283089999997], [12.083959899999982, 26.713829999999984, 26.828749639999984, 33.905978289999986, 22.504269999999995, 11.82882999999998, 33.87224769999999, 16.584569999999985, 23.631729999999987, 3.9993099999999897, 19.176394999999992, 4.120383999999979, 16.811598300000004, 28.024129999999996, 23.028330000000015, 75.66044, 24.875289999999996, 25.15515, 61.01912999999998, 24.079729999999987, 8.75943, 74.40137699999998, 39.53182999999999, 5.854828990000004, 0.0, 46.86885899999999, 16.25746319999999, 84.89332999999999, 17.033372000000014, 15.695945899999998], [36.08564090000001, 20.377911000000008, 20.847890640000006, 13.956119290000007, 25.470528999999996, 35.39971100000001, 13.893788700000007, 41.661429000000005, 25.659211000000006, 44.014431, 31.130944, 47.99692500000001, 61.61127929999999, 19.171448999999996, 66.90701100000001, 29.931181, 28.922450999999995, 29.333690999999995, 15.265810999999992, 23.042271000000003, 52.50511099999999, 27.751081999999997, 11.404110999999999, 47.929509989999985, 46.86885899999999, 0.0, 31.437344200000002, 40.052011, 63.885913, 31.976226899999993], [5.291303300000009, 11.765366799999994, 12.272886439999994, 21.383115089999993, 6.507933200000004, 4.776366800000009, 21.324784499999993, 10.224833200000006, 11.115266799999995, 13.2326468, 4.660688200000001, 17.36192080000001, 30.947935099999995, 12.643193200000004, 36.28926680000001, 61.364176799999996, 10.327626800000003, 10.638686800000006, 46.57066679999999, 8.455266799999995, 21.06776679999999, 59.1346862, 24.9583668, 17.306165789999987, 16.25746319999999, 31.437344200000002, 0.0, 70.7786668, 33.2889088, 1.4905173000000072], [76.06117010000001, 60.36510000000001, 60.839026360000005, 51.94486771000001, 65.0194, 73.39030000000001, 51.882620300000006, 76.9287, 63.63700000000001, 84.00238, 71.120555, 87.99765400000001, 101.4793317, 59.162459999999996, 106.93100000000001, 15.839910000000003, 68.90536, 69.32242, 29.10840000000001, 62.891000000000005, 89.77749999999999, 13.020953000000006, 51.2543, 85.93050100999999, 84.89332999999999, 40.052011, 70.7786668, 0.0, 101.924642, 69.3007841], [28.341612099999995, 43.731542, 43.41618436, 50.09979371, 39.53764200000001, 28.540141999999996, 50.192124299999996, 33.617942, 38.818042, 20.268262000000004, 34.34717700000001, 19.287787999999992, 4.774173700000011, 45.03678200000001, 7.987641999999999, 90.802732, 40.06928200000001, 40.32502200000001, 76.210242, 41.081642, 14.539942000000014, 91.433595, 54.73514200000001, 21.05814301000002, 17.033372000000014, 63.885913, 33.2889088, 101.924642, 0.0, 32.72742610000001], [6.779814000000018, 12.357884099999985, 12.865403739999987, 19.961632389999988, 7.078015899999997, 4.1924841000000175, 19.917301799999986, 9.701315900000013, 9.707784099999987, 14.721164100000008, 5.2531708999999935, 18.80043810000002, 32.364052400000006, 13.235675899999997, 37.727784100000015, 61.90669409999999, 10.920144099999996, 11.2312041, 47.113184099999984, 8.997784099999988, 22.535884099999997, 59.65256889999999, 25.518484099999995, 16.727283089999997, 15.695945899999998, 31.976226899999993, 1.4905173000000072, 69.3007841, 32.72742610000001, 0.0]]

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

			if self.songNum == currentSongNum:
				temp = self.prob_matrix[row]
				temp.pop(row)
				self.songNum = np.argmin(temp)

			if self.songNum == currentSongNum:
				temp = self.prob_matrix[row]
				temp.pop(row)
				self.songNum = np.argmin(temp)

		elif action == 'dislike':

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

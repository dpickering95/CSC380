#*****************************************************#
# Play List 6 (pl6)                                   #
# Seed Song is spotify:track:7tUUZ74ZhKN8B1IiMREYlO   #
# "Sense" by King Gizzard & The Lizard Wizard         #
#*****************************************************#

import numpy as np

class pl6:

	def __init__(self):

		self.songNum = 0 ## start counting from 0

		self.song_pool = [['4VAWLjoHleIvg2Dnkyv7PH', 0], ['7nBd0swyCrKU69QqJ254FL', 0], ['2RXwaxD5vfbNjsu5FPWb46', 0], ['3JKhqkUU02FTQtTVXmPT5j', 0], ['2enpvVKb3TncmvWecZkqJx', 0], ['1nOOaNCjxSjG0nFbA2peqE', 0], ['4XEQbMxh6ISs74ScO3OW0E', 0], ['5qci2nsICRk3V3tICZr4w6', 0], ['1pLjbiisxvrtp37sAst6JZ', 0], ['5wsIFLY5CHEzZllwNH5T6H', 0], ['1XeYAaPtV3HPPqfMS0ANNO', 0], ['7134BLbUr6djveEsr2CQFN', 0], ['7x3yqZnXWnLopmPDg0TYfv', 0], ['7DrwaZ7czId6Nm40esdSap', 0], ['1ku897rR9A6IfzWAORdxcB', 0], ['47NLFVzMNcYjyyYXj9Lk7o', 0], ['7vYmveK37j5mtN9uGp9WFd', 0], ['0aJlWrFBmarDHR1vcVfeA5', 0], ['7bTObOCv3SnJTr0hiafrxT', 0], ['2NgJraprzOanuaT42eYCNS', 0], ['0y6Mp5Y1OxHtzxi6AwewPt', 0], ['6hclzBnmKoeHe4B0VQhrDY', 0], ['0u1D0UwHULxLj1JEgjyCel', 0], ['3jb0Xm4izpeSZNMGxdtZkx', 0], ['6AuS0ZfvgkWJRmO3zW00vA', 0], ['1GgX1kUlKh3TPa3qEnCzwg', 0], ['0V1xJXwwuXsr5oW5nSBVOC', 0], ['0yZrGC0mYBfkWToPZbAiYm', 0], ['38nadnjqc7AURrFFD0NlIo', 0], ['4AkFbCis7PMJYVGnszF3BH', 0]]

		self.prob_matrix = [[0.0, 23.128355069999994, 75.65704000000001, 9.027160000000006, 11.985918700000003, 41.41435000000001, 2.431339999999994, 32.88084359999999, 3.712454300000001, 17.918028000000007, 25.309057209999988, 83.23600619999999, 36.692333999999995, 44.21105999999999, 32.4326394, 17.334454369999996, 56.56135766999999, 20.11713000000001, 74.67405600000001, 65.62242277, 11.68035000000001, 34.460760000000015, 19.156860000000005, 23.115606900000014, 12.302160000000002, 25.32276999999999, 7.462030000000002, 9.793479999999992, 15.774206, 18.605459999999997], [23.128355069999994, 0.0, 55.085295070000015, 14.92919506999999, 12.430673769999991, 18.448005070000015, 22.69669506999999, 11.848511469999998, 19.848155369999994, 5.215263069999988, 44.422702139999984, 62.10774887, 16.043621070000004, 24.547695069999996, 53.56371566999999, 36.65190069999999, 35.4330026, 7.611225069999984, 54.04829907000002, 45.01778770000001, 13.484865069999984, 14.178595070000016, 4.50449506999999, 7.395348169999979, 20.84119506999999, 47.14986506999999, 16.760325069999993, 29.952235069999986, 12.299561069999998, 40.678895069999996], [75.65704000000001, 55.085295070000015, 0.0, 67.7278, 66.97117870000001, 37.47169, 76.98070000000001, 43.52378360000002, 74.39541430000001, 57.75803200000001, 99.12399721, 7.584946199999985, 39.23127400000001, 35.613100000000024, 106.37957940000001, 91.47219437000001, 22.478297670000018, 59.92577, 2.522996, 10.721382770000014, 67.79389, 47.906800000000004, 57.18150000000001, 62.2155469, 73.6602, 99.43273, 69.05247000000001, 84.23316000000001, 64.58183400000001, 93.01830000000001], [9.027160000000006, 14.92919506999999, 67.7278, 0.0, 3.4210786999999976, 33.215790000000005, 11.3995, 24.68168359999999, 7.347014300000005, 9.988588000000002, 33.89789721, 75.0368462, 28.718373999999994, 35.349299999999985, 41.021479400000004, 25.926294370000004, 48.362197669999986, 12.196030000000006, 66.722896, 57.69298276999999, 3.676470000000004, 26.427000000000007, 10.7693, 14.919646900000007, 7.718400000000002, 34.184529999999995, 3.375130000000004, 18.56704, 8.012365999999993, 27.359700000000004], [11.985918700000003, 12.430673769999991, 66.97117870000001, 3.4210786999999976, 0.0, 30.734868700000007, 12.413578699999997, 24.183162299999992, 8.433335600000003, 9.216610700000004, 35.02337590999999, 74.53832489999999, 27.994652699999996, 34.48217869999999, 44.1591581, 27.06937307, 47.86367636999999, 11.53904870000001, 65.97637470000001, 56.91850407, 3.254008699999993, 25.999878700000007, 10.128378700000003, 12.55872560000001, 11.0844787, 37.051651299999996, 6.485348700000002, 19.666038699999994, 7.256712699999996, 30.4723787], [41.41435000000001, 18.448005070000015, 37.47169, 33.215790000000005, 30.734868700000007, 0.0, 40.58469, 8.942493600000017, 38.15182430000001, 23.518258000000003, 62.63070721, 43.82165619999999, 4.927184000000012, 7.163089999999982, 71.0042894, 54.00050437000001, 17.147007669999983, 24.92382, 35.71170600000001, 27.07779276999999, 30.80426, 12.644789999999997, 22.790490000000005, 24.743856899999994, 38.19619, 64.44586, 34.130320000000005, 47.24823, 29.59555600000001, 57.97489000000001], [2.431339999999994, 22.69669506999999, 76.98070000000001, 11.3995, 12.413578699999997, 40.58469, 0.0, 34.073183599999986, 4.082114299999994, 20.087688000000004, 23.443397209999993, 84.40634619999999, 37.87867399999999, 46.23639999999998, 32.40897940000001, 15.311594370000003, 57.73169766999999, 21.287470000000006, 75.844396, 66.79008277, 10.792030000000004, 35.594100000000005, 21.532799999999998, 22.286946900000007, 13.225499999999997, 25.29743, 8.574969999999997, 7.710139999999997, 16.66686599999999, 18.524600000000003], [32.88084359999999, 11.848511469999998, 43.52378360000002, 24.68168359999999, 24.183162299999992, 8.942493600000017, 34.073183599999986, 0.0, 31.60064389999999, 14.967751599999986, 55.73421360999998, 50.35523740000001, 4.435109600000004, 13.456783599999996, 63.026204199999995, 48.12441076999999, 23.85651407, 16.98771359999998, 42.20918760000002, 33.16929917, 24.861153599999984, 4.715083599999983, 14.25698359999999, 18.867836699999977, 30.31368359999999, 56.526353599999986, 26.136813599999993, 41.32872359999999, 21.676049599999995, 50.05538359999999], [3.712454300000001, 19.848155369999994, 74.39541430000001, 7.347014300000005, 8.433335600000003, 38.15182430000001, 4.082114299999994, 31.60064389999999, 0.0, 16.640026300000006, 26.82685750999999, 81.9558065, 35.41224029999999, 42.68151429999999, 35.9598397, 18.87005467, 55.281157969999995, 18.86818430000001, 73.39411830000002, 64.33597267, 8.336304300000009, 33.36241430000001, 17.746914300000004, 19.853407200000014, 11.103014300000002, 28.859709699999993, 6.157884300000001, 11.290574299999992, 14.683248299999995, 22.0977143], [17.918028000000007, 5.215263069999988, 57.75803200000001, 9.988588000000002, 9.216610700000004, 23.518258000000003, 20.087688000000004, 14.967751599999986, 16.640026300000006, 0.0, 42.55996521, 65.32291419999999, 18.77924199999999, 26.945487999999983, 49.694547400000005, 34.60476237, 38.64826566999999, 3.016557999999997, 56.76096400000001, 47.70439476999999, 10.884277999999998, 16.921988000000006, 1.7864879999999965, 5.430114900000007, 16.758588000000003, 42.588602, 12.159458000000006, 27.340972, 7.688822000000011, 36.125288000000005], [25.309057209999988, 44.422702139999984, 99.12399721, 33.89789721, 35.02337590999999, 62.63070721, 23.443397209999993, 55.73421360999998, 26.82685750999999, 42.55996521, 0.0, 105.21705100999999, 60.13272320999999, 68.31499720999997, 9.67041781000001, 12.056602839999991, 79.02170045999998, 44.133927209999996, 97.82540121, 88.75488555999999, 33.697367209999996, 58.361297210000004, 44.193197209999994, 44.15205031, 35.32989720999999, 3.9105672100000017, 31.547027209999992, 16.556937209999997, 39.89426320999999, 11.21559720999999], [83.23600619999999, 62.10774887, 7.584946199999985, 75.0368462, 74.53832489999999, 43.82165619999999, 84.40634619999999, 50.35523740000001, 81.9558065, 65.32291419999999, 105.21705100999999, 0.0, 46.5436722, 41.42994620000001, 110.1674332, 95.08364816999999, 26.674751470000004, 65.1168762, 8.700350199999985, 17.67193657, 73.63231619999999, 52.844246199999986, 64.6121462, 66.44300069999998, 77.1288462, 105.49951619999999, 75.95197619999999, 90.97188619999999, 69.8052122, 98.1845462], [36.692333999999995, 16.043621070000004, 39.23127400000001, 28.718373999999994, 27.994652699999996, 4.927184000000012, 37.87867399999999, 4.435109600000004, 35.41224029999999, 18.77924199999999, 60.13272320999999, 46.5436722, 0.0, 9.447473999999993, 67.21530539999999, 52.31352036999999, 19.869023669999997, 20.79320399999999, 38.05067800000002, 28.974608770000003, 28.666643999999987, 8.747773999999987, 18.172273999999994, 23.05687289999998, 34.502373999999996, 60.33184399999999, 29.942303999999996, 45.134213999999986, 25.48154, 53.869074], [44.21105999999999, 24.547695069999996, 35.613100000000024, 35.349299999999985, 34.48217869999999, 7.163089999999982, 46.23639999999998, 13.456783599999996, 42.68151429999999, 26.945487999999983, 68.31499720999997, 41.42994620000001, 9.447473999999993, 0.0, 75.2193794, 59.94759436999999, 15.581297670000003, 29.71532999999998, 34.581796000000026, 25.54408277000001, 37.51720999999998, 17.268299999999982, 25.178199999999986, 31.070946899999974, 41.07689999999999, 69.53382999999998, 38.64322999999999, 53.824539999999985, 34.05526599999999, 62.68359999999999], [32.4326394, 53.56371566999999, 106.37957940000001, 41.021479400000004, 44.1591581, 71.0042894, 32.40897940000001, 63.026204199999995, 35.9598397, 49.694547400000005, 9.67041781000001, 110.1674332, 67.21530539999999, 75.2193794, 0.0, 17.70021497, 84.02671826999999, 48.03610940000001, 104.1639834, 95.97750337, 41.11854940000001, 62.25707940000001, 51.3167794, 50.043632500000015, 38.9764794, 7.1221494000000085, 37.9946094, 24.83251940000001, 43.7858454, 15.107179400000001], [17.334454369999996, 36.65190069999999, 91.47219437000001, 25.926294370000004, 27.06937307, 54.00050437000001, 15.311594370000003, 48.12441076999999, 18.87005467, 34.60476237, 12.056602839999991, 95.08364816999999, 52.31352036999999, 59.94759436999999, 17.70021497, 0.0, 69.12490329999999, 32.52632437000001, 89.26219837000001, 81.07568839999999, 24.028764370000008, 46.747294370000006, 36.218794370000005, 32.52544747000001, 23.28469437, 13.727964369999995, 22.896624369999998, 7.734334370000006, 28.268460369999996, 5.10099437], [56.56135766999999, 35.4330026, 22.478297670000018, 48.362197669999986, 47.86367636999999, 17.147007669999983, 57.73169766999999, 23.85651407, 55.281157969999995, 38.64826566999999, 79.02170045999998, 26.674751470000004, 19.869023669999997, 15.581297670000003, 84.02671826999999, 69.12490329999999, 0.0, 38.46222766999998, 20.24170167000002, 11.957185300000006, 46.957667669999985, 26.189597669999984, 37.93749766999999, 39.86835076999998, 51.31419766999999, 78.82486766999999, 49.27732766999999, 64.29723766999999, 43.15056367, 71.52989767], [20.11713000000001, 7.611225069999984, 59.92577, 12.196030000000006, 11.53904870000001, 24.92382, 21.287470000000006, 16.98771359999998, 18.86818430000001, 3.016557999999997, 44.133927209999996, 65.1168762, 20.79320399999999, 29.71532999999998, 48.03610940000001, 32.52632437000001, 38.46222766999998, 0.0, 57.718926, 49.52295276999999, 10.53888, 14.49543, 4.665929999999994, 3.0196769000000026, 13.742030000000007, 42.660500000000006, 12.833100000000009, 27.853010000000005, 4.760336000000013, 33.10873000000001], [74.67405600000001, 54.04829907000002, 2.522996, 66.722896, 65.97637470000001, 35.71170600000001, 75.844396, 42.20918760000002, 73.39411830000002, 56.76096400000001, 97.82540121, 8.700350199999985, 38.05067800000002, 34.581796000000026, 104.1639834, 89.26219837000001, 20.24170167000002, 57.718926, 0.0, 9.156486770000015, 65.592366, 45.696296000000004, 56.17679600000001, 60.0055509, 71.45089600000001, 97.25756600000001, 67.390026, 82.409936, 62.40726200000002, 90.81759600000001], [65.62242277, 45.01778770000001, 10.721382770000014, 57.69298276999999, 56.91850407, 27.07779276999999, 66.79008277, 33.16929917, 64.33597267, 47.70439476999999, 88.75488555999999, 17.67193657, 28.974608770000003, 25.54408277000001, 95.97750337, 81.07568839999999, 11.957185300000006, 49.52295276999999, 9.156486770000015, 0.0, 57.38407276999999, 37.510382769999985, 47.14688276999999, 51.81913586999998, 63.264982769999996, 89.04368236999998, 58.66585277, 73.84654276999999, 54.19521677, 82.63168277], [11.68035000000001, 13.484865069999984, 67.79389, 3.676470000000004, 3.254008699999993, 30.80426, 10.792030000000004, 24.861153599999984, 8.336304300000009, 10.884277999999998, 33.697367209999996, 73.63231619999999, 28.666643999999987, 37.51720999999998, 41.11854940000001, 24.028764370000008, 46.957667669999985, 10.53888, 65.592366, 57.38407276999999, 0.0, 25.03431, 12.564809999999994, 11.538116900000004, 7.880910000000007, 34.21862, 4.325780000000007, 17.339570000000002, 6.358895999999989, 27.24761000000001], [34.460760000000015, 14.178595070000016, 47.906800000000004, 26.427000000000007, 25.999878700000007, 12.644789999999997, 35.594100000000005, 4.715083599999983, 33.36241430000001, 16.921988000000006, 58.361297210000004, 52.844246199999986, 8.747773999999987, 17.268299999999982, 62.25707940000001, 46.747294370000006, 26.189597669999984, 14.49543, 45.696296000000004, 37.510382769999985, 25.03431, 0.0, 15.901900000000007, 14.522646899999994, 25.754600000000007, 57.14153, 27.29293000000001, 42.30424000000001, 18.992966000000013, 47.47930000000001], [19.156860000000005, 4.50449506999999, 57.18150000000001, 10.7693, 10.128378700000003, 22.790490000000005, 21.532799999999998, 14.25698359999999, 17.746914300000004, 1.7864879999999965, 44.193197209999994, 64.6121462, 18.172273999999994, 25.178199999999986, 51.3167794, 36.218794370000005, 37.93749766999999, 4.665929999999994, 56.17679600000001, 47.14688276999999, 12.564809999999994, 15.901900000000007, 0.0, 6.838146899999989, 18.0633, 44.35563, 13.767030000000004, 28.950339999999997, 9.135666000000008, 37.7094], [23.115606900000014, 7.395348169999979, 62.2155469, 14.919646900000007, 12.55872560000001, 24.743856899999994, 22.286946900000007, 18.867836699999977, 19.853407200000014, 5.430114900000007, 44.15205031, 66.44300069999998, 23.05687289999998, 31.070946899999974, 50.043632500000015, 32.52544747000001, 39.86835076999998, 3.0196769000000026, 60.0055509, 51.81913586999998, 11.538116900000004, 14.522646899999994, 6.838146899999989, 0.0, 13.462046900000011, 45.632516900000006, 15.831976900000011, 28.846886900000005, 7.695812900000015, 35.99434690000001], [12.302160000000002, 20.84119506999999, 73.6602, 7.718400000000002, 11.0844787, 38.19619, 13.225499999999997, 30.31368359999999, 11.103014300000002, 16.758588000000003, 35.32989720999999, 77.1288462, 34.502373999999996, 41.07689999999999, 38.9764794, 23.28469437, 51.31419766999999, 13.742030000000007, 71.45089600000001, 63.264982769999996, 7.880910000000007, 25.754600000000007, 18.0633, 13.462046900000011, 0.0, 35.004929999999995, 4.956330000000001, 19.965639999999993, 9.166365999999995, 25.240700000000004], [25.32276999999999, 47.14986506999999, 99.43273, 34.184529999999995, 37.051651299999996, 64.44586, 25.29743, 56.526353599999986, 28.859709699999993, 42.588602, 3.9105672100000017, 105.49951619999999, 60.33184399999999, 69.53382999999998, 7.1221494000000085, 13.727964369999995, 78.82486766999999, 42.660500000000006, 97.25756600000001, 89.04368236999998, 34.21862, 57.14153, 44.35563, 45.632516900000006, 35.004929999999995, 0.0, 30.890599999999992, 17.71089, 38.38656399999999, 9.764229999999994], [7.462030000000002, 16.760325069999993, 69.05247000000001, 3.375130000000004, 6.485348700000002, 34.130320000000005, 8.574969999999997, 26.136813599999993, 6.157884300000001, 12.159458000000006, 31.547027209999992, 75.95197619999999, 29.942303999999996, 38.64322999999999, 37.9946094, 22.896624369999998, 49.27732766999999, 12.833100000000009, 67.390026, 58.66585277, 4.325780000000007, 27.29293000000001, 13.767030000000004, 15.831976900000011, 4.956330000000001, 30.890599999999992, 0.0, 15.191909999999993, 8.611835999999997, 24.08763], [9.793479999999992, 29.952235069999986, 84.23316000000001, 18.56704, 19.666038699999994, 47.24823, 7.710139999999997, 41.32872359999999, 11.290574299999992, 27.340972, 16.556937209999997, 90.97188619999999, 45.134213999999986, 53.824539999999985, 24.83251940000001, 7.734334370000006, 64.29723766999999, 27.853010000000005, 82.409936, 73.84654276999999, 17.339570000000002, 42.30424000000001, 28.950339999999997, 28.846886900000005, 19.965639999999993, 17.71089, 15.191909999999993, 0.0, 23.61327399999999, 10.925340000000006], [15.774206, 12.299561069999998, 64.58183400000001, 8.012365999999993, 7.256712699999996, 29.59555600000001, 16.66686599999999, 21.676049599999995, 14.683248299999995, 7.688822000000011, 39.89426320999999, 69.8052122, 25.48154, 34.05526599999999, 43.7858454, 28.268460369999996, 43.15056367, 4.760336000000013, 62.40726200000002, 54.19521677, 6.358895999999989, 18.992966000000013, 9.135666000000008, 7.695812900000015, 9.166365999999995, 38.38656399999999, 8.611835999999997, 23.61327399999999, 0.0, 28.851465999999995], [18.605459999999997, 40.678895069999996, 93.01830000000001, 27.359700000000004, 30.4723787, 57.97489000000001, 18.524600000000003, 50.05538359999999, 22.0977143, 36.125288000000005, 11.21559720999999, 98.1845462, 53.869074, 62.68359999999999, 15.107179400000001, 5.10099437, 71.52989767, 33.10873000000001, 90.81759600000001, 82.63168277, 27.24761000000001, 47.47930000000001, 37.7094, 35.99434690000001, 25.240700000000004, 9.764229999999994, 24.08763, 10.925340000000006, 28.851465999999995, 0.0]]

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

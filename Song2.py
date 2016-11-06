from spotipy.oauth2 import SpotifyClientCredentials
import spotipy as sp
import random
import numpy as np

class Song2:
    """ A song in Spot represents the current state of the HMM """

    def __init__(self, songID):
        client_credentials_manager = SpotifyClientCredentials(client_id='96eecfa895234e1b8a2bda924f0c2db5', client_secret='150e251fa585478dbb549abeb5c0f73a')
        ## client credentials of our app are needed to access song featuers

        spotify = sp.Spotify(client_credentials_manager=client_credentials_manager)
        ## sets up the app

        sp.trace=False
        ## don't want to read everything about every song we look at
        self._get_id = songID
        self.songID = songID
        self.features = spotify.audio_features([songID]).pop()
        self.track = spotify.track(songID)['artists'].pop()
        ##self.artists = self.track['artists'].pop()
        
        

    def getFeature(self, feat):
        return (self.features[feat])

    def getArtist(self):
        return (self.track['id'])

    def getRelatedArtist(self): # returns a list of 20 artist ids.
        relatedArtists = sp.Spotify.artist_related_artists(sp.Spotify(), self.getArtist())
        #print(relatedArtists)
        id_list = []
        ids = relatedArtists['artists']
        for i in range(0,len(ids),8):
            var = ids[i]['id']
            id_list.append(var)
        return(id_list)

    def getTopTracks(self):  # returns 10 track objects per artist.
        song_pool = []
        related_artists = self.getRelatedArtist()
        for i in range(len(related_artists)):
            var = sp.Spotify.artist_top_tracks(sp.Spotify(), related_artists[i])
            for i in range(len(var['tracks'])):
                song_pool.append((var['tracks'][i]['id'],0))
        print(len(song_pool))
        return song_pool

    def compare(self, song_pool):  #
        prob_matrix = []
        keywords = ['danceability', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'tempo']
        #val = random.randrange(0, len(song_pool))
        for i in range(len(song_pool)):  # get 1 song
            starting_song = Song2("spotify:track:" + song_pool[i][0])
            # song1_audio_feats = sp.Spotify.audio_features(sp.Spotify(), starting_song)
            #del(song_pool[i])
            difference_values = []
            for i in range(len(song_pool)): #compare it to all other songs
                #print(i)
                # features for each song
                current_song = Song2("spotify:track:" + song_pool[i][0])
                #song2_audio_feats = sp.Spotify.audio_features(sp.Spotify(), [song_pool[i]])
                difference_value = 0
                for j in range(len(keywords)):
                     difference_value += abs(starting_song.getFeature(keywords[j]) - current_song.getFeature(keywords[j]))
                difference_values.append(difference_value)
            prob_matrix.append(difference_values)
            #index = np.argmin(difference_values)
            #new_song_id = song_pool[index]
        return prob_matrix

    def next_song(self, song_pool):
        matrix = [
             [0.0, 96.53915178, 100.443745, 7.002878780000009, 69.58687082, 87.56357358000001, 4.890651780000002, 38.87956178000001, 78.13324178000002, 92.26725178000002, 59.39251178, 25.411995220000005, 47.59899822, 23.233090440000005, 75.68261432000001, 11.499452570000003, 44.85315222000001, 17.557588220000007, 94.44052152, 9.68814822, 87.89124822, 77.85251122, 17.130420220000012, 91.55782653000003, 86.38634822000002, 62.937121720000015, 94.30574822, 65.47981822, 65.78482272000001, 91.53442832],
             [96.53915178, 0.0, 4.094896780000017, 92.46702699999999, 28.739022600000002, 12.064721799999983, 94.7183, 59.600709999999985, 20.830389999999976, 8.335899999999974, 40.08866, 71.49214699999999, 56.03615, 79.21606134, 22.52076609999999, 87.60720434999999, 58.33730399999998, 79.79973999999999, 5.4206732999999865, 93.95769999999999, 10.825499999999998, 22.436662999999996, 82.64357199999998, 7.938578309999975, 10.561599999999977, 35.73327349999998, 2.374899999999998, 37.358129999999996, 34.11497449999998, 6.082380099999988],
             [100.443745, 4.094896780000017, 0.0, 94.79634378, 31.034325820000017, 14.14383858, 96.97119678000001, 61.76982678, 23.056306779999996, 10.478996779999992, 44.092236780000015, 75.46545022000001, 58.12013322000002, 81.46683544000001, 26.37806932000001, 91.37490757, 60.597107220000005, 83.22504322, 9.283976520000005, 96.18960322000001, 13.086983220000016, 25.147966220000015, 85.33267522, 11.735284469999993, 14.358083219999994, 39.602576719999995, 6.162003220000015, 39.59635322000001, 37.98427772, 9.839883320000006],
             [7.002878780000009, 92.46702699999999, 94.79634378, 0.0, 63.762121599999986, 80.86169480000001, 2.389527000000008, 33.055683, 71.75663700000001, 85.38212700000001, 55.93636699999999, 21.929759999999998, 40.72647699999999, 16.345568339999996, 72.1697391, 8.102177349999995, 37.853251, 13.022712999999996, 90.92764629999999, 2.8245669999999916, 82.16312699999999, 72.603636, 12.008545000000003, 88.13155131, 82.38222700000001, 59.496246500000005, 90.35814699999999, 58.738696999999995, 62.3639475, 88.07935309999999],
             [69.58687082, 28.739022600000002, 31.034325820000017, 63.762121599999986, 0.0, 18.04381640000002, 66.0095226, 30.905804599999982, 8.616632600000024, 22.738122600000025, 13.168362599999998, 44.60963839999999, 27.3443554, 50.48556125999999, 8.467743500000012, 60.69428224999999, 29.679129399999983, 52.48871739999999, 27.225650700000013, 65.22044539999999, 18.4610054, 8.901640400000005, 54.584549399999986, 24.369662290000026, 18.62010540000002, 8.820293099999978, 26.596025400000002, 8.634575399999994, 7.201951899999983, 24.317357500000014],
             [87.56357358000001, 12.064721799999983, 14.14383858, 80.86169480000001, 18.04381640000002, 0.0, 83.03862180000002, 48.7122118, 9.445731799999994, 4.942821800000008, 31.212061800000015, 62.583454800000005, 44.187571800000015, 67.53466314, 13.294644300000007, 78.33153415000001, 46.664945800000005, 70.2497618, 10.410551499999995, 82.25686180000001, 1.4928217999999847, 12.094858800000013, 72.4489898, 7.314154110000008, 1.6039218000000044, 26.719523299999995, 9.739241799999984, 25.663791800000013, 25.1008527, 7.222458299999994],
             [4.890651780000002, 94.7183, 96.97119678000001, 2.389527000000008, 66.0095226, 83.03862180000002, 0.0, 35.20441000000001, 73.91489000000001, 87.63140000000001, 58.18716, 24.206647000000004, 42.95504999999999, 18.615961340000002, 74.47726610000001, 10.294104350000001, 40.23980400000001, 15.330240000000003, 93.2351733, 5.0748, 84.4404, 74.911163, 14.17447200000001, 90.35247831000002, 84.55350000000001, 61.73177350000002, 92.5144, 60.79283, 64.5794745, 90.2610801],
             [38.87956178000001, 59.600709999999985, 61.76982678, 33.055683, 30.905804599999982, 48.7122118, 35.20441000000001, 0.0, 39.334320000000005, 53.42481000000001, 23.230049999999984, 13.899443000000005, 8.724559999999983, 19.72865134000001, 39.27285609999999, 29.89769435000001, 6.008933999999998, 21.747830000000008, 58.0307633, 34.45085000000001, 49.266809999999985, 39.70684699999999, 23.762062, 55.148142310000004, 49.37991, 26.527511500000003, 57.312829999999984, 26.952579999999987, 29.375064499999997, 55.05667009999999],
             [78.13324178000002, 20.830389999999976, 23.056306779999996, 71.75663700000001, 8.616632600000024, 9.445731799999994, 73.91489000000001, 39.334320000000005, 0.0, 14.154490000000001, 21.782270000000022, 53.189757000000014, 35.213840000000026, 58.42633134000001, 4.222376100000012, 69.21921435000002, 37.63491400000001, 61.069350000000014, 19.32028329999999, 73.14991000000002, 10.55248999999998, 2.9922730000000195, 63.08358200000001, 16.437588310000002, 10.665589999999998, 17.388883500000002, 18.602509999999977, 16.554260000000017, 15.750584500000006, 16.34619009999999],
             [92.26725178000002, 8.335899999999974, 10.478996779999992, 85.38212700000001, 22.738122600000025, 4.942821800000008, 87.63140000000001, 53.42481000000001, 14.154490000000001, 0.0, 35.90376000000002, 67.27724700000002, 47.700250000000025, 71.03656134000002, 18.211866100000016, 83.21130435000002, 50.142404000000006, 75.05884000000002, 6.725773299999987, 85.74580000000002, 4.896000000000023, 16.981763000000022, 77.16167200000001, 3.84307831, 6.167100000000001, 31.414373500000004, 6.052999999999978, 29.14623000000002, 29.796074500000007, 3.7644800999999872],
             [59.39251178, 40.08866, 44.092236780000015, 55.93636699999999, 13.168362599999998, 31.212061800000015, 58.18716, 23.230049999999984, 21.782270000000022, 35.90376000000002, 0.0, 34.203486999999996, 19.666110000000003, 42.793201339999996, 17.982106100000006, 50.39054435, 21.940883999999986, 43.37507999999999, 36.82401330000001, 57.43904, 31.38676, 21.346003, 46.272911999999984, 32.609918310000026, 30.01586000000002, 4.492613500000019, 37.95424, 9.206330000000003, 8.138314500000014, 35.18172010000001],
             [25.411995220000005, 71.49214699999999, 75.46545022000001, 21.929759999999998, 44.60963839999999, 62.583454800000005, 24.206647000000004, 13.899443000000005, 53.189757000000014, 67.27724700000002, 34.203486999999996, 0.0, 22.614716999999988, 8.682685660000002, 50.2749391, 16.193920650000003, 19.776843000000003, 9.231693, 69.0350143, 23.413847000000004, 62.81136699999999, 52.76851599999999, 12.071464999999993, 66.20930069000002, 61.38246700000001, 37.573931500000015, 69.32224699999999, 40.786936999999995, 40.434827500000004, 66.5462331],
             [47.59899822, 56.03615, 58.12013322000002, 40.72647699999999, 27.3443554, 44.187571800000015, 42.95504999999999, 8.724559999999983, 35.213840000000026, 47.700250000000025, 19.666110000000003, 22.614716999999988, 0.0, 24.38608865999999, 35.62365610000001, 36.53503764999999, 3.0032259999999833, 30.380409999999987, 52.38573130000001, 38.593909999999994, 45.562650000000005, 34.001313, 30.472581999999985, 51.501417690000025, 45.628550000000025, 22.934648500000023, 53.68833, 20.314020000000006, 23.775424500000018, 50.910030100000014],
             [23.233090440000005, 79.21606134, 81.46683544000001, 16.345568339999996, 50.48556125999999, 67.53466314, 18.615961340000002, 19.72865134000001, 58.42633134000001, 71.03656134000002, 42.793201339999996, 8.682685660000002, 24.38608865999999, 0.0, 58.95330476, 12.359143010000002, 21.623842660000008, 6.204278659999998, 75.71121196, 14.741638660000003, 68.93815866, 57.387201659999995, 6.249510659999992, 74.82851697000001, 69.05125866000002, 46.20781216000002, 77.02883865999999, 44.469128659999996, 47.05551316000001, 74.75231876000001],
             [75.68261432000001, 22.52076609999999, 26.37806932000001, 72.1697391, 8.467743500000012, 13.294644300000007, 74.47726610000001, 39.27285609999999, 4.222376100000012, 18.211866100000016, 17.982106100000006, 50.2749391, 35.62365610000001, 58.95330476, 0.0, 66.18316175000001, 37.9714621, 59.1712461, 19.100092800000002, 73.6857461, 13.460306099999992, 3.394343099999993, 62.30507409999999, 16.054787790000013, 12.149406100000013, 13.58949259999999, 20.271326099999992, 17.099876100000007, 11.988231599999994, 17.261626],
             [11.499452570000003, 87.60720434999999, 91.37490757, 8.102177349999995, 60.69428224999999, 78.33153415000001, 10.294104350000001, 29.89769435000001, 69.21921435000002, 83.21130435000002, 50.39054435, 16.193920650000003, 36.53503764999999, 12.359143010000002, 66.18316175000001, 0.0, 33.84941165000001, 8.382227650000004, 83.10706895, 7.505127650000001, 78.66528765, 66.60932464999999, 6.140455650000009, 82.05862604000002, 77.15838765000001, 53.65598915000002, 85.27070764999999, 56.823257649999995, 54.52337015000001, 82.30117575],
             [44.85315222000001, 58.33730399999998, 60.597107220000005, 37.853251, 29.679129399999983, 46.664945800000005, 40.23980400000001, 6.008933999999998, 37.63491400000001, 50.142404000000006, 21.940883999999986, 19.776843000000003, 3.0032259999999833, 21.623842660000008, 37.9714621, 33.84941165000001, 0.0, 27.582436000000005, 54.7305053, 35.71639600000001, 47.96187599999999, 36.40535899999999, 27.744267999999998, 53.93479169000001, 48.18097600000001, 25.299422500000006, 56.157595999999984, 23.089445999999988, 26.1676705, 53.881076099999994],
             [17.557588220000007, 79.79973999999999, 83.22504322, 13.022712999999996, 52.48871739999999, 70.2497618, 15.330240000000003, 21.747830000000008, 61.069350000000014, 75.05884000000002, 43.37507999999999, 9.231693, 30.380409999999987, 6.204278659999998, 59.1712461, 8.382227650000004, 27.582436000000005, 0.0, 78.0793213, 14.537440000000005, 70.33905999999999, 60.29509699999999, 3.155831999999993, 75.22576169000001, 69.47216000000002, 46.74046650000001, 77.57408, 48.66862999999999, 49.62323450000001, 75.1686401],
             [94.44052152, 5.4206732999999865, 9.283976520000005, 90.92764629999999, 27.225650700000013, 10.410551499999995, 93.2351733, 58.0307633, 19.32028329999999, 6.725773299999987, 36.82401330000001, 69.0350143, 52.38573130000001, 75.71121196, 19.100092800000002, 83.10706895, 54.7305053, 78.0793213, 0.0, 90.4458213, 9.142381300000011, 18.716418300000008, 79.0651493, 4.584694989999988, 8.941481299999989, 32.431399799999994, 3.1734012999999894, 35.859951300000006, 28.832306799999998, 3.9057068000000004],
             [9.68814822, 93.95769999999999, 96.18960322000001, 2.8245669999999916, 65.22044539999999, 82.25686180000001, 5.0748, 34.45085000000001, 73.14991000000002, 85.74580000000002, 57.43904, 23.413847000000004, 38.593909999999994, 14.741638660000003, 73.6857461, 7.505127650000001, 35.71639600000001, 14.537440000000005, 90.4458213, 0.0, 83.67596, 72.118363, 11.399872000000013, 89.56350769000002, 83.78906000000002, 60.94273850000002, 91.74758, 57.940129999999996, 61.78667450000001, 89.47068010000001],
             [87.89124822, 10.825499999999998, 13.086983220000016, 82.16312699999999, 18.4610054, 1.4928217999999847, 84.4404, 49.266809999999985, 10.55248999999998, 4.896000000000023, 31.38676, 62.81136699999999, 45.562650000000005, 68.93815866, 13.460306099999992, 78.66528765, 47.96187599999999, 70.33905999999999, 9.142381300000011, 83.67596, 0.0, 12.095162999999998, 72.78083199999999, 6.232667690000023, 1.5540999999999787, 26.997298499999978, 8.63398, 27.026629999999997, 25.372074499999986, 6.12688010000001],
             [77.85251122, 22.436662999999996, 25.147966220000015, 72.603636, 8.901640400000005, 12.094858800000013, 74.911163, 39.70684699999999, 2.9922730000000195, 16.981763000000022, 21.346003, 52.76851599999999, 34.001313, 57.387201659999995, 3.394343099999993, 66.60932464999999, 36.40535899999999, 60.29509699999999, 18.716418300000008, 72.118363, 12.095162999999998, 0.0, 60.736868999999984, 17.78470469000002, 11.997063000000017, 16.953389499999982, 20.210762999999996, 17.477533, 13.328111499999988, 17.673717100000008],
             [17.130420220000012, 82.64357199999998, 85.33267522, 12.008545000000003, 54.584549399999986, 72.4489898, 14.17447200000001, 23.762062, 63.08358200000001, 77.16167200000001, 46.272911999999984, 12.071464999999993, 30.472581999999985, 6.249510659999992, 62.30507409999999, 6.140455650000009, 27.744267999999998, 3.155831999999993, 79.0651493, 11.399872000000013, 72.78083199999999, 60.736868999999984, 0.0, 78.18299369, 72.409932, 49.562298500000004, 80.35025199999998, 50.69260199999999, 50.4050025, 78.08660809999999],
             [91.55782653000003, 7.938578309999975, 11.735284469999993, 88.13155131, 24.369662290000026, 7.314154110000008, 90.35247831000002, 55.148142310000004, 16.437588310000002, 3.84307831, 32.609918310000026, 66.20930069000002, 51.501417690000025, 74.82851697000001, 16.054787790000013, 82.05862604000002, 53.93479169000001, 75.22576169000001, 4.584694989999988, 89.56350769000002, 6.232667690000023, 17.78470469000002, 78.18299369, 0.0, 5.903167690000003, 28.635369190000002, 5.631087689999977, 32.977637690000016, 27.800396190000008, 2.5818017899999868],
             [86.38634822000002, 10.561599999999977, 14.358083219999994, 82.38222700000001, 18.62010540000002, 1.6039218000000044, 84.55350000000001, 49.37991, 10.665589999999998, 6.167100000000001, 30.01586000000002, 61.38246700000001, 45.628550000000025, 69.05125866000002, 12.149406100000013, 77.15838765000001, 48.18097600000001, 69.47216000000002, 8.941481299999989, 83.78906000000002, 1.5540999999999787, 11.997063000000017, 72.409932, 5.903167690000003, 0.0, 25.526398500000003, 8.28707999999998, 27.092530000000018, 23.881174500000007, 5.73078009999999],
             [62.937121720000015, 35.73327349999998, 39.602576719999995, 59.496246500000005, 8.820293099999978, 26.719523299999995, 61.73177350000002, 26.527511500000003, 17.388883500000002, 31.414373500000004, 4.492613500000019, 37.573931500000015, 22.934648500000023, 46.20781216000002, 13.58949259999999, 53.65598915000002, 25.299422500000006, 46.74046650000001, 32.431399799999994, 60.94273850000002, 26.997298499999978, 16.953389499999982, 49.562298500000004, 28.635369190000002, 25.526398500000003, 0.0, 33.46431849999998, 4.992868499999983, 3.665700999999995, 30.68910659999999],
             [94.30574822, 2.374899999999998, 6.162003220000015, 90.35814699999999, 26.596025400000002, 9.739241799999984, 92.5144, 57.312829999999984, 18.602509999999977, 6.052999999999978, 37.95424, 69.32224699999999, 53.68833, 77.02883865999999, 20.271326099999992, 85.27070764999999, 56.157595999999984, 77.57408, 3.1734012999999894, 91.74758, 8.63398, 20.210762999999996, 80.35025199999998, 5.631087689999977, 8.28707999999998, 33.46431849999998, 0.0, 35.15175, 31.841074499999987, 3.7306800999999905],
             [65.47981822, 37.358129999999996, 39.59635322000001, 58.738696999999995, 8.634575399999994, 25.663791800000013, 60.79283, 26.952579999999987, 16.554260000000017, 29.14623000000002, 9.206330000000003, 40.786936999999995, 20.314020000000006, 44.469128659999996, 17.099876100000007, 56.823257649999995, 23.089445999999988, 48.66862999999999, 35.859951300000006, 57.940129999999996, 27.026629999999997, 17.477533, 50.69260199999999, 32.977637690000016, 27.092530000000018, 4.992868499999983, 35.15175, 0.0, 7.177644500000011, 32.200250100000005],
             [65.78482272000001, 34.11497449999998, 37.98427772, 62.3639475, 7.201951899999983, 25.1008527, 64.5794745, 29.375064499999997, 15.750584500000006, 29.796074500000007, 8.138314500000014, 40.434827500000004, 23.775424500000018, 47.05551316000001, 11.988231599999994, 54.52337015000001, 26.1676705, 49.62323450000001, 28.832306799999998, 61.78667450000001, 25.372074499999986, 13.328111499999988, 50.4050025, 27.800396190000008, 23.881174500000007, 3.665700999999995, 31.841074499999987, 7.177644500000011, 0.0, 29.043405599999996],
             [91.53442832, 6.082380099999988, 9.839883320000006, 88.07935309999999, 24.317357500000014, 7.222458299999994, 90.2610801, 55.05667009999999, 16.34619009999999, 3.7644800999999872, 35.18172010000001, 66.5462331, 50.910030100000014, 74.75231876000001, 17.261626, 82.30117575, 53.881076099999994, 75.1686401, 3.9057068000000004, 89.47068010000001, 6.12688010000001, 17.673717100000008, 78.08660809999999, 2.5818017899999868, 5.73078009999999, 30.68910659999999, 3.7306800999999905, 32.200250100000005, 29.043405599999996, 0.0]]
        row = 0
        min = 1000
        count = 0
        while count < 10:
            for i in range(len(matrix[row])):
                if matrix[row][i] < min and matrix[row][i] > 0:
                    if song_pool[i][1] != 1:
                        min = matrix[row][i]
                        index = matrix[row].index(min)
                    else:
                        min = 1000
                        continue
            print(song_pool[index][0])
            song_pool[index] = (song_pool[index][0], 1)
            row = index
            min = 1000
            count += 1

    def fisher_yates(self,song_pool):
        i = len(song_pool) - 1
        while i > 0:
            s = random.randint(0, i)
            song_pool[s], song_pool[i] = song_pool[i], song_pool[s]
            i -= 1
        for i in range(10):
            print(song_pool[i][0])















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
        for i in range(len(ids)):
            var = ids[i]['id']
            id_list.append(var)
        return(id_list)

    def getTopTracks(self):  # returns 10 track objects.
        song_pool = []
        related_artists = self.getRelatedArtist()
        for i in range(len(related_artists)):
            var = sp.Spotify.artist_top_tracks(sp.Spotify(), related_artists[i])
            for i in range(len(var['tracks'])):
                song_pool.append(var['tracks'][i]['id'])
        print(len(song_pool))
        return(song_pool)

    def compare(self, song_pool):
        keywords = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
                    'liveness', 'valence', 'tempo']
        val = random.randrange(0, len(song_pool))
        starting_song = Song2("spotify:track:" + song_pool[val])
        # song1_audio_feats = sp.Spotify.audio_features(sp.Spotify(), starting_song)
        del(song_pool[val])
        difference_values = []
        difference_value = 0
        for i in range(len(song_pool)):
            # features for each song
            current_song = Song2("spotify:track:" + song_pool[i])
            # song2_audio_feats = sp.Spotify.audio_features(sp.Spotify(), [song_pool[i]])
            for j in range(len(keywords)):
                difference_value += abs(starting_song.getFeature(keywords[j]) - current_song.getFeature(keywords[j]))
            difference_values.append(difference_value)
        index = np.argmin(difference_values)
        new_song_id = song_pool[index]
        return(new_song_id)









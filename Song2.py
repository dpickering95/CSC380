from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

class Song2:
    """ A song in Spot represents the current state of the HMM """

    def __init__(self, songID):
        client_credentials_manager = SpotifyClientCredentials(client_id='96eecfa895234e1b8a2bda924f0c2db5', client_secret='150e251fa585478dbb549abeb5c0f73a')
        ## client credentials of our app are needed to access song featuers

        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        ## sets up the app

        sp.trace=False
        ## don't want to read everything about every song we look at
        self.songID = songID
        self.features = sp.audio_features([songID]).pop()

    def getFeature(self, feat):
        return (self.features[feat])
                        
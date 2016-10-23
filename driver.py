from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from CSC380 import Song2



test = Song2.Song2('spotify:track:31n9wiTDFnCE3WJNcSRqL9')
## creates a song, which is really just a dictionary of features

#print(test.getFeature('liveness'))
#print(test.getArtist())
#print(test.getRelatedArtist())
print(test.getTopTracks())
## print whichever feature we want
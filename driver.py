import spotipy.oauth2
import spotipy
import Song2

# https://play.spotify.com/track/2ltgTiMvFZhU44RAscXLoD     Brand New - Jude Law and a Semester Abroad
# https://play.spotify.com/track/4iUFYqWo9l1BpOZAHsR7zf     ADTR - Bad Vibrations

# test = Song2.Song2('spotify:track:31n9wiTDFnCE3WJNcSRqL9')        //devante's list
test = Song2.Song2('spotify:track:4iUFYqWo9l1BpOZAHsR7zf')
## creates a song, which is really just a dictionary of features

#print(test.getFeature('liveness'))
#print(test.getArtist())
#print(test.getRelatedArtist())
# print(test.getTopTracks())
songPool = test.getTopTracks()
nextSong = test.next_song(songPool)
probMatrix = test.compare(songPool)
for i in range(len(probMatrix)):
    print(probMatrix[i])



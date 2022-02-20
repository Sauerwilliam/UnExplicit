from posixpath import split
from re import search
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
user = 'o5yyopuyrqd5dbj0z8srzmwa7'
inputPlaylist = '5vnbt1XSa214HOuMA0UuBO'
outputPlaylist = '137xYoo2RGNQZ4BfJFTXGL'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="1bb0235e73db457cb38eb43acaccaf47",
                                               client_secret="f47e1dfbaffc4deba80cb634624220a0",
                                               redirect_uri="http://google.com",
                                               scope="playlist-modify-public playlist-read-private playlist-modify-private user-follow-read user-library-read"))

songs = sp.user_playlist_tracks(user,inputPlaylist,'items.track.name')
songsList = json.dumps(songs)
songsList = songsList.replace('{','')
songsList = songsList.replace('}','')
songsList = songsList.replace(']','')
songsList = songsList.replace('"','')
songsList = songsList.replace('items: [','')
songsList = songsList.replace('track: name: ','')
songsAsList = songsList.split(',')

i=0
searchList = []
while i < len(songsAsList):
    searchList.append(sp.search(songsAsList[i],1))
    i+=1
x=0
def get_ID(idString):
    spilting = json.dumps(idString)
    spliting = spilting.split(' "type": "track", "uri": "')
    spliting.pop(0)
    spliting = spliting[0].split('}]')
    spliting.pop(1)
    return([spliting[0][0:(len(spliting[0])-1)]])
    
    
#playlist = sp.user_playlist_create(user,'clean')
songs = []
while x < len(searchList):
    if '"explicit": true' in json.dumps(searchList[x]):
        if '"explicit": true' in json.dumps(sp.search(songsAsList[x],1,1)):
            print("no song found :/")
        else:
            print("Finally got a match")
            songs.append(get_ID(sp.search(songsAsList[x],1,1)))
    if '"explicit": false' in json.dumps(searchList[x]):
        print("got a match")
        songs.append(get_ID(searchList[x]))
        #print(get_ID(searchList[x]))
        #sp.playlist_add_items(outputPlaylist,[get_ID(searchList[x])])
    x+=1
#print(searchList)
#print(songs)
y=0
while y < len(songs):
    sp.user_playlist_add_tracks(user,outputPlaylist,songs[y])
    y+=1

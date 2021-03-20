from utils import *
from spotify import *

def Main():

    Utils.newLine()
    print("Hello, Welcome to Spotify Song recommender")
    print("Select a Menu")
    print("")
    print("1. Get top tracks of an artist")
    print("2. Song Recommendation")
    print("3. Search a song by lyric")
    print("4. Exit")
    answer = input(": ")
    while answer not in ["1", "2", "3", "4"]:
        print("Wrong Option")
        answer = input(": ")

    if answer == '1':
        Utils.newLine()
        print("You selected 'Get top 5 tracks of an artist'")
        artist = input("Enter artist name (Full Name): ")
        country = input("Select country from KR US CA: ")
        print("")
        Utils.newLine()
        print("Top 5 tracks of {} at Spotify".format(artist))
        print("")
        optionOne = OptionOne(artist, country)
        optionOne.getArtistTopTracks(artist, country)

    if answer == '4':
        print('Bye bye')
        Utils.newLine()
        sys.exit(1)




Main()
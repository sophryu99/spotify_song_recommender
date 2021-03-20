from spotify import *
from config import *

client_id = Config.client_id
client_secret = Config.client_secret

class Utils:
    """ For functionalities """

    @staticmethod
    def newLine():
        print("")
        print("########################################")
        print("########################################")

    # @staticmethod
    # def getTopTracks(name, country):
    #     Spotify.getArtistTopTracks(name, country)

class OptionOne(Utils):
    def __init__ (self, artist, country):
        self.artist = artist
        self.country = country

    def get_headers(self, client_id, client_secret):
        """Authorization for Spotify API request"""

        endpoint = "https://accounts.spotify.com/api/token"
        encoded = base64.b64encode("{}:{}".format(client_id, client_secret).encode('utf-8')).decode('ascii')

        headers = {
            "Authorization": "Basic {}".format(encoded)
        }

        payload = {
            "grant_type": "client_credentials"
        }

        r = requests.post(endpoint, data=payload, headers=headers)

        access_token = json.loads(r.text)['access_token']

        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }

        return headers

    def getArtistId(self, artist):
        """ Get ArtistId by name"""

        url = "https://api.spotify.com/v1/search?q=artist:{}&type=artist".format(artist)
        headers = self.get_headers(client_id, client_secret)

        r = requests.get(url, headers=headers)
        raw = json.loads(r.text)
        items = raw['artists']['items']
        artistId = items[0]['id']
        return artistId

    def getArtistTopTracks(self, artist, country):
        """ Get Artist's top 5 tracks """

        artistId = self.getArtistId(artist)
        url = "https://api.spotify.com/v1/artists/{}/top-tracks?country={}".format(artistId, country)
        headers = self.get_headers(client_id, client_secret)
        r = requests.get(url, headers=headers)
        raw = json.loads(r.text)
        total = raw['tracks'][:5]
        for i in total: 
            print("Song title:", i['name'])
            print("Listen at:", i['album']['external_urls']['spotify'])
            print("")


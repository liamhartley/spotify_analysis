import urllib.request


query = "/albums"
full_url = base_url + query

class QuerySpotify:

    def __init__(self):
        self.base_url = "https://api.spotify.com/v1"
        self.client_id = "ecccc29810b646f8a2dfc31e33dd4d4c"
        self.secret_key = "25437758fd9344c099d1d29e00e3cd0b"

    def api_call(self, query, params):
        url = self.base_url + query + params
        headers = {}



query = QuerySpotify()

response = query.api_call(query='/albums', params='')

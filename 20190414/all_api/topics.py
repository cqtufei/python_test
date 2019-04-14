import requests

class Topics(object):
    base_url = "http://39.107.96.138:3000/api/v1"
    def __init__(self,url):
        self.url = self.base_url+url
    
    def get_index_topics(self):
        r = requests.get(self.url)

        return r
        
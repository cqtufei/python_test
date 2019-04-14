import requests
import json


base_url = "http://39.107.96.138:3000/api/v1"
def get_index_topics():
    index_page_url=base_url+"/topics"
    r = requests.get(index_page_url)
    return r

def test_index_page():
    res = get_index_topics()
    r = res.json()
    assert len(r['data']) == 20
    assert res.status_code == 200

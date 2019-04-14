from all_api.topics import Topics

def test_index_page():
    url = "/topics"
    topics = Topics(url)
    print("----url----",topics.url)
    res = topics.get_index_topics()
    r = res.json()
    assert len(r['data']) == 20
    assert res.status_code == 200
    
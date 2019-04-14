import json
with open('data_Json.json','r',encoding='utf8') as f:
    d = json.load(f)
    print(d)
    f.close()
    
import requests
import json

url = "http://39.107.96.138:3000/"
cookies = {
    'node_club':"",
    "connect.sid":"",
}
r=request.get

r = requests.get(url)

print(type(r.cookies))

url = 'https://www.baidu.com/'

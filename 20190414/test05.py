import json
import requests

url = 'http://39.107.96.138:3000/api/v1/topics'

request_data = {
    "accesstoken":"3333a0fb-6dd8-439e-813b-2c3a5213a154",
    "title":"abcssssssss",
    "tab":"ask",
    "content":"xxxxxxxxxxxxxxxxx"
}
# 新建主题
r = requests.post(url,data=request_data)
print(r.text,type(r.text))

res = json.loads(r.text)
print(res["topic_id"])

# TODO 编辑主题
import json
import requests

base_url = "http://39.107.96.138:3000/api/v1"
url = base_url+'/topics'

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
update_data = {
    "accesstoken":"3333a0fb-6dd8-439e-813b-2c3a5213a154",
    "topic_id":res["topic_id"],
    "title":"abcsssssssstufei",
    "tab":"ask",
    "content":"xxxxxxxxxxxxxxxxxtufei"
}
update_url = base_url+"/topics/update"

r = requests.post(url,data=request_data)
print(r.text,type(r.text))

res = json.loads(r.text)
print(res["topic_id"])
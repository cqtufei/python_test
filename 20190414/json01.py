import json

data = {
    'username':'wangfei',
    'age':25,
    'is_man':False
}
with open('data_Json.json','w') as f:
    json.dump(data,f)


# f = open('data_Json.json','r',encoding=('utf8'))
r = json.dumps(data)
print('.data_Json.json: \n',r,'\n')



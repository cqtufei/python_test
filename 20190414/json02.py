import json

black_json=(8,"Q")
encode_json = json.dumps(black_json)
decode_json = json.loads(encode_json)

print(encode_json,decode_json)

print(type(decode_json),type(encode_json))

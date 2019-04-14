import requests

# r = requests.get('https://api.github.com/events')
# r.json()
# print(r)


r = requests.get('https://api.github.com/events', stream=True)

r.raw
r.raw.read(10)

# with open(filename, 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=128):
#         fd.write(chunk)

print(r)

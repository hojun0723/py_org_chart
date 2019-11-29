import urllib.request

url = 'http://123.123.123.123'

request = urllib.request.Request(url)
request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(request).read()
u = str(response_body, "utf-8")

print(u)

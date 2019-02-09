from urllib.parse import urlencode
para = urlencode({'id': '1003', 'inital': '65'})
print(para)

# output:
# id=1003&inital=65

# requests库，这样写就可以编码
import requests
params = {'id': '1003', 'inital': '65'}
r = requests.get(url="http://www.httpbin.org/get", params=params)
print(r.url)
# output:
# http://www.httpbin.org/get?id=1003&inital=65

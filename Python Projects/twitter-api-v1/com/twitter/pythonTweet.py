from requests.auth import HTTPBasicAuth
import requests

url = 'https://api.twitter.com/2/tweets'
headers = {'Accept': 'application/json', 'apikey' : 'fCDWuQP6sz1yxkdxal3JDvtgl',
           'apisecret' : 'tQx8dJMkj6BB8i7i5Nimv1X0ka5Z3lfbBwDO1icjA6lUcaSUoB',
           'bearer':'AAAAAAAAAAAAAAAAAAAAAOWrZgEAAAAAzF0TC2WBBrh3fKhf6GmvvD3iOvk%3Dz2rh34HrmiT2AefZD9NJXrRR4CAPEYq0Tk22Yzje6KczHlPZEL'}
auth = HTTPBasicAuth('apikey', 'fCDWuQP6sz1yxkdxal3JDvtgl')
myobj = {'text': 'Thats the tweet'}

x = requests.post(url, headers=headers, data = myobj)

print(x.text)

import requests

response = requests.get('http://www.baidu.com')
print(response)
print(response.__dict__)
print(response.content.decode('utf-8'))
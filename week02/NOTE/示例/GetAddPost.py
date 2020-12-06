import requests

# http 协义乌的GET方法
r = requests.get('https://github.com')
r.status_code
r.headers['content-type']
r.encoding
# 选中以上代码，使用shift-enter 执行查看结果
###############################################3

# http 协议的POST方法
import requests
r = requests.post('http://httpbin.org/post', data={'key':'value'})
r.json()

'''
>>> import requests
r = requests.post('http://httpbin.org/post', data={'key':'value'})
r.json()
>>> r = requests.post('http://httpbin.org/post', data={'key':'value'})
>>> r.json()
{'args': {}, 'data': '', 'files': {}, 'form': {'key': 'value'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '9', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.24.0', 'X-Amzn-Trace-Id': 'Root=1-5fcb4bea-31fd0cf329edcb0034f1e2b4'}, 'json': None, 'origin': '114.245.87.208', 'url': 'http://httpbin.org/post'}
>>> 
'''

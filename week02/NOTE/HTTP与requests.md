# HTTP

- w3c 标准

    > 定义网页分为 结构(HTML)、表现(CSS)、行为(JS) 三部分

- HTTP协议和浏览器

    - Headers
        - Request URL
        - Request Method
            - GET
            - POST
        - Status Code
            - HTTP状态码
                - 1xx   信息响应
                - 2xx   成功信息
                - 3xx   重定向
                - 4xx   客户端响应
                - 5xx   服务端响应
        - Cookie
            - 记录验证信息
        - User-Agent
            - 模拟浏览器

    - Request Headers
        - Cookie
        - Host
        - Referer
        - User-agent







# requests 

```python
import requests

url = "https://movie.douban.com/top250"

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'

hearde = {'user-agent': user_agent}
# user-agent不是user_agent

response = requests.get(url, headers=hearde)

print(response.text)
print(f'Code: {response.status_code}')
print(f'Headers: {response.headers}')
```

- GET

```python
In [1]: import requests                                                                                                                                                                        

In [3]: payload = {'key1': 'value1', 'key2': ['value2', 'value3']}                                                                                                                             

In [4]: url = 'http://www.httpbin.org'                                                                                                                                                         

In [5]: r = requests.get(url, params=payload)    

In [10]: r.status_code                                                                                                                                                                         
Out[10]: 200

In [11]: r.url                                                                                                                                                                                 
Out[11]: 'http://www.httpbin.org/?key1=value1&key2=value2&key2=value3'
```

- POST

    

- 模拟Cookie


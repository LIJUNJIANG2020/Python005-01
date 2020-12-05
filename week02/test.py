import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
s.connect(('www.baidu.com', 80))
print(s)
s.send(b'GET / HTTP/1.1\r\nHOST:www.baidu.com\r\nConnection: close\n\r\n')
# 选中代码shift+enter 执行
buffer= []

while True:
    data = s.recv(1024)
    if data:
        buffer.append(data)
    else:
        break
s.close()

print(buffer) 

res = b''.join(buffer) 
header, html = res.split(b'\r\n\r\n',1)

print(header.decode('utf-8'))




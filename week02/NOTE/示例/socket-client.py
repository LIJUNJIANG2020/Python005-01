import socket

HOST = '127.0.0.1'
PORT = 60522


c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect((HOST, PORT)) # 连接server
while True:
    c_data = input('input >> ')
    if data == 'exit':
        break
    c.sendall(c_data.encode()) # 向server发送数据

    s_data = c.recv(1024)     # 接收server 返回数据

    # 处理返回数据
    if data:
        print(s_data.decode('utf-8'))
    else:
        break
        
c.close()
import socket

HOST = '127.0.0.1'
PORT = 60522

# def echo_server(host=HOST, port=PORT):
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print(f'Connected by {addr}')

    while True:
        c_data = conn.recv(1024)
        if not data:
            break
        conn.sendall(c_data)
    conn.close()
    # print('+++')
s.close()
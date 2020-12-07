import socket
from logout import logToFile
from pathlib import Path

upload = Path(__file__).parent.parent.joinpath('var', 'upload')
up_file = 'tar_file.txt'

if not upload.is_dir():
    Path.mkdir(upload)


def echoServer(host, port, listens=1):
    BIND = (host, port)
    LISTENT = listens

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(BIND)
    s.listen(LISTENT)
    buffer = []

    while True:
        conn, addr = s.accept()
        logToFile(conn)

        while True:
            c_data = conn.recv(1024)
            if not c_data:
                break
            buffer.append(c_data)

        logToFile('传输完成')
        with open(upload.joinpath(up_file), 'w') as f:
            # print(Path(__file__))
            for line in buffer:
                f.write(line.decode())

        logToFile('已写入文件 tra_file.txt')
        conn.close()
    s.close()


if __name__ == "__main__":
    echoServer(host='127.0.0.1', port=60522)
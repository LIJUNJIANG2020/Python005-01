import socket
import os.path

def echoClient(host, port):
	URL = (host, port)

	c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	c.connect(URL)

	file_path = input('输入要上传的文件路径： ')
	if os.path.isfile(file_path):
		with open(file_path, 'r') as f :
			for line in f.readlines():
				# print(line)
				c.sendall(line.encode())
				# print('send')
	else:
		print('input error')

					

if __name__ == "__main__":
	echoClient('127.0.0.1', 60522)
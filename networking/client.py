import socket

host = '127.0.0.1'
port = 8080

s = socket.socket()
s.connect((host,port))

message = input("Enter your message to capitalize : ")

while message != 'q':
	s.send(message.encode('utf-8'))
	data = s.recv(1024).decode('utf-8')
	print(data)
	message = input("Enter your message to capitalize : ")

s.close()
import socket
host = '127.0.0.1'
port = 8080

s = socket.socket()
s.bind((host,port))

s.listen(2)

c,addr = s.accept()
print("Connected @ " + str(addr))

while 1:
	data = c.recv(1024).decode('utf-8')
	if not data:
		break
	print("Received: " + data )
	data = data.upper()
	print("Sending " + data)
	c.send(data.encode('utf-8'))

c.close()




import socket
def Main():
	host = '10.10.9.105'
	port = 5011
	s = socket.socket()
	s.bind((host,port))
	s.listen(1)
	c,addr = s.accept()
	print("Connection" + str(addr))
	while True:
		data = c.recv(1024).decode().split()
		if not data:
			break
		print("Connected User" + str(data))
		if data[1] == 'INR' and data[4] == 'Dollar':
			# print("accept" + str(data))
			data1 = int(data[2]) / 67
			c.send(str(data1).encode())
		elif data[1] == 'Dollar' and data[4] == 'INR':
			data1=int(data[2])*67
			c.send(str(data1).encode())
		elif data[1] == 'Pound' and data[4] == 'INR':
			data1 = int(data[1]) * 89
			c.send(str(data1).encode())
		elif data[1] == 'INR' and data[4] == 'Pound':
			data1 = int(data[2]) / 89
			c.send(str(data1).encode())
		elif data[1] == 'Pound' and data[4] == 'Dollar':
			data1 = int(data[2]) * 1.27
			c.send(str(data1).encode())
		elif data[1] == 'Dollar' and data[4] == 'Pound':
			data1 = int(data[2]) / 1.27
			c.send(str(data1).encode())
		elif data[1] == 'YEN' and data[4] == 'INR':
			data1 = int(data[2]) * 0.63
			c.send(str(data1).encode())
		elif data[1] == 'Pound' and data[4] == 'YEN':
			data1 = int(data[2]) * 142.14
			c.send(str(data).encode())
		elif data[1] == 'YEN' and data[4] == 'Pound':
			data1 = int(data[2]) /142.14
			c.send(str(data).encode())
		elif data[1] == 'Dollar' and data[4] == 'YEN':
			data1 = int(data[2]) * 112.33
			c.send(str(data1).encode())
		elif data[1] == 'YEN' and data[4] == 'Dollar':
			data1 = int(data[2]) / 112.33
			c.send(str(data1).encode())
	c.close()
if __name__ == '__main__':
	Main()




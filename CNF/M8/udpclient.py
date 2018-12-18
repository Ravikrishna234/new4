import socket
def func1():
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	host = '10.10.9.105'
	port = 8021
	server = (host,port)
	s.bind((host,port))
	print("client started")
	data = input()
	while True:
		s.sendto(str(data).encode('ASCII'),server)
		data, addr = s.recvfrom(1024)
		print("Received from server" + str(data.decode('ASCII')))
		data = input()
	s.close()
if __name__ == '__main__':
	func1()
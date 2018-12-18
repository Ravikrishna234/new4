import socket

def func():
	host = '10.10.9.105'
	port =5000

	s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))

	print("Server Started... ")
	while True:
		data, addr = s.recvfrom(1024)
		print("message from" + str(addr))
		print("received from" + str(data))
		data = str(data.decode('ASCII')).upper()
		print("sending"+str(data))
		s.sendto(str(data).encode('ASCII'),addr)

	s.close()
if __name__ == '__main__':
	func()
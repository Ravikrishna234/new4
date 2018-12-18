import socket
def Main():
    host = '10.10.9.105'
    port = 5011
    s = socket.socket()
    s.connect((host, port))

    while True:
        print("From currency")
        message = input("-> ")
        s.send(message.encode())
        data = s.recv(1024).decode()
        print("Received"+str(data))
    s.close()
if __name__ == '__main__':
    Main()





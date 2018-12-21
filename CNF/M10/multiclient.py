import socket
import threading
from _thread import *
def Main():
    host = '10.10.9.105'
    port = 5001
    client = True
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    user = input("Enter your user name")
    s.connect((host, port))
    start_new_thread(receivemsg,(s,))
def receivemsg(sock):
    while True:
        msg = sock.recv(1024).decode('ascii')
        print(msg)

    while client:
        msg = input()
        msg1 = user + ">" + msg
        s.send(msg1.encode())
    s.close()
if __name__ == '__main__':
    Main()
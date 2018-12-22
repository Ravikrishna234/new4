import socket
import sys
import threading
def receivemsg(sock):
    serverdown = False
    while client and(not serverdown):
        # try:
        msg = sock.recv(1024).decode('ascii')
        print(msg)
        inp = input()
        msg2 = sock.send(str(inp).encode('ascii'))
        message1 = sock.recv(1024).decode('ascii')
        message = message1.split()
        if(message[0] == "ATTENDANCE"):
            print("ATTENDANCE AWARDED")
        else:
            print("No attendance")
        # except:
            # print('Server is Down. You are now Disconnected. Press enter to exit...')
            # serverDown = True
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    uname = input("Enter your username")
    ip = input("Enter your IP address")
    port = 5011
    s.connect((ip,port))
    s.send(uname.encode('ascii'))
    msg1 = s.recv(1024).decode('ascii')
    print(msg1)
    client = True
    # receivemsg(s)
    threading.Thread(target = receivemsg, args = (s,)).start()
    # while client:
    #     tmp = input()
    #     s.send(tmp.encode('ascii'))

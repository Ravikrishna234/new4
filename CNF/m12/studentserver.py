import socket
import threading
from _thread import *
import csv

def handlestudents(client,rollno):
    client1 = True
    keys = students.keys()
    values = students.values()
    # msg = client.recv(1024).decode('ascii')
    count = 0
    if count == 0:
        for msg in keys:
            if(rollno in msg):
                message1 = students.get(rollno)
                print(message1[0])
                count = count + 1
                client.send(message1[0].encode('ascii'))
        # message = client.recv(1024).decode('ascii')
    if count == 1:
        clientrun = False
        ans = client.recv(1024).decode('ascii')
        if not clientrun:
            for answer in values:
                if(ans in answer):
                    client.send("ATTENDANCE AWARDED".encode('ascii'))
                    clientrun = True
                    break


        if(not clientrun):
            client.send("No ATTENDANCE".encode('ascii'))
            clientrun = True
        else:
            client.send("No person found".encode('ascii'))
if __name__ == '__main__':
    students = {}
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server = True
    with open('data.csv','r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            key = row[0]
            students[key] = [row[1],row[2]]
    # print(students)
    csvFile.close()
    host = socket.gethostname()
    port = 5011
    clients = {}
    host1 = socket.gethostbyname(host)
    s.bind((host,port))
    print("Server start")
    print("IP address of the server::%s"%host1)
    s.listen(10)
    while server:
        client,addr = s.accept()
        rollno = client.recv(1024).decode('ascii')
        print("Connected to the server" + str(rollno))
        client.send("Welcome to class".encode('ascii'))
        if(client not in clients):
            if(rollno in students.keys()):
                clients[rollno] = client
            # handlestudents(client,rollno)
                threading.Thread(target = handlestudents, args = (client,rollno,)).start()
                client.send("Roll Number Found".encode('ascii'))
            else:
                client.send("No rollnumber found".encode('ascii'))
                break
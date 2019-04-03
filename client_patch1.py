import socket
import math


def process(m):
    m.sum()
            
    return m


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
sol = []
try:
    m = sock.recv(1024).decode()
   # print(m)
    a = m.split(',')
    b =[]
    temp = []
    for i in range(len(a)):
        b.append(int(a[i]))

    m = process(b)
    
    for i in range(len(m)):
        temp.append(str(m[i]))

    temp = ','.join(map(str, temp))
    #process(m)
    #sol.append(process(m))
    print(temp)
    sock.send(temp.encode())

finally:
    print('closing socket')
    sock.close()

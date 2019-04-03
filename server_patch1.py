# Python program to implement server side of chat room. 
import socket 





def mergeSort(m):
    return m




# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)



#code for dist

no_of_clients = 3








clients = []
msgs = ["12,11,13,1454,143,254523,3424,13214,23242432,24524,3242,234242,234,3424,45,43534,2423,45,34534,242,23432,234,24,24,23", "14,10,452,23424,2432432,234,4,45,2343,5454,2455,2342,45,45454,4254,546,35,676,435,654,764,34,564,354,434","2,1,342,34,574,34564,3455,564,23543,45656,456,34,56,3534,65,353,54,3,5435,65,565,34,65,563,65,34"]
sol = []


try:
   	# Wait for a connection
    print('waiting for a connection')
    # connection, client_address = sock.accept()
    
    while(len(clients) < no_of_clients):
    	clients.append(sock.accept())

    for i in range(len(msgs)):
    	clients[i][0].send(msgs[i].encode())

    for i in range(len(msgs)):
    	sol.append(clients[i][0].recv(1024).decode())
    print(sol)

    a = sol.split(',')
    b =[]
    temp = []
    for i in range(len(a)):
        b.append(int(a[i]))

    

finally:
    # Clean up the connection
    for i in range(len(clients)):
    	clients[i][0].close

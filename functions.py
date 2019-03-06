import socket
import numpy as np
import cv2
import io as StringIO

class Client():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost',8000)

    def connect(self):
        self.s.connect(self.address)

    def recieveAndPrintMessage(self):
        
        print(message)

    def closeConnection(self):
        self.s.close()

    def getData(self):
        gb = bytes(0)
        while True:
            rb = self.s.recv(1024)
            if not rb: 
                break
            print("sending %d"%len(gb))
            gb = gb + rb
        # t = self.s.recv(1024)
        self.data = np.fromstring(gb,dtype=np.float64)
        print(self.data.shape)












class Host():
    def __init__(self,no_of_clients = 2):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost', 8000)
        self.s.bind(self.address)
        self.s.listen(1)
        self.no_of_clients = no_of_clients
        self.clients = []
        self.data = np.asarray(cv2.imread('img.jpg'),dtype = "int32")
        # self.data = np.random.rand(4,2,3)
    
    def printData(self):
        print(self.data.shape)

    def connectToClients(self):
        while(len(self.clients) < self.no_of_clients):
            self.clients.append(self.s.accept())
        self.s.close()

    def sendMessageToAll(self):
        for i in range(len(self.clients)):
            self.clients[i][0].send(("connected to " + str(i)).encode())

    def closeAll(self):
        for i in range(len(self.clients)):
            self.clients[i][0].close()

    def sendData(self):
        t = int(self.data.shape[0]/self.no_of_clients)
        for i in range(len(self.clients)):
            sendingMessage = (self.data[i*t:(i + 1)*t]).tostring()
            print("sending %d",len(sendingMessage))
            self.clients[i][0].send(sendingMessage)

    

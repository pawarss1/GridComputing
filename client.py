
from functions import *

try:
	client = Client() 
	print("client created")
	client.connect()
	print("client connected")
	client.getData()
	print("Message recived")

finally:
	client.closeConnection()



from functions import *

try:
	host = Host()
	host.printData()
	print("host created")
	host.connectToClients()
	print("conntcted to clinets")
	host.sendData()
	print("sent messages")

finally:
	host.closeAll()



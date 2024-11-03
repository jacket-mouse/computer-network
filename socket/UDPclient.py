from socket import *


server_name = "10.27.138.11"
server_port = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message = input('Input lowercase sentence:')
    if message == "leeson":
        break
    clientSocket.sendto(message.encode(), (server_name, server_port))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
clientSocket.close()
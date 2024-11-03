# import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) 
# Prepare a sever socket 

server_port = 12000
serverSocket.bind(('', server_port))
serverSocket.listen(1)

while True:     
    # Establish the connection    
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:         
        message = connectionSocket.recv(1024).decode() # 'GET /HelloWorld.html HTTP/1.1\r\nHost: localhost:12000\r\nSec-Fetch-Site: none\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Mode: navigate\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0.1 Safari/605.1.15\r\nAccept-Language: zh-CN,zh-Hans;q=0.9\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate\r\n\r\n'
        filename = message.split()[1] # /HelloWorld.html                           
        # with open(filename[1:], "r") as f: # HelloWorld.html
        #     outputdata = [line.encode() for line in f]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket         
        # String
        response_headers = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "Connection: close\r\n"
            f"Content-Length: {len(outputdata)}\r\n"
            "\r\n"
        )
        connectionSocket.send(response_headers.encode())
 
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        error = "HTTP/1.1 404 Not Found\r\n"
        connectionSocket.send(error.encode())
 
        # Close client socket
        connectionSocket.close()          
serverSocket.close()
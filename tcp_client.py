#!/usr/bin/python
import socket

target_host = 'google.com'
target_port = 80

#socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to client
client.connect((target_host, target_port))
#send data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())
#receive response
response = client.recv(4096).decode()
print(response)

import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server,port = 'localhost',8989

reqSchema = {
        "type": "Provider",
        "show": "Databases"
    }
reqSchema = json.dumps(reqSchema)
s.connect((server,port))
s.send(reqSchema.encode('UTF-8'))
print(s.recv(1024).decode('UTF-8'))
s.close()
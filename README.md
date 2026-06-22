# TCP-Socket-Based-Client-Server-Communication-System
This project enables communication between two computers using TCP socket programming. One computer acts as a server and the other as a client, allowing reliable message exchange after establishing a network connection.


# for server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Waiting for connection...")

client, addr = server.accept()
print(f"Connected by {addr}")

while True:
    message = client.recv(1024).decode()
    if not message:
        break
    print("Client:", message)


    reply = input("You: ")
    client.send(reply.encode())


#for client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("10.207.98.224" ,5000))

while True:
    msg = input("You: ")
    client.send(msg.encode())

    if msg.lower() =="exit":
        break

    reply = client.recv(1024).decode()
    print("Server:", reply)

client.close()

client.close()
server.close()

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("10.115.140.13" ,5000))

while True:
    msg = input("You: ")
    client.send(msg.encode())

    if msg.lower() =="exit":
        break

    reply = client.recv(1024).decode()
    print("Server:", reply)

client.close()
import socket

port = 5050
data_len = 16
format = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)

server.bind((server_ip, port))
server.listen()

print("Server is listening...")

while True:
    server_socket, client_addr = server.accept()
    print("Connected to:", client_addr)

    connected = True
    while connected:
        msg_len_raw = server_socket.recv(data_len).decode(format)
        if not msg_len_raw:
            break

        msg_len = int(msg_len_raw.strip())
        message = server_socket.recv(msg_len).decode(format)
        print("Received message:", message)
        if message == "Disconnect":
            connected = False
            server_socket.send("Disconnect received".encode(format))
            continue

        #For Counting vowels
        vowels = "aeiouAEIOU"
        count = sum(1 for c in message if c in vowels)
        if count == 0:
            reply = "Not enough vowels"
        elif count <= 2:
            reply = "Enough vowels I guess"
        else:
            reply = "Too many vowels"

        server_socket.send(reply.encode(format))

    server_socket.close()

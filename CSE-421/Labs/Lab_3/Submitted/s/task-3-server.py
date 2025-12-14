import socket
import threading

port = 5050
data_len = 16
format = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)
server.bind((server_ip, port))
server.listen()
print("Multi-threaded Vowel Server is listening...")


def handle_client(client_socket, client_addr):
    print("Connected to:", client_addr)
    connected = True

    while connected:
        msg_len_raw = client_socket.recv(data_len).decode(format)
        if not msg_len_raw:
            break

        msg_len = int(msg_len_raw.strip())
        message = client_socket.recv(msg_len).decode(format)
        print(f"[{client_addr}] Received message:", message)

        if message == "Disconnect":
            connected = False
            client_socket.send("Disconnect received".encode(format))
            break

        # Count vowels
        vowels = "aeiouAEIOU"
        count = sum(1 for c in message if c in vowels)

        if count == 0:
            reply = "Not enough vowels"
        elif count <= 2:
            reply = "Enough vowels I guess"
        else:
            reply = "Too many vowels"

        client_socket.send(reply.encode(format))

    client_socket.close()
    print("Disconnected:", client_addr)


while True:
    client_socket, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()

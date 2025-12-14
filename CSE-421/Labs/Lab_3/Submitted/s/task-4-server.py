import socket

port = 5050
data_len = 16
format = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)
server.bind((server_ip, port))
server.listen()
print("Salary Server is listening...")


while True:
    server_socket, client_addr = server.accept()
    print("Connected to:", client_addr)
    connected = True
    while connected:
        # Received message length
        msg_len_raw = server_socket.recv(data_len).decode(format)
        if not msg_len_raw:
            break

        msg_len = int(msg_len_raw.strip())
        # Received actual message (hours)
        hours_str = server_socket.recv(msg_len).decode(format)
        print("Received hours:", hours_str)

        # Disconnect checking
        if hours_str == "Disconnect":
            server_socket.send("Disconnect received".encode(format))
            connected = False
            continue

        hours = int(hours_str)

        # Salary calculation
        if hours <= 40:
            salary = hours * 200
        else:
            salary = 8000 + (hours - 40) * 300

        reply = f"Salary = Tk {salary}"
        server_socket.send(reply.encode(format))

    server_socket.close()
    print("Disconnected:", client_addr)

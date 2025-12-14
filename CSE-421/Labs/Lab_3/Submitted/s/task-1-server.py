import socket

port = 5050
data_len = 16
format = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)

server_socket_address = (server_ip, port)
server.bind(server_socket_address)

server.listen()
print('The server is listening....')

while True:
    server_socket, client_add = server.accept()
    print('Connected to:', client_add)

    connected = True
    while connected:

        msg_len_raw = server_socket.recv(data_len).decode(format)

        if not msg_len_raw:   # client forced to close
            break

        msg_len = int(msg_len_raw.strip())  # for safer length parsing

        message = server_socket.recv(msg_len).decode(format)

        print('Received message:', message)

        if message == 'Disconnect':
            print('Server disconnected with:', client_add)
            connected = False

        server_socket.send('hello client - message received'.encode(format))

    server_socket.close()

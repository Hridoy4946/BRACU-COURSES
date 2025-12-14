import socket

port = 5050
data_len = 16
format = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)
client.connect((server_ip, port))


def send_msg(msg):
    message = msg.encode(format)
    msg_len = len(message)
    msg_len_str = str(msg_len).encode(format)
    msg_len_str += b" " * (data_len - len(msg_len_str))

    client.send(msg_len_str)
    client.send(message)
    response = client.recv(128).decode(format)
    print("Server:", response)


# Test cases
send_msg("sky") #Not enough vowels
send_msg("hi") #Enough vowels I guess
send_msg("hello world") #Too many vowels
send_msg("aeiou") #Too many vowels
send_msg("Disconnect")

client.close()

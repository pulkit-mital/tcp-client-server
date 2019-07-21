import socket

target_host = "127.0.0.1"
target_port = 1234

# create a scoket object
# AF_INEt => going to user standard IPv4 address or hostname
# SOCK_STRAM  => indicates this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client
client.connect((target_host, target_port))

response = client.recv(4096)

print(response.decode())

client.close()

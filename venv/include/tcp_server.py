import socket

client = socket.socket()

# reserve a port on the computer

port = 1234

# next bind the server to port
# not typed any IP address in Ip field
# instead we are inputting the empty string
# this makes our server listen to request
# from different computers in the network
client.bind(('', port))
print("socket binded to ", port)

# put the socket in the listening mode
client.listen(5)
print("socket is listening...")

# a infinite loop until will interrupt or throws error
while True:
    cli, addr = client.accept()
    print("got connection from", addr)
    cli.send('Thank you for connecting'.encode())
    cli.close()


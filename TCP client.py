import socket


target_host = "localhost"
target_port = 80

# Create a socket object
# Anytime you make a TCP request this is what you need

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to our target
# Anytime you make a connect, make it a twople
client.connect((target_host, target_port))

# Once you connect you need to send some data
client.send(b"GET / HTTP/1.1\r\nHOST:google.com\r\n\r\n")


# Recieve the HTTP response
# Set the buffer size to 4096
response = client.recv(4096)
print(response)
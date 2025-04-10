import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


ip_address = "192.168.112.245"
port = 6969
complete = (ip_address, port)

while True:
    message = input("Enter your message: ")
    encoded_message = message.encode('ascii')
    s.sendto(encoded_message, complete)


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip_address = "192.168.112.244"
port = 8080
complete = (ip_address, port)
s.bind(complete)

while True:
    msg = s.recvfrom(1024) 
    print(msg[0].decode('ascii'))
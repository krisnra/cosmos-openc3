import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 26000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Listening for command packets on port", UDP_PORT)
while True:
    data, addr = sock.recvfrom(1024)
    print("Received:", [hex(x) for x in data])

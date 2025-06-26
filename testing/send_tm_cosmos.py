import socket
import struct
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 8081

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
count = 0
while True:
    tlm_id = 1      # harus sesuai ID_ITEM di tlm.txt
    temp = 77      # suhu, uint16
    volt = 2150     # tegangan, uint16
    # >BHHB = big-endian: 1byte(ID), 2byte(temp), 2byte(volt), 1byte(count)
    data = struct.pack(">BHHB", tlm_id, temp, volt, count)
    sock.sendto(data, (UDP_IP, UDP_PORT))
    print("Send TLM:", tlm_id, temp, volt, count)
    count = (count + 1) % 256
    time.sleep(1)

import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 10025

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print("Menunggu paket TC di port", UDP_PORT)

while True:
    data, addr = sock.recvfrom(1024)
    print("Paket TC diterima (hex):", data.hex())
    
    # --- Decode CCSDS Primary Header (6 byte) ---
    if len(data) < 11:
        print("Paket terlalu pendek!")
        continue

    # Unpack CCSDS header
    (pri1, pri2, length) = struct.unpack(">HHH", data[0:6])
    version    = (pri1 >> 13) & 0x7
    type_      = (pri1 >> 12) & 0x1
    sec_hdr    = (pri1 >> 11) & 0x1
    apid       = pri1 & 0x7FF
    grp_flags  = (pri2 >> 14) & 0x3
    seq_count  = pri2 & 0x3FFF

    print("=== CCSDS Header ===")
    print(f"Version: {version}")
    print(f"Type: {type_}")
    print(f"SecHdrFlag: {sec_hdr}")
    print(f"APID: {apid}")
    print(f"Group Flags: {grp_flags}")
    print(f"Sequence Count: {seq_count}")
    print(f"Packet Length: {length}")

    # --- Decode Payload (mulai byte ke-6) ---
    # Misal: Packet_ID (uint16), ParamValue (uint32), (tambah jika ada field lain)
    payload = data[6:]
    if len(payload) < 6:
        print("Payload terlalu pendek!")
        continue

    packet_id, param_value = struct.unpack(">HI", payload[:6])
    print("=== Payload ===")
    print(f"Packet_ID: {packet_id}")
    print(f"ParamValue: {param_value}")

    # Jika ada argumen lain, lanjutkan parsing sesuai urutan xtce.xml


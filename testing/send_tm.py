import socket
import struct

# CCSDS Primary Header
version = 0      # 3 bit
type_ = 0        # 1 bit (TM)
sec_hdr_flag = 0 # 1 bit
apid = 100       # 11 bit

primary_header = ((version << 13) | (type_ << 12) | (sec_hdr_flag << 11) | apid)
group_flags = 3  # standalone
seq_count = 1
seq_flags_and_count = ((group_flags << 14) | seq_count)
# Jumlah payload = 4 * 18 (float32) = 72 byte (asumsi kamu isi 18 float)
packet_length = 72  # (dummy, hitung benar sesuai payload)

header = struct.pack(">HHH", primary_header, seq_flags_and_count, packet_length)

# Payload: isi sesuai urutan Spacecraft container!
payload = b""
payload += struct.pack(">f", 0.0)  # EpochUSNO
payload += struct.pack(">I", 0)    # OrbitNumberCumulative
payload += struct.pack(">I", 0)    # ElapsedSeconds
payload += struct.pack(">f", 0.0)  # A
payload += struct.pack(">f", 0.0)  # Height

payload += struct.pack(">fff", 0.0, 0.0, 0.0)  # Position (x, y, z)
payload += struct.pack(">fff", 0.0, 0.0, 0.0)  # Velocity (x, y, z)
payload += struct.pack(">f", 990)              # Latitude
payload += struct.pack(">f", 5566)              # Longitude

payload += struct.pack(">f", 10)              # Battery1_Voltage (ISI DATA)
payload += struct.pack(">f", 8.5)              # Battery2_Voltage
payload += struct.pack(">f", 0.0)              # Battery1_Temp
payload += struct.pack(">f", 0.0)              # Battery2_Temp

payload += struct.pack(">fff", 0.0, 0.0, 0.0)  # Magnetometer (x, y, z)
payload += struct.pack(">f", 0.0)              # SunsensorS
payload += struct.pack(">fff", 22, 33, 44)  # Gyro (x, y, z)
payload += struct.pack(">f", 0.0)              # Detector_Temp

# Tambahkan semua boolean flag dan enum sesuai urutan (isi 0 saja untuk dummy)
for _ in range(19):  # misal ada 19 boolean
    payload += struct.pack(">B", 0)  # bool_t = 8 bit

for _ in range(3):   # enum (isi 0)
    payload += struct.pack(">B", 0)

# Gabung header dan payload
packet = header + payload

# Kirim ke UDP port 10015
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(packet, ("127.0.0.1", 10015))
print("Paket telemetry dikirim.")


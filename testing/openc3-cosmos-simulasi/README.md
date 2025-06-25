# openc3-cosmos-simulasi

Plugin COSMOS (OpenC3) untuk simulasi telemetri SAT1. Plugin ini memungkinkan COSMOS menerima data telemetri SAT1 melalui koneksi UDP dari sumber eksternal.

## Penggunaan
1. **Instal Plugin:** Build dan install gem plugin ini ke dalam COSMOS Anda.
2. **Konfigurasi:** Secara default plugin disetel menerima telemetri di UDP port 26001 dari `127.0.0.1`. Jika perlu, ubah IP/port di `plugin.txt` atau via VARIABLE saat instalasi.
3. **Pengiriman Data:** Gunakan program eksternal (misalnya Python) untuk mengirim paket data telemetri ke COSMOS. Contoh sederhana (Python):

    ```python
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Contoh paket telemetri: [ID=1][TEMP=25][VOLT=3000][COUNT=5]
    packet = bytes([0x01, 0x00, 0x19, 0x0B, 0xB8, 0x05])
    sock.sendto(packet, ("127.0.0.1", 26001))
    print("Telemetry packet sent")
    ```
    Format paket mengikuti definisi di `tlm.txt`: byte pertama ID = 1, diikuti temperature 16-bit, voltage 16-bit, dan counter 8-bit.

4. **Menjalankan COSMOS:** Jalankan COSMOS OpenC3, buka **Telemetry Viewer** untuk target SAT1. Anda akan melihat nilai telemetry (TEMP, VOLT, dll) terupdate setiap kali paket dikirim.



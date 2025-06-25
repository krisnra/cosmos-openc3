# Demo procedure untuk SAT1

# Pastikan modul COSMOS scripting ter-load
require 'cosmos/script'

# 1. Kirim command PING ke SAT1
puts "Sending PING command to SAT1..."
cmd("SAT1", "PING")  # Mengirim perintah PING (tanpa parameter)

# 2. Tunggu sedikit untuk memastikan telemetry update (jika ada respon)
wait(1)

# 3. Cek nilai telemetry saat ini
temp = tlm("SAT1", "STATUS", "TEMP")
volt = tlm("SAT1", "STATUS", "VOLT")
count = tlm("SAT1", "STATUS", "COUNT")
puts "Current Telemetry - TEMP: #{temp} °C, VOLT: #{volt} mV, COUNT: #{count}"

# 4. Kirim command SET_VALUE dengan parameter
puts "Sending SET_VALUE command with VALUE=123..."
cmd("SAT1", "SET_VALUE", "VALUE" => 123)

# 5. Tunggu dan kemudian verifikasi (dalam simulasi ini command tidak mengubah telemetry, 
# tapi kita bisa ilustrasikan seolah menunggu perubahan)
wait_check("SAT1 STATUS COUNT != #{count}", 5)  # tunggu hingga COUNT berubah (misal next packet)

puts "Demo procedure complete."


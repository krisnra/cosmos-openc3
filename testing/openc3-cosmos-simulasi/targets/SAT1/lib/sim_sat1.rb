# lib/sim_sat1.rb

# Module/Namespace untuk target SAT1 (opsional digunakan)
module SimSat1
  # Contoh: method untuk memproses command PING (hanya logging)
  def self.process_ping
    OpenC3::Logger.info("SAT1 PING command received at COSMOS simulation.")
  end

  # Method untuk memproses command SET_VALUE dengan parameter
  def self.process_set_value(val)
    OpenC3::Logger.info("SAT1 SET_VALUE command received with value=#{val}.")
    # (Dalam simulasi ini, tidak ada perangkat riil yang diubah, hanya log.)
  end
end


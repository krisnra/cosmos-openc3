# encoding: utf-8
require 'rbconfig'

Gem::Specification.new do |spec|
  spec.name        = 'openc3-cosmos-simulasi'      # Nama gem plugin
  spec.summary     = 'OpenC3 COSMOS plugin for SAT1 simulation (UDP telemetry input)'
  spec.description = <<-DESC
Plugin COSMOS (OpenC3) untuk simulasi SAT1.
Memungkinkan penerimaan telemetry SAT1 melalui koneksi UDP.
DESC
  spec.authors     = ['Nama Anda']
  spec.email       = ['email@contoh.com']
  spec.license     = 'MIT'
  spec.platform    = Gem::Platform::RUBY

  # Versi diambil dari environment variable atau default 0.0.1
  spec.version = ENV['VERSION'] ? ENV['VERSION'].dup : '0.0.2'

  # Sertakan semua file yang diperlukan dalam gem
  spec.files = Dir['plugin.txt'] + ['Rakefile', 'README.md'] + Dir['targets/**/*']

  # Dependensi runtime (OpenC3 COSMOS) - opsional, sesuaikan versi bila perlu
  spec.add_runtime_dependency 'openc3'
end


:start
D:\esptool.exe --chip esp32s3 erase_flash
D:\esptool.exe --chip esp32s3 --baud 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_freq 80m --flash_size detect 0x0 firmware_s3.bin
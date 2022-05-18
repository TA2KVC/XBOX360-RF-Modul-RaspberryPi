# XBOX360-RF-Modul-RaspberryPi
XBOX 360 RF Module - Raspberry Pi İletişimi

Wiringpi kütüphanesinin kurulması gerekiyor.

Role olarak NPN transistor kullandım. PN2222A veya 2N2222 transistor kullanılabilir. Eldeki PN2222A yı kullandım.

Sonsuz döngüde çalışması için While True: komutu kullanıldı

Raspberry Pi başlangıcında çalışması için
başında "sudo" komutu olmadan:

crontab -e

komutundan sonra

@reboot cd /home/pi/Vol && /usr/bin/python example.py &

satırları eklendi.

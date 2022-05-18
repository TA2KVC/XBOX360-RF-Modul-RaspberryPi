import xbox_rf

# xbox_rf kutuphanesinin eklenmesi ve
# XBOX 360 RF Modul Led Animasyonlarinin baslatilmasi
# Boot Animasyonunun sonsuz dongude tekrarlanmasi icin kutuphaneye role amacli 2n2222 transistoru calistiran kod eklendi
while True:
        xbox_rf.Delay(1000)
        print("1/5 Powering..")
        xbox_rf.RelayOn()
        print("2/5 Initializing..")
        xbox_rf.Init()
        print("3/5 Animasyon")
        xbox_rf.BootAnimation()
        print("4/5 Wait...")
        xbox_rf.Delay(5000)
        print("5/5 Poweroff..")
        xbox_rf.RelayOff()

nilai = int(input("Masukan nilai ujian anda :"))
if nilai >= 80  and nilai <= 100 :
    a = "A"
    print("nilai anda %s, Maka Grade Anda adalah %s" % (nilai,a))
elif nilai >= 70 and nilai <= 79 :
    b = "B"
    print("nilai anda %s, Maka Grade Anda adalah %s" % (nilai,b))
elif nilai >= 60 and nilai <= 69 :
    c = "C"
    print("nilai anda %s, Maka Grade Anda adalah %s" % (nilai,c))
elif nilai >= 50 and nilai <= 59 :
    d = "D"
    print("nilai anda %s, Maka Grade Anda adalah %s" % (nilai,d))
else :
    e = "E"
    print("nilai anda %s, Maka Grade Anda adalah %s" % (nilai,e))
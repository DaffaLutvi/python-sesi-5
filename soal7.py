berat = float(input("Masukan berat badan (kg) : "))
tinggi = float(input("Masukan tinggi badan (m) : "))
tinggi2 = tinggi * tinggi
hasil = berat / tinggi2

if hasil >= 30.0:
    kategori = "Kegemukan"
elif hasil >= 25.0 and hasil < 30.0:
    kategori = "Kelebihan Berat Badan"
elif hasil >= 18.5 and hasil < 25.0:
    kategori = "Normal"
else :
    kategori = "Kurang Berat Badan"
    
print("Dengan BMI %s,Maka kamu termasuk kedalam %s" % (hasil, kategori))
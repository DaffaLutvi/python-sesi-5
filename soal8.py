sisi1 = int(input("Masukan sisi pertama: "))
sisi2 = int(input("Masukan sisi kedua: "))
sisi3 = int(input("Masukan sisi ketiga: "))

if sisi1 ==0 or sisi2 == 0 or sisi3 == 0:
    kategori = "Tidak Dapat membuat segitiga"
elif sisi1 == sisi2 and sisi2 == sisi3:
    kategori = "Segitiga Sama Sisi"
elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
    kategori = "Segitiga Sama Kaki"
else:
    kategori = "Segitiga Sembarang"
print("%s adalah hasil yang kamu dapatkan dengan angka yang kamu masukan" % (kategori))
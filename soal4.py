wadah = []
nilai1 = int(input("Masukan angka pertama: "))
wadah.append(nilai1)
nilai2 = int(input("Masukan angka kedua:"))
wadah.append(nilai2)
nilai3 = int(input("Masukan angka ketiga:"))
wadah.append(nilai3)
wadah.sort(reverse=True)
print("angka terbesarnya adalah %s dari angka diinput" % (wadah[0]))
print("Ini adalah urutannya")
print(wadah)
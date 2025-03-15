nilai1 = int(input("Masukan angka pertama: "))
nilai2 = int(input("Masukan angka kedua: "))
op = input("Masukan operator aritmatika (+, -, *, /): ")
if op == "+":
    hasil_tambah = nilai1 + nilai2
    print("hasilnya adalah: ", hasil_tambah)
elif op == "-":
    hasil_kurang = nilai1 - nilai2
    print("hasilnya adalah: ", hasil_kurang)
elif op == "*":
    hasil_kali = nilai1 * nilai2
    print("hasilnya adalah: ", hasil_kali)
elif op == "/":
    hasil_bagi = nilai1 / nilai2
    print("hasilnya adalah: ", hasil_bagi)
else:
    print("operator yang anda masukan salah")
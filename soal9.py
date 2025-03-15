useradmin, passadmin ="admin","admin123"
useruser,passuser ="user","user123"
userguest = "guest"

inuser = input("Masukan username anda : ")
inpass = input("Masukan password anda(Kosongkan bila anda adalah guest) : ")
if inuser == useradmin and inpass == passadmin:
    kategori = "akses admin"
elif inuser == useruser and inpass == passuser:
    kategori = "akses terbatas"
elif inuser == userguest and inpass == "":
    kategori = "akses minimal"
else:
    kategori = "akses tidak dikenal"
print(kategori,"it adalah akses yang anda dapatkan")
nilai = 90

# Equal eksplisit
if nilai == 50:
    print("Nilai anda adalah:",nilai)

# Equal
if nilai == 80:
    print("Nilai anda adalah:",nilai)

# Not Equal
if nilai != 75:
    print("Nilai anda Bukan: 75")

print(50*"=")

nilai = 100

if 90 <= nilai <= 100:
    print("Nilai anda adalah A")
elif 70 <= nilai <= 80:
    print("Nilai anda adalah B")
elif 60 <= nilai <= 70:
    print("Nilai anda adalah C")
elif 0 <= nilai <= 60:
    print("Mohon Maaf, Anda Harus Mengulang Matkul ini!!!")

print(50*"_")

#Operator logika untuk string dan list
toko_buku = ["Buku Novel","Buku Cerpen","Buku Komik","Buku Tutorial","Buku Agama"]
beli = "Buku Sekolah"

if beli in toko_buku:
    print('Saya beli buku',beli,'seharga 50.000')

if not beli in toko_buku:
    print('Toko buku ini tidak menjual',beli)

huruf = "S"
if huruf in beli:
    print("ada huruf",huruf,"di",beli)
else:
    print("tidak ada huruf",huruf,"di",beli)

print(50*'-')
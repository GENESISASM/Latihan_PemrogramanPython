#List sebagai Iterable
toko_buku = ["Buku Novel","Buku Cerpen","Buku Komik","Buku Tutorial","Buku Agama"]

for a in toko_buku:
    print(a)
    print(len(a))

print(80*'_')

#String sebagai Iterable
Buku_Novel = 'Buku Novel'
for b in Buku_Novel:
    print(b)

print(80*'_')

#For dalam For

sayur = ['bayam','kangkung','kol','popcay','kembang kol']
buah = ['apel','pisang','jeruk','semangka','melon','timun suri']
rempah = ['pala','kemiri','ketumbar','lada','garam','gula']

belanja = [sayur,buah,rempah]

for DaftarBelanja in belanja:
    print(DaftarBelanja)
    for isi in DaftarBelanja:
        print(isi)
    print('\n')
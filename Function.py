#Fungsi Sederhana
def List_tokobuku():
    print('Novel','komik','ensiklopedia')
List_tokobuku()
print(50*'=')

#Fungsi dipanggil Fungsi
def Harga_Buku():
    List_tokobuku()
    print('Harga buku itu semua adalah Rp 150.000')
Harga_Buku()
print(50*'-')

#Membuat fungsi dengan input argumen
def harga_total_buku(pcs):
    harga = 50000
    harga_total_buku = pcs*harga
    print('Harga',pcs,'pcs Buku adalah',harga_total_buku)
harga_total_buku(3)
harga_total_buku(10)
harga_total_buku(1)
harga_total_buku(2)
print(50*'=')
#Scope Variable: Local
pinjamBuku = 'Sarjana Kertas'

def gantiBuku(bukuBaru):
    pinjamBuku = bukuBaru
    print('Buku berikutnya yang saya pinjam adalah',bukuBaru)
gantiBuku('Jongos Berdasi')
gantiBuku('Amor Fati')
print("Buku pertama yang saya pinjam adalah",pinjamBuku)
print(80*'=')

#Scope Variable: Global
BeliBuah = 'Apel'
Beratbeli = '1 Kg'
print('Buah pertama yang saya beli adalah',BeliBuah,'beratnya',Beratbeli)

def BeliLagi(BuahBaru,berat):
    global BeliBuah,Beratbeli
    BeliBuah = BuahBaru
    Beratbeli = berat
    print('Buah berikutnya yang saya beli adalah',BuahBaru,'beratnya',berat)
BeliLagi('Jeruk','2 Kg')
print('Buah yang saya beli adalah',BeliBuah,'beratnya',Beratbeli)
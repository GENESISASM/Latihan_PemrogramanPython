#While dengan menggunakan syarat
angka = 1

while angka < 5:
    print('Nilainya adalah',angka)
    angka +=1
print(50*'=')

#Perulangan dengan Boolean/True,False
start = True
angka = 0
while start:
    print('Hore')
    if angka is 50:
        start = False
        print('Angka 50 ditemukan')
    angka += 5
print(50*'-')

#perulangan dengan Else
nilai = 10
while nilai < 100:
    print('Nilai anda adalah', nilai)
    nilai += 10
else:
    print('Nilai akhir anda adalah', nilai)
print(50*'=')

#perulangan dengan Break
nilai1 = 10
while nilai1 < 100:
    if nilai1 is 50:
        print('Nilai 50 ada')
        break
    print('Nilai anda adalah', nilai1)
    nilai1 += 10
else:
    print('Nilai akhir anda adalah', nilai1)
print(50*'-')

#perulangan dengan Continue
nilai2 = 10
while nilai2 < 100:
    if nilai2 is 50:
        print('Nilai 50 ada')
        nilai2 += 10
        continue
    print('Nilai anda adalah', nilai2)
    nilai2 += 10
    #if nilai2 is 50:
    #    print('Nilai 50 ada')
    #    continue
else:
    print('Nilai akhir anda adalah', nilai2)
print(50*'=')

#Perulangan dengan Pass
nilai2 = 10
while nilai2 < 100:
    if nilai2 is 50:
        pass
    print('Nilai anda adalah', nilai2)
    nilai2 += 10
else:
    print('Nilai akhir anda adalah', nilai2)
print(50*'-')
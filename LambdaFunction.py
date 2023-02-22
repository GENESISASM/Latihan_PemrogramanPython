def jumlah(a,b):
    c = a+b
    return c

hasil = jumlah(5,5)
print(hasil)
print(50*'=')

#build an Anonymous function with lambda
kali = lambda x,y: x*y
hasil1 = kali(5,6)
hasil2 = kali(2,2)
hasil3 = kali(hasil1,hasil2)
print(hasil1)
print(hasil2)
print(hasil3)
print(50*'-')

tambah = lambda c,d: c+d
total = tambah(3,4)
total1 = tambah(5,5)
total2 = tambah(2,1)
total3 = tambah(total,total1)
total4 = tambah(total2,total3)

print("hasil dari C + D adalah: ",total4)

tabungan = [100,200,300,400,500]
print('Data saat ini adalah: ',tabungan)
print(100*'=')

#Memasukan Data Baru
tabungan.append(700)
print('Data masuk: ',600)
tabungan.append(800)
print('Data masuk: ',700)
print('Data saat ini adalah: ',tabungan)
print(100*'-')

#Menghapus data terakhir
keluar = tabungan.pop()
print('Data keluar: ',keluar)
print('Data sekarang: ',tabungan)
print(100*'=')

from collections import deque
antrian = deque([1,2,3,4,5,6,7,8])
antrian.append(8)
print('Data masuk: ',9)
print('Data Sekarang: ',antrian)
antrian.append(10)
print('Data masuk: ',10)
print('Data Sekarang: ',antrian)
print(100*'-')

#Mengurangi Antrian dari depan
out = antrian.popleft()
print('Data keluar: ',out)
print('Data Sekarang: ',antrian)
out = antrian.popleft()
print('Data keluar: ',out)
print('Data Sekarang: ',antrian)
out = antrian.popleft()
print('Data keluar: ',out)
print('Data Sekarang: ',antrian)
out = antrian.popleft()
print('Data keluar: ',out)
print('Data Sekarang: ',antrian)
out = antrian.popleft()
print('Data keluar: ',out)
print('Data Sekarang: ',antrian)

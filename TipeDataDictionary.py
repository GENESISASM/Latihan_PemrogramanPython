data_mahasiswa1 = {'ID':5008,"Nama":"Muhammad Saiful Arif","Prodi":"TI","Kelas":"2E"}
data_mahasiswa2 = {'ID':5121,"Nama":"Lita Astri Pramest","Prodi":"TI","Kelas":"2D"}
data_mahasiswa3 = {'ID':5135,"Nama":"Ridwan Maulana Subekti","Prodi":"TI","Kelas":"2B"}

print(data_mahasiswa1["Nama"])
print(data_mahasiswa2.keys())
print(data_mahasiswa3.values())
print(data_mahasiswa2.items())
print(130*'=')
datalis = {5008:data_mahasiswa1,5121:data_mahasiswa2,5135:data_mahasiswa3}
print(datalis[5121])
print(datalis[5008])
print(datalis[5135])
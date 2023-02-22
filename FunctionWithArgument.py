#Fungsi dengan argument sederhana
def keluarga(nama):
    print('Anak dari keluarga ini bernama:',nama)
keluarga('Bolang')
print(50*'=')

#Fungsi dengan keyword
def Mahasiswa(Nama,Prodi):
    print('Mahasiswa ini bernama:',Nama)
    print('Mahasiswa jurusan:',Prodi)
Mahasiswa(Nama="Lita Astri Pramesti",Prodi="Teknik Informatika\n")
Mahasiswa(Prodi="Teknik Mesin",Nama="Aditya")
print(50*'-')

#Fungsi dengan Menggunakan Default Argument
def Dosen(nama,mata_kuliah='Matematika Diskrit',shift='Pagi\n'):
    print('Dosen ini bernama:',nama)
    print('Beliau mengajar di Mata Kuliah:',mata_kuliah)
    print('Beliau mengajar pada:',shift)
Dosen(nama='Bapak Entis Sutisna',mata_kuliah='Kalkulus 1')
Dosen(nama='Ibu Acy',shift='siang\n')
Dosen(nama='Bapak Afizal',mata_kuliah='Sistem Informasi',shift='Sore')
#Dosen(mata_kuliah="Fisika Listrik") "yang ini salah karena dapat menghasilkan eror yakni missing positional 1 dibagian nama"
print(50*'=')
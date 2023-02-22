Nama_Mahasiswa = ['saiful','ridho','arsy','dewi','rizky','faqih']
Nama_Prodi = ['informatika','sastra arab','hukum','komputerisasi akuntansi','informatika','akuntansi']

#Looping dengan Enumerasi
for index,mahasiswa in enumerate(Nama_Mahasiswa):
    print(index, ':',mahasiswa)
print(100*'=')

#Looping dengan zip
for mahasiswa,prodi in zip(Nama_Mahasiswa,Nama_Prodi):
    print(mahasiswa, 'jurusannya adalah:',prodi)
print(100*'=')

#Looping di tipe data set
#set
Mahasiswa = {'arsy','maulida','faiz','dewa','saiful','lulu','sayyidah'}

for pelajar in sorted(Mahasiswa):
    print(pelajar)
print(100*'=')

#Looping di tipe data Dictionary
Mahasiswa1 = {'faqih':'akuntasi','gonjeh':"guru",'maulina':'ekonomi islam','syidad':'dkv','anjali':'dkv'}

#Looping semuanya:
for i in Mahasiswa1.items():
    print(i)
print(100*'=')
#Looping satu-satu:
for a,b in Mahasiswa1.items():
    print(a,'jurusannya:',b)
print(100*'=')
for c,d in reversed(Mahasiswa1.items()):
    print(c,d)
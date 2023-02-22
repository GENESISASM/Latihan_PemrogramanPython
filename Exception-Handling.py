import sys #Mengimport Modul Sys untuk exit
print("Program Pembagian Bilangan")
a = float (input("Masukan Nilai a: "))
b = float (input("Masukan Nilai b: "))

try:
    hasil = a/b
except ZeroDivisionError:
    print("\n ERROR: Nilai B tidak boleh Nol")
    sys.exit(1) #Menghentikan Program

print("\n Nilai a: ",a)
print("\n Nilai b: ",b)
print("Hasilnya adalah: ",hasil)

print(50*'=')
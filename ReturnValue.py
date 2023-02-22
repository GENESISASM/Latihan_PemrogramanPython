# Fungsi dengan return Value
def kuadrat(argumen):
    hasil = argumen **2
    return hasil
a = kuadrat(2)
print(a)

print('='*50)

# Fungsi dengan return value dan multiple argumen
def tambah(angka1, angka2):
    total = angka1 + angka2
    print(angka1,'+',angka2,'=',total)
    return total
def kali(angka1,angka2):
    total = angka1 * angka2
    print(angka1,'X',angka2,'=',total)
    return total
a = kali(5,tambah(2,4))
print(a)
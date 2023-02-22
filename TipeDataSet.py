#Set atau Himpunan:
#Cara Membuat Set terbagi 2:

#Cara Pertama:
Laptop = {"asus",
        "lenovo",
        "hp",
        "apple",
        "dell",
        "samsung"}

Laptop.add("aser")
Laptop.add("samsung")#dalam himpunan, data yang double akan dianggap sama
print(sorted(Laptop))
print(130*'=')

#Cara Kedua:
laptop = set()
laptop.add("asus")
laptop.add("hp")
laptop.add("dell")
laptop.add("lenovo")
laptop.add("apple")
laptop.add("aser")
print(laptop)
print(130*'-')

#Dalam Himpunan bisa digunakan fungsi operasi irisan gabungan dll
Ganjil = {1,3,5,7,9}
Genap = {2,4,6,8,10}
Prima = {2,3,5,7,11,13}

print(Ganjil.union(Prima))
print(Ganjil.union(Genap))
print(Genap.intersection(Prima))
print(Ganjil.intersection(Prima))
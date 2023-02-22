Data1 = [1,2,4,8,16,32,64,128,256,512] #Sebuah deklarasi variable yang memiliki jumlah 10 variable
Data2 = [10,20,40,80,160,320,640,1280,2560,5120]
print(Data1) #Menampilkan variabe Data1 kedalam console
print(Data2, "\n")

# Mengakses List
subdata1 = Data1[5]
subdata2 = Data1[-6]
print(subdata1, subdata2, "\n")

# Memotong List
subdata3 = Data1[0:5]
subdata4 = Data1[:4]
print(subdata3, subdata4, "\n")

# Menambah List
Data3 = Data2 + Data1
Data4 = Data1 + Data1
print(Data3, "\n", Data4, "\n")

# Merubah Content dari List
Data1[5] = 64
Data1[2] = 112
print(Data1, '\n')

# Mengcopy List ke-Variable Baru
a = Data1[:]
a[8] = 1024

# Merubah Content List dengan Menggonakan metode Slicing
Data1[1:5] = [12,13,14,15]
print(a, Data1, '\n')

# list dalam List
x = [Data1, Data2]
print(x, '\n')

# Mengakses List dalam Multidimensional List
y1 = x[0][3]
y2 = x[1][5]
print(y1, y2, '\n')

#  Method untuk List
Data1.append(2048) #Menambah variable baru dengan menggunakan append kedalam Data1 menjadi 11 variable
Data2.append(10240)
print(Data1, Data2, '\n')

# Function will be used on List
panjang_list = len(Data1)
print(Data1, '\n')
print(panjang_list, '\n')
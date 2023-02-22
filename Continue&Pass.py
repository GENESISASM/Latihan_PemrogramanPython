#Loop dengan Break
a = 3
for i in range(0,6):
    if i is a:
        print('Nilai ini adalah:',a)
        break
    print('Nilainya adalah:',i)
else:
    print('Akhir dari program')

print(50*'=')

#Loop dengan Continue
A = 4
for b in range(0,7):
    if b is A:
        print('Nilai ini adalah:',A)
        continue
    print('Nilainya adalah:',b)
else:
    print('Akhir dari program')

print(50*'_')
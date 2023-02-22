#Loop With Range Method
for i in range(0,10,2):
    print(i)

print(50*'-','\n')

#Found a Number With Loop Method
Number = 50

for a in range(10,100,10):
    print(a)
    if a is Number:
        print('Number has Founded')
        break

print(50*'_','\n')

#Loop else
number = 110

for b in range(10,100,10):
    print(b)
    if b is number:
        print('Number has founded')
        break
else:
    print('Number Not Found')

print('\nProgram Telah Berakhir\n')
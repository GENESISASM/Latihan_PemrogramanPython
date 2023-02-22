#Definition of Tuple
data_list = [1,2,3,4,5]
data_tuple = (1,2,3,4,5)
print(data_list,type(data_list))
print(data_tuple,type(data_tuple))
print(130*'=')

#Perbedaan Penggunaan Memory pada List dan Tuple
import sys
Data1 = [1,2,3,4,5,6,7,8,9,10,'Bakwan','Risoles',False,3.14]
Data2 = (1,2,3,4,5,6,7,8,9,10,'Bakwan','Risoles',False,3.14)
Besar_Data1 = sys.getsizeof(Data1)
Besar_Data2 = sys.getsizeof(Data2)
print(Data1)
print(Data2)
print('Besar Memory yang digunakan adalah:',Besar_Data1)
print('Besar Memory yang digunakan adalah:',Besar_Data2)
print(130*'-')

#Perbedaan Watku dalam mengolah data
import timeit
List_time = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9,10]",number=1000000)
Tuple_time = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9,10)",number=1000000)
print('waktu yang dibutuhkan untuk List:',List_time)
print('waktu yang dibutuhkan untuk Tuple:',Tuple_time)
print(130*'=')
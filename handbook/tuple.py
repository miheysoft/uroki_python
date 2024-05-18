# создание кортежа 
tuple_int = (1, 2, 3)
tuple_null = tuple('работа по найму')
tuple_list = (4, True, '1')
print(tuple_int[2])
print(tuple_null[-1])
print(tuple_list[0:1]) # получается список
# методы кортежа 
owochi = ('a', 'a', 'b', 'a')
print(owochi.count('a')) # количество вхождений
print(owochi.index('a')) # индекс первого вхождения (возвращает индекс)

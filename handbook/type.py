#!/usr/bin/env python3
# список
my_list = [1, 2, "дурень", 6.1]
print(my_list)
# кортеж
my_tuple = (1, 2, "дурень", 6.1)
print(my_tuple)
# словарь 
my_dict = {1: "дурень", 2: 6.1, "дурень": "дурень"}
print(my_dict)
# множество
my_set = {1, 2, "дурень", 6.1}
print(my_set)

# числа 
integer_t = 10
float_t = 3.1
complex_t = 2 + 3j

# выводим результат
print(type(integer_t))
print(type(float_t))
print(type(complex_t))

# арифметические операции
print(f"возведение в степень {integer_t ** float_t}") # 
print(f"целочисленноеделение {integer_t // float_t}") # 
print(f"остаток от деления {integer_t % float_t}") # 
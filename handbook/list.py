#!/usr/bin/env python3
# создание списка
my_list = ['a', 'b', 'c'] # пустой список
my_listtws = list((1, 2, 3, 4, 5))
print(f"{my_list} вторая {my_listtws}")
my_list_all = [my_list, my_listtws]
print(my_list_all)
# объединение списков
my_list.extend(my_listtws)
print(my_list)
combo_list = my_list + my_listtws
print(combo_list)
# Методы

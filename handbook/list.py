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
ovoshi_list = ['помидоры', 'огурцы', 'баклажаны']
ovoshi_list.append('морковка')
ovoshi_list.insert(0, 'лук')
del_ovoshi = ovoshi_list.pop() # удаляет последний элемент из списка и возвращает его значение
print(ovoshi_list)
print (del_ovoshi)
ovoshi_list.remove('огурцы') # remove() используется для удаления первого вхождения элемента из списка. Если элемент не найден, функция возвращает None.
ovoshi_list.sort() # сортирует список по возрастанию значений элементов
print(ovoshi_list)

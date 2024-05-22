my_set = {1, 2, 3, 10, 5, 6}
print(my_set)
my_set1 = set(["1", "2", "3", "4"])  #
print(my_set1)
my_set.add("5")  # add element to sets
print(my_set)
my_set.remove(1)  # удаляет элемент по индексу
print(f"удалил элемент 1 {my_set}")  # удаляет элемент по индексу

other_set = {1, 2, 3, 11, 5, 6}
union_set = my_set.union(other_set)  # объединяет два множества
print(union_set)

intersection_set = my_set.intersection(other_set)  # перес
print(f"пересечение двух множеств {intersection_set}")

defference_set = my_set.difference(other_set)  # разность двух множеств
print(f"my_set {my_set} other_set {other_set} разность двух множеств {defference_set}")

symmetric_difference_set = my_set.symmetric_difference(other_set)  #
print(
    f"symmetric_difference симметрическая разность двух множеств {symmetric_difference_set}"
)
print(
    f"symmetric_difference симметрическая разность двух множеств {my_set ^ other_set}"
)

#  применение множеств
#  Удаление дубликатов
my_list = [1, 2, 3, 4, 5, 6, 5]
my_set = set(my_list)
print(my_set)

#  проверка наличия элемента в множестве
if 5 in my_set:
    print(f"Элемент {5} есть в множестве")

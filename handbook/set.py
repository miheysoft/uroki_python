my_set = {1, 2, 3}
print(my_set)
my_set1 = set(["1", "2", "3", "4"])  #
print(my_set1)
my_set.add("5")  # add element to sets
print(my_set)
my_set.remove(1)  # удаляет элемент по индексу
print(f"удалил элемент 1 {my_set}")  # удаляет элемент по индексу

other_set = {1, 2, 3}
union_set = my_set.union(other_set)  # объединяет два множества
print(union_set)

intersection_set = my_set.intersection(other_set)  # объединяет два множества
print(intersection_set)

defference_set = my_set.difference(other_set)  #
print(defference_set)

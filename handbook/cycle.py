# цикл while
i = 1
while i <= 6:
    print(i)
    i += 1

vegetables = ["broccoli", "cauliflower", "spinach"]
for vegetable in vegetables:
    print(vegetable)

i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 7:
        break
else:
    print("i is not 6")

vegetables = ["broccoli", "cauliflower", "spinach", "asparagus", "cabbage"]
for vegetable in vegetables:
    if vegetable == "spinach":
        print(vegetable)
        break

else:
    print("spinach не найден")

# Генераторы списков
squares = [x**2 for x in range(1, 11)]
print(squares)
for square in squares:
    print(square)

# Генератор словарей
my_dict = {x: x**2 for x in range(1, 11)}
print(my_dict)

# Генератор множеств
my_set = {x**2 for x in range(1, 11)}
print(my_set)

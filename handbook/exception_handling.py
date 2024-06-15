try:
    x = int(input("Введите число: "))
    result = 10 / x
except ZeroDivisionError:
    print("Нельзя делить на ноль")
except ValueError:
    print("Вы ввели не число")
else:
    print("Результат: ", result)
finally:
    print("Выполнено")

x = -1
if x < 0:
    raise ValueError("число должно быть больше нуля")

x = -10
assert x < 0, "число должно быть больше нуля"

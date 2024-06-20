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

if x < 0:
    raise ValueError("число должно быть больше нуля")

x = -10
assert x < 0, "число должно быть больше нуля"


### Пример 2: Проверка условий в функциях
def деление(a, b):
    assert b != 0, "Делитель не должен быть равен нулю"
    return a / b


# print(деление(10, 2))  # Работает нормально
# print(деление(10, 0))  # Генерирует AssertionError


### Пример 5: Использование assert для отладки
def факториал(n):
    assert n >= 0, "Число должно быть неотрицательным"
    if n == 0 or n == 1:
        return 1
    else:
        return n * факториал(n - 1)


print(факториал(5))  # Работает нормально
print(факториал(-1))  # Генерирует AssertionError

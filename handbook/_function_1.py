def suma(a, b):
    return a + b


print(suma(2, 2))


# функция заглушка
def empty_function():  # None, NoneType
    pass


print(empty_function())  # NoneType


def keyword_function(a=1, b=2):
    return a * b


print(f"аргументы с ключевыми словами {keyword_function()}")

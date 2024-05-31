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


def my_function(*args):  # произвольное количество аргументов функции (args)
    for arg in args:
        print(arg)


my_function([1, 2, 3], 12, "go")


def my_function1(a, b=10):  # аргумент № 2 и ключевым словом b по умолчанию
    result = a + b
    return result


print(my_function1(5))


# Функция print_values принимает произвольное количество именованных аргументов (keyword arguments), которые передаются в функцию как словарь. Внутри функции цикл for перебирает все пары ключ-значение этого словаря, и печатает их.
# Чтобы использовать эту функцию, вы можете передать ей любое количество именованных аргументов, вот так:
def print_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


print_values(name="Вовка", family="Грабовой", status="техник")

# Глобальная переменная
my_global_variable = "Это глобальная переменная"


def my_function():
    # Глобальная переменная доступна здесь
    print(my_global_variable)


my_function()  # Вы: "Это глобальная переменная"

# Глобальная переменная
my_global_variable = "Это глобальная переменная"


def my_function():
    # Локальная переменная с тем же именем
    global my_global_variable
    my_global_variable = "используем глобальную переменную ключевое слово global"
    # Теперь my_global_variable внутри функции отличается от глобальной
    print(my_global_variable)  # Выведет: "Это локальная переменная"
    return my_global_variable  # Вернет локальное значение


# Вызов функции и присваивание результата глобальной переменной
myglobal_variable = my_function()
print(
    my_global_variable
)  # Выведет: "Это локальная переменная", а не "Это глобальная переменная"

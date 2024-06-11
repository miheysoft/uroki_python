# # Создание класса
# class MyClass:
#     my_attribute = 51

#     def my_method():  #
#         print("Мой метод")


# print(f"my_attribute = {MyClass.my_attribute}")  # Создание объекта класса

# my_object = MyClass()  # Создание объекта класса
# print(f"my_object.my_attribute  =  {my_object.my_attribute}")


class MyClass1:
    my_attribute = 52

    def my_method(self):
        print(self.my_attribute)

    def my_other_method(self):
        self.my_method()


my_object1 = MyClass1()
my_object1.my_other_method()


class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")


print(MyClass("John").say_hello())
print(MyClass.__name__)


class Family:
    def __init__(self, surname):
        self.surname = surname

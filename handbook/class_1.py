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
my_object1.my_other_method
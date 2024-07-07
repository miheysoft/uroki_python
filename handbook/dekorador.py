class MyClass:
    @classmethod
    def my_class_method(cls, arg1, arg2):
        print(f"Class:{cls} arg1:{arg1} arg2:{arg2}")

    @staticmethod
    def my_static_method(arg1, arg2):
        print(f"arg1:{arg1} arg2:{arg2}")


MyClass.my_class_method(1, 2)
MyClass.my_static_method("a", 2)

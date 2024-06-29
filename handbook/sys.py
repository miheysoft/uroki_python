import sys
import os
import subprocess

for name, module in sys.modules.items():
    if module is None:
        continue
    print(name)

# Версия Python
print(f"Версия Python: {sys.version}")

# Путь к интерпретатору Python
print(f"Путь к интерпретатору Python: {sys.executable}")

# Вывод всех аргументов командной строки
print("Аргументы командной строки:")
for arg in sys.argv:
    print(arg)

# Максимальная глубина рекурсии
print(f"Максимальная глубина рекурсии: {sys.getrecursionlimit()}")

# Путь к библиотекам Python
print(f"Путь к библиотекам Python: {sys.path}")

# Переменные окружения
print(f"Переменные окружения: {os.environ}")

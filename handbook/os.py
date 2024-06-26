import os

files = os.listdir(".")
print(files)
os.system("ls -l")
# получение значений переменных окружения
print(os.environ["HOME"])
print(os.environ["PATH"])
print(os.environ["SHELL"])

# Получение всех переменных окружения
env_variables = os.environ

# Вывод всех переменных окружения
for key, value in env_variables.items():
    print(f"{key}: {value}")

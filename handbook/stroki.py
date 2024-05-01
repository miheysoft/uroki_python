text1 = '''Привет, мир!'''
print(text1)
text2 = 'сбербанк рулит !'
text3 = "начал регулярно заниматься"
my_string = str([1, 2, 3])
print(my_string)
#Методы
string1 = 'Привет '
string2 = 'Мир'
string3 = string1 + string2
print(string3)
string4 = "TTK "
string5 = string4 * 3
print(string5)
print(string5[2])
print(string5[4:7])
print(dir(string5)) #вывод списка методов
#print(help(string5.zfill))
type(string5) #вывод типа
my_string = "Я люблю Python"
print(my_string[0:4])
print(my_string[:12])
print(my_string[0:-5])
print(my_string[2:])
# Форматирование строк
name = "Маша"
fam_name = "Машина"
print("Меня зовут {} {}".format(fam_name, name))
print(f"Меня зовут {fam_name} {name}")
print("Меня зовут {0} {1}".format(fam_name, name))
# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
# while True:
#     ip = input("Введите IP-адрес в формате x.x.x.x: ")
#     octets = ip.split(".")
#     valid_ip = len(octets) == 4

#     for i in octets:
#         valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip

#     if valid_ip:
#         break
#     print("Неправильный IP-адрес")

# if 1 <= int(octets[0]) <= 223:
#     print("unicast")
# elif 224 <= int(octets[0]) <= 239:
#     print("multicast")
# elif ip == "255.255.255.255":
#     print("local broadcast")
# elif ip == "0.0.0.0":
#     print("unassigned")
# else:
#     print("unused")

while True:
    ip = input('Введите IP-адрес ')
    ip_okt = ip.split('.')
    valid_ip = len(ip_okt) == 4

    for i in ip_okt:
        valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip
    
    if valid_ip:
        break
    else:
        print('Неправильный IP-адрес')    

if valid_ip:
    ip_int = int(ip_okt[0]) 
    if ip_int >= 1 and ip_int <= 223:
        type_adr = 'unicast'
    elif ip_int >= 224 and ip_int <= 239:
        type_adr = 'multicast'
    elif ip == "255.255.255.255":
        type_adr = 'local broadcast'
    elif ip == "0.0.0.0":
        type_adr = 'unassigned'
    else:
        type_adr = 'unused'
    print(f"{type_adr}")
   

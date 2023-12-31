# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP-адрес ')
ip_list = ip.split(".")
ip_int = int(ip_list[0]) 
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
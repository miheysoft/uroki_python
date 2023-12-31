# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
result = {}

with open('ospf.txt') as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[1][0].isdigit():
            interface = line_list[0]
            address = line_list[1]
            result[interface] = address

print(result)
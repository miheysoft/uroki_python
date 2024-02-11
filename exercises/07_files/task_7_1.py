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
d_keys = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
result = dict.fromkeys(d_keys)

output = "\n{:25} {}"

with open("ospf.txt", "r") as f:
    for line in f:
        route = line.replace(",", " ").replace("[", "").replace("]", "")
        route = route.split()
        del route[0], route[3]
        i_list = 0
        for keys in result:
            result[keys] = route[i_list]
            i_list += i_list
            print(result[keys])
            #print(output.format(result[keys]))
            
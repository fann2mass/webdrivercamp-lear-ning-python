#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]
result_list = []

for i in my_list:
    if i % 2 == 0:
        result_list.append(True)
    else:
        result_list.append(False)

result_tuple = tuple(result_list)
print(my_list)
print(result_tuple)

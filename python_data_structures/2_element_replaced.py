#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

if index < 0 or index > len(list_):
    print(list_)
else:
    list_[index] = element_to_replace
    print(list_)

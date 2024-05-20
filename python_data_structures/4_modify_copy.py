#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

copy_list = list_[:]
list_[index] = element_to_replace
print('Copy:    ', list_)
print('Original:', copy_list)

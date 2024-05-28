#!/usr/bin/python3
def mult_values(d):
    for i in d:
        d[i] *= 2
    return d


if __name__ == "__main__":
    dict_print = __import__('6_dict_print').dict_print
    dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
    new_dict = mult_values(dict_)
    dict_print(new_dict)

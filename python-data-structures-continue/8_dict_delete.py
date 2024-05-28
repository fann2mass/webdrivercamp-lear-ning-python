#!/usr/bin/python3
def dict_delete(dict_, key=""):
    if key in dict_:
        del dict_[key]
    return dict_


if __name__ == "__main__":
    dict_print = __import__('6_dict_print').dict_print
    dict_ = {"libs": (1, 2, 3), "x": "Selenium", "lang": ["Java"], "frame": "Behave", "set": set()}
    new_dict = dict_delete(dict_, 'lang')
    print(f"{'Updated Dict':.^20}")
    dict_print(new_dict)
    new_dict = dict_delete(dict_, 'y')
    print(f"{'Updated Dict':.^20}")
    dict_print(new_dict)

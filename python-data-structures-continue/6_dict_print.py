#!/usr/bin/python3
def dict_print(dict_):
    sorted_keys = sorted(dict_.keys())

    for key in sorted_keys:
        print(key, ': ', dict_[key], sep='')


if __name__ == "__main__":
    dict_ = {"libs": (1, 2, 3), "x": "Selenium", "lang": ["Java", "Python"], "frame": "Behave", "set": set()}
    dict_print(dict_)

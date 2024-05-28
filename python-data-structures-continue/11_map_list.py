#!/usr/bin/python3
def map_list(list_=[], num=0):
    return list(map(lambda x: x * num, list_))


if __name__ == "__main__":
    list_ = [5, 4, 3, 2, 1, 7]
    new_list = map_list(list_, 4)
    print(f"Original: {list_}")
    print(f"Modified: {new_list}")

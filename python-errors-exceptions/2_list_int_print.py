#!/usr/bin/python3
import traceback


def list_int_print(lst=[], i=0):
    counter = 0
    for index in range(i):
        try:
            print(int(lst[index]), end='')
            counter += 1
        except IndexError:
            print(traceback.format_exc())
            break
        except Exception:
            pass
    print()
    return counter


if __name__=="__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]
    count = list_int_print(list_, 4)
    print(f"Count: {count:d}")
    list_ = [1, 2, "Camp", 5, [3, 4]]
    count = list_int_print(list_, len(list_))
    print(f"Count: {count:d}")
    count = list_int_print(list_, len(list_) + 2)
    print(f"Count: {count:d}")

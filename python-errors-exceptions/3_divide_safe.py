#!/usr/bin/python3
def divide_safe(a, b):
    res = None
    try:
        res = a / b
    except ZeroDivisionError:
        print(end='')
    except TypeError:
        print("Error: Both inputs must be integers.")
    finally:
        print(f"Result: {res}")
    return res


if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
    b = 0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")

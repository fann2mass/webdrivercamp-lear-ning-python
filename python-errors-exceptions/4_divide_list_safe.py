#!/usr/bin/python3
def divide_list_safe(list_1, list_2, list_len):
    result_list = []

    for i in range(list_len):
        try:
            if i >= len(list_1) or i >= len(list_2):
                raise IndexError("out of range")

            num1 = list_1[i]
            num2 = list_2[i]

            if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                raise TypeError("wrong type")

            result = num1 / num2

        except IndexError:
            print("out of range")
            result = 0

        except TypeError as e:
            print(e)
            result = 0

        except ZeroDivisionError:
            print("division by 0")
            result = 0

        finally:
            result_list.append(result)

    return result_list


if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()
    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)

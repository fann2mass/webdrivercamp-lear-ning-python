#!/usr/bin/python3
def tuple_return(arg):
    if len(arg) == 0:
        return arg.append(None)
    else:
        return len(arg), arg[0]

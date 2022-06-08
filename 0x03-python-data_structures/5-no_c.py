#!/usr/bin/python3
def no_c(my_string):
    rm = list(my_string)
    for i in rm:
        if i == 'c':
            rm.remove('c')
        if i == 'C':
            rm.remove('C')
    my_string = "".join(rm)
    return my_string

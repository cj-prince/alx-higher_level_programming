#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    rp = []
    for i in range(len(my_list)):
        rp.append(my_list[i])
    if idx < 0:
        return rp
    elif idx >= len(my_list):
        return rp
    else:
        rp[idx] = element
        return

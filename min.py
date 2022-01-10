import sys
from itertools import *

nset = int(sys.stdin.readline().strip("\n"))
for i in range(nset):
    arr_list = []
    narr = int(sys.stdin.readline().strip("\n"))
    arr_list = sys.stdin.readline().strip("\n").split(" ", narr)
    arr_list = list(map(int, arr_list))
    minval = None
    for i in product('+*', repeat=(narr - 1)):
        arr_list_cpy = arr_list.copy()
        for j in range(len(i)):
            if i[j] == "*":
                sumvalue = arr_list_cpy[j] + arr_list_cpy[j + 1]
                arr_list_cpy[j] = sumvalue
                arr_list_cpy[j + 1] = sumvalue
        if minval is None:
            minval = min(arr_list_cpy)
        else:
            if min(arr_list_cpy) < minval:
                minval = min(arr_list_cpy)
    print(minval)


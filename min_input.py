from itertools import *

nset = int(input())
for i in range(nset):
    # arr_list = []
    narr = int(input())
    *arr_list, = map(int, input().split())
    minval = None
    for i in product('+*', repeat=(narr - 1)):
        arr_list_cpy = arr_list.copy()
        for j in range(len(i)):
            if i[j] == "*":
                arr_list_cpy[j] += arr_list_cpy[j + 1]
                arr_list_cpy[j + 1] = arr_list_cpy[j]
        minloc = min(arr_list_cpy)
        if minval is None:
            minval = minloc
        else:
            if minloc < minval:
                minval = minloc
    print(minval)
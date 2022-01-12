import sys
from itertools import product
from array import array

nset = int(sys.stdin.readline().strip())
list_arr = []

for i in range(nset):
    narr = int(sys.stdin.readline().strip())
    arr_list = sys.stdin.readline().strip().split(" ", narr)
    arr_list = list(map(int, arr_list))
    arr_list = array('l', arr_list)

    minval = None
    for i in product('+*', repeat=(narr - 1)):
        i = array('u', i)
        arr_list_cpy = array('l', arr_list)

        for j in range(len(i)):
            if i[j] == "*":
                summa = arr_list_cpy[j]
                for k in range(j, len(i)):
                    if i[k] == "*":
                        summa += arr_list_cpy[k+1]
                    else:
                        break

                for k in range(j, len(i)):
                    if i[k] == "*":
                        arr_list_cpy[k] = summa
                        arr_list_cpy[k+1] = summa
                        i[k] = "+"
                    else:
                        break

        minloc = min(arr_list_cpy)
        if minval is None:
            minval = minloc
        else:
            if minloc > minval:
                minval = minloc
    print(minval)
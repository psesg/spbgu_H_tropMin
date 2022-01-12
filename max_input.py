from itertools import *

nset = int(input())
for i in range(nset):

    narr = int(input())
    *arr_list, = map(int, input().split())
    minval = None

    for i in product('+*', repeat=(narr - 1)):
        i = list(i)
        arr_list_cpy = arr_list.copy()

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
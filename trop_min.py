import logging
import sys
import os
from itertools import *
from typing import List, Any

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)  # DEBUG, CRITICAL

fromfile = False
original_stdin = sys.stdin


def iter_signs(rep):
    ls: list[Any] = []
    for i in product('+*', repeat=rep):
        ls.append(i)
        logging.info("ls.append(i) '{}' len (i) = '{}' i[0] = '{}'".format(i, len(i), i[0]))
    return ls


my_input_file = os.path.join(os.getcwd(), "trop_min.txt")
if os.path.exists(my_input_file):
    # file exists
    logging.info("will take data from {}".format(my_input_file))
    fin = open(my_input_file, "r")
    sys.stdin = fin
    fromfile = True
else:
    logging.info("will take data from {}".format("stdin"))

nset = int(sys.stdin.readline().strip("\n"))

for i in range(nset):
    arr_list = []
    narr = int(sys.stdin.readline().strip("\n"))
    arr_list = sys.stdin.readline().strip("\n").split(" ", narr)
    arr_list = list(map(int, arr_list))
    logging.info("narr = {} \narr_list ={}".format(narr, arr_list))
    minval = None

    for i in product('+*', repeat=(narr - 1)):
        i = list(i)
        arr_list_cpy = arr_list.copy()
        logging.info("i = '{}'".format(i))
        logging.info("arr_list = '{}'".format(arr_list))
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
                    else:
                        break

                for k in range(j, len(i)):
                    if i[k] == "*":
                        i[k] = "+"
                    else:
                        break

        logging.info("arr_list_cpy = '{}'".format(arr_list_cpy))
        logging.info("min = '{}'".format(min(arr_list_cpy)))
        minloc = min(arr_list_cpy)
        if minval is None:
            minval = minloc
        else:
            if minloc < minval:
                minval = minloc
    print(minval)

if fromfile:
    sys.stdin = original_stdin  # Change the standard output to the file we created.
    fin.close()
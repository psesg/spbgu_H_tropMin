import logging
import sys
import os
from itertools import *
from typing import List, Any

logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)  # DEBUG, CRITICAL

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
        str4eval = ""
        arr_list_cpy = arr_list.copy()
        # logging.info("i = {} len(i) = {} i[0] = {}".format(i, len(i), i[0]))
        for j in range(len(i)):
            if i[j] == "*":
                sumvalue = arr_list_cpy[j] + arr_list_cpy[j + 1]
                arr_list_cpy[j] = sumvalue
                arr_list_cpy[j + 1] = sumvalue
            str4eval = str4eval + str(arr_list[j])
            str4eval = str4eval + " "
            str4eval = str4eval + i[j]
            str4eval = str4eval + " "
        str4eval = str4eval + str(arr_list[j + 1])
        logging.info("str4eval = '{}'".format(str4eval))
        logging.info("arr_list_cpy = '{}'".format(arr_list_cpy))
        logging.info("min = '{}'".format(min(arr_list_cpy)))
        if minval is None:
            minval = min(arr_list_cpy)
        else:
            if min(arr_list_cpy) < minval:
                minval = min(arr_list_cpy)
    print(minval)

if fromfile:
    sys.stdin = original_stdin  # Change the standard output to the file we created.
    fin.close()

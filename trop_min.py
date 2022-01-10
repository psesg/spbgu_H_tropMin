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
    logging.info("narr = {} \narr_list ={}".format(narr, arr_list ))


#ls = iter_signs(3)
#for i in ls:
#    print(i)

if fromfile:
    sys.stdin = original_stdin  # Change the standard output to the file we created.
    fin.close()
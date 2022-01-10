from itertools import *


def iter_signs(rep):
    ls = []
    for i in product('+*', repeat=rep):
        ls.append(i)
    return ls


ls = iter_signs(3)
for i in ls:
    print(i)

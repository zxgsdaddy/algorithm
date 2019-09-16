#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/9/16
from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]


def cmp(x, y):
    if x + y > y + x:
        return -1
    elif x + y == y + x:
        return 0
    else:
        return 1


def number_join(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(cmp))
    return "".join(li)


print(number_join(li))

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/8/12
from cal_exc_time import cal_exc_time_with_list


def insert_sort(li, gap):
    for i in range(gap, len(li)):
        j = i - gap
        val = li[i]
        while j >= 0 and li[j] > val:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = val


@cal_exc_time_with_list(50)
def shell_sort(li):
    '''
    gap 取法有很多种  只是其中一种
    '''
    d = len(li) // 2
    while d >= 1:
        insert_sort(li, d)
        d //= 2


shell_sort()

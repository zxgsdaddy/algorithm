#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/8/2
from cal_exc_time import cal_exc_time, get_random_list


# 小根堆
def sift(li, low, high):
    tmp = li[low]
    i = low
    j = i * 2 + 1
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j += 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = i * 2 + 1
        else:
            break
    li[i] = tmp


@cal_exc_time
def topk(li, k):
    top = li[:k]
    for i in range((k - 2) // 2, -1, -1):
        sift(top, i, k - 1)
    for i in range(k, len(li) - 1):
        if li[i] > top[0]:
            top[0], li[i] = li[i], top[0]
            sift(top, 0, k - 1)
    for j in range(k - 1, -1, -1):
        top[0], top[j] = top[j], top[0]
        sift(top, 0, j - 1)
    return top


_list = get_random_list(1000000)
print(topk(_list, 15))

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/8/2
# O(nlogn)

import random


# 大根堆
def sift(li, low, high):
    tmp = li[low]
    i = low
    j = i * 2 + 1
    while j <= high:
        if j + 1 < high and li[j + 1] > li[j]:  # 左孩纸 n*2+1 右孩纸 n*2+2
            j += 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = i * 2 + 1
        else:
            break
    li[i] = tmp


def heap_sort(li):
    lens = len(li)
    for i in range((lens - 2) // 2, -1, -1):  # 子节点的父节点 (n-1)//2 逆序建堆
        sift(li, i, lens - 1)
    for i in range(lens):
        high = lens - 1 - i
        li[0], li[high] = li[high], li[0]
        sift(li, 0, high - 1)


list_disorder = list(range(20))
list_disorder.append(random.randint(0, 19))
list_disorder.append(random.randint(0, 19))
list_disorder.append(random.randint(0, 19))
random.shuffle(list_disorder)
heap_sort(list_disorder)
print(list_disorder)
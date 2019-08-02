#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/8/2
import random


def merge(li, low, mid, high):
    ltmp = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    ltmp.extend(li[i:mid + 1]) if i <= mid else ltmp.extend(li[j:high + 1])
    li[low:high + 1] = ltmp


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


list_disorder = list(range(20))
list_disorder.append(random.randint(0, 19))
list_disorder.append(random.randint(0, 19))
list_disorder.append(random.randint(0, 19))
random.shuffle(list_disorder)
print(list_disorder)
merge_sort(list_disorder, 0, len(list_disorder) - 1)
print(list_disorder)

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/8/2
from cal_exc_time import cal_exc_time, get_random_list


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


def _merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


@cal_exc_time
def merge_sort(li):
    _merge_sort(li, 0, len(li) - 1)


_list = get_random_list(100)
merge_sort(_list)
print(_list)
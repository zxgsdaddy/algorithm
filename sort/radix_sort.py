#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/8/19
from cal_exc_time import cal_exc_time_with_list


@cal_exc_time_with_list(100000)
def radix_sort(li):
    max_num = max(li)
    buckets = [[] for _ in range(10)]
    it = 0
    while 10 ** it <= max_num:
        for val in li:
            index = val // (10 ** it) % 10
            buckets[index].append(val)
        li.clear()
        for bucket in buckets:
            li.extend(bucket)
            bucket.clear()
        it += 1


radix_sort()

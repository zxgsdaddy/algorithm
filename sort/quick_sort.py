#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/8/2
from cal_exc_time import cal_exc_time_with_list
import random


@cal_exc_time_with_list(50)
def quick_sort(li):
    random_index = random.randint(0, len(li) - 1)
    li[0], li[random_index] = li[random_index], li[0]
    partition(li, 0, len(li) - 1)


def partition(li, left, right):
    if left < right:
        mid = homing_one(li, left, right)
        partition(li, left, mid - 1)
        partition(li, mid + 1, right)


def homing_one(li, left, right):
    val = li[left]
    while left < right:
        while left < right and li[right] >= val:  # 如果不含等号，有重复值会陷入死循环
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= val:  # 如果不含等号，有重复值会陷入死循环
            left += 1
        li[right] = li[left]
    li[left] = val
    return left


quick_sort()

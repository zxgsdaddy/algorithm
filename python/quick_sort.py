#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/8/2
import random


def quick_sort(li):
    random_index = random.randint(0, len(li) - 1)
    li[0], li[random_index] = li[random_index], li[0]
    sort_handler(li, 0, len(li) - 1)


def sort_handler(li, left, right):
    if left < right:
        mid = homing_one(li, left, right)
        sort_handler(li, left, mid - 1)
        sort_handler(li, mid + 1, right)


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


list_disorder = list(range(20))
list_disorder.append(random.randint(0, 19))
list_disorder.append(random.randint(0, 19))
list_disorder.append(random.randint(0, 19))
random.shuffle(list_disorder)
quick_sort(list_disorder)
print(list_disorder)

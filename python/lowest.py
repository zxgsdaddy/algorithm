#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/8/1
import random


def bubble_sort(li):
    list_len = len(li)
    for i in range(list_len - 1):
        exchange = False
        for j in range(list_len - 1 - i):
            if li[j] > li[j + 1]:
                exchange = True
                li[j], li[j + 1] = li[j + 1], li[j]
        if not exchange:
            break


def selection_sort(li):
    list_len = len(li)
    for i in range(1, list_len - 1):
        min_index = i - 1
        for j in range(i, list_len):
            if li[min_index] > li[j]:
                min_index = j
        li[i - 1], li[min_index] = li[min_index], li[i - 1]


def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        val = li[i]
        while j >= 0 and li[j] > val:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = val


list_disorder = list(range(100))
random.shuffle(list_disorder)
insert_sort(list_disorder)
print(list_disorder)

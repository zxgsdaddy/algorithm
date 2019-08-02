#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/8/2

import random
import time


def cal_exc_time(func):
    def wrapper(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print('currentFunc [%s] execution cost time : %s' % (func.__name__, time.time() - start_time))
        return result

    return wrapper


def get_random_list(lens):
    l_disorder = list(range(int(lens)))
    l_disorder.append(random.randint(0, lens - 1))
    l_disorder.append(random.randint(0, lens - 1))
    l_disorder.append(random.randint(0, lens - 1))
    l_disorder.append(random.randint(0, lens - 1))
    l_disorder.append(random.randint(0, lens - 1))
    random.shuffle(l_disorder)
    return l_disorder


def cal_exc_time_with_list(lens):
    def get_list(func):
        _list = get_random_list(lens)

        def wrapper():
            start_time = time.time()
            result = func(lens)
            print('currentFunc [%s] execution cost time : %s' % (func.__name__, time.time() - start_time))
            print(_list)
            return result

        return wrapper

    return get_list

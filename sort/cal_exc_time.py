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
    return [random.randint(0, 1000) for _ in range(lens)]


# 脱裤子放屁， 只为写个装饰器传参的
def cal_exc_time_with_list(lens):
    def get_list(func):
        _list = get_random_list(lens)
        print("disorder", _list)

        def wrapper():
            start_time = time.time()
            result = func(_list)
            print(_list)
            print('currentFunc [%s] execution cost time : %s' % (func.__name__, time.time() - start_time))
            return result

        return wrapper

    return get_list

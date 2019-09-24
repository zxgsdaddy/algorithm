#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/9/24

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def _gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    gcd = _gcd(a, b)
    return a * b / gcd


# print(_gcd(12, 16))
print(lcm(12, 16))

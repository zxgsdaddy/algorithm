#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/9/23

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


# 自顶向下
def cut_rod_up_down(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rod_up_down(p, n - i))
        return res


# 自底向上
def cut_rod_dp(p, n):
    r = [0]
    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i - j])
        r.append(res)
    return r[n]


# 自底向上 扩展切法
def cut_rod_extend(p, n):
    r = [0]
    s = [0]
    for i in range(1, n + 1):
        res = 0
        part_length = 0  # Pi 不切分的部分
        for j in range(1, i + 1):
            new_res = p[j] + r[i - j]
            if res < new_res:
                res = new_res
                part_length = j
        r.append(res)
        s.append(part_length)
    groups = []
    _n = n
    while _n > 0:
        part_len = s[_n]
        _n -= part_len
        groups.append(part_len)
    return r[n], groups


print(cut_rod_extend(p, 9))

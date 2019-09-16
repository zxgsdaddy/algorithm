#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/9/16

activities = [(3, 5), (0, 6), (1, 4), (5, 7), (5, 9), (3, 9), (6, 10), (8, 11), (12, 16), (2, 14), (8, 12)]

activities.sort(key=lambda x: x[1])  # 最优解 一定是最早结束的活动的集合


def activity(acts):
    last_end_time = 0
    result = []
    for i, (start_time, end_time) in enumerate(acts):
        if start_time >= last_end_time:
            last_end_time = end_time
            result.append((start_time, end_time))

    return result


print(activity(activities))

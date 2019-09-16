#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/9/16

goods = [(60, 10), (100, 20), (120, 30)]  # 商品表（价格，重量）
goods.sort(key=lambda item: item[0] / item[1], reverse=True)


def fractional_backpack(goods, w):  # 分数背包
    pick_weights = [0 for _ in range(len(goods))]
    total_prize = 0
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            pick_weights[i] = weight
            w -= weight
            total_prize += prize
        else:
            pick_weights[i] = w / weight
            total_prize += pick_weights[i] * prize
            break
    return pick_weights, total_prize


print(fractional_backpack(goods, 50))

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/9/2

from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.l_child = None
        self.r_child = None
        self.parent = None

    def __str__(self):
        return "data:%s " % (self.data)


# 遍历
def pre_oder(root):
    if (root):
        print(root.data, end=",")
        pre_oder(root.l_child)
        pre_oder(root.r_child)


def in_oder(root):
    if (root):
        in_oder(root.l_child)
        print(root.data, end=",")
        in_oder(root.r_child)


def post_oder(root):
    if (root):
        post_oder(root.l_child)
        post_oder(root.r_child)
        print(root.data, end=",")


def lel_oder(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        if node.l_child:
            queue.append(node.l_child)
        if node.r_child:
            queue.append(node.r_child)
        print(node.data, end=",")


def atree():
    a = BiTreeNode("A")
    b = BiTreeNode("B")
    c = BiTreeNode("C")
    d = BiTreeNode("D")
    e = BiTreeNode("E")
    f = BiTreeNode("F")
    g = BiTreeNode("G")
    e.l_child = a
    e.r_child = g
    g.r_child = f
    a.r_child = c
    c.l_child = b
    c.r_child = d
    return e

# root = atree()
# lel_oder(root)

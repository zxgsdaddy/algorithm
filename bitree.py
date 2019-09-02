#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/9/2

from tree import *
from sort.cal_exc_time import get_random_list


class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
            if not self.root:
                self.root = node
        elif val < node.data:
            node.l_child = self.insert(node.l_child, val)
            node.l_child.parent = node
        elif val > node.data:
            node.r_child = self.insert(node.r_child, val)
            node.r_child.parent = node
        return node


li = get_random_list(15)
bi_tree = BST()
for val in li:
    bi_tree.insert(bi_tree.root, val)

in_oder(bi_tree.root)

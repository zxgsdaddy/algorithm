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

    def __remove_node_leaf(self, node):
        if not node.parent:
            self.root = None
        elif node.parent.l_child == node:
            node.parent.l_child = None
        else:
            node.parent.r_child = None

    def __remove_node_only_one_child(self, node, left_child=True):
        child = node.l_child if left_child else node.r_child
        if not node.parent:
            self.root = node.l_child if left_child else node.r_child
        else:
            if node.parent.l_child == node:
                node.parent.l_child = child
            else:
                node.parent.r_child = child
            child.parent = node.parent

    def remove(self, val):
        if not self.root:
            return None
        node = self.query(self.root, val)
        if not node:
            return None
        if not node.l_child and not node.r_child:
            self.__remove_node_leaf(node)
        elif not node.r_child:
            self.__remove_node_only_one_child(node)
        elif not node.l_child:
            self.__remove_node_only_one_child(node, left_child=False)
        else:
            min_node = node.r_child
            while min_node.l_child:
                min_node = min_node.l_child
            min_val = min_node.data
            self.remove(min_val)
            # self.__remove_node_only_one_child(node, left_child=min_node.l_child)
            node.data = min_val

    def query(self, node, val):
        if not node:
            return None
        elif node.data == val:
            return node
        elif val < node.data:
            return self.query(node.l_child, val)
        elif node.data < val:
            return self.query(node.r_child, val)


# li = get_random_list(15)
li = [0, 6, 3, 2, 1, 5, 4]
bi_tree = BST()
for val in li:
    bi_tree.insert(bi_tree.root, val)
in_oder(bi_tree.root)
print("")
bi_tree.remove(3)
bi_tree.remove(0)

in_oder(bi_tree.root)
# print(bi_tree.query(bi_tree.root, 6))

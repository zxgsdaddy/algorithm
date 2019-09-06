#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/9/5

from bitree import BST
from tree import *


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0


class AVLTree(BST):
    def __init__(self):
        BST.__init__(self)

    def rotate_left(self, p, c):
        s2 = c.l_child
        p.r_child = s2
        if s2:
            s2.parent = p

        c.l_child = p
        p.parent = c

        p.bf = 0
        c.bf = 0

        return c

    def rotate_right(self, p, c):
        s2 = c.r_child
        p.l_child = s2
        if s2:
            s2.parent = p

        c.r_child = p
        p.parent = c

        p.bf = 0
        c.bf = 0

        return c

    def rotate_right_left(self, p, c):
        g = c.l_child

        s3 = g.r_child
        c.l_child = s3
        if s3:
            s3.parent = c
        g.r_child = c
        c.parent = g

        s2 = g.l_child
        p.r_child = s2
        if s2:
            s2.parent = p
        g.l_child = p
        p.parent = g

        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0

        return g

    def rotate_left_right(self, p, c):
        g = c.r_child

        s2 = g.l_child
        c.r_child = s2
        if s2:
            s2.parent = c
        g.l_child = c
        c.parent = g

        s3 = g.r_child
        p.l_child = s3
        if s3:
            s3.parent = p
        g.r_child = p
        p.parent = g

        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0

        return g

    def insert(self, node, val):
        pass

    def insert_no_rec(self, val):  # 非递归插入
        p = self.root
        if not p:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.l_child:
                    p = p.l_child
                else:
                    p.l_child = AVLNode(val)
                    p.l_child.parent = p
                    node = p.l_child  # node 存储 插入节点
                    break
            elif val > p.data:
                if p.r_child:
                    p = p.r_child
                else:
                    p.r_child = AVLNode(val)
                    p.r_child.parent = p
                    node = p.r_child
                    break
            else:  # val == p.data
                return
        # 2.更新 balance factor
        while node.parent:
            if node.parent.l_child == node:  # 传递是从左子树来的，左子树更沉
                # 更新node.parent.bf -=1
                if node.parent.bf < 0:  # 原来node.parent.bf == -1 ,更新后变为 -2
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent  # 为了连接旋转后的子树
                    x = node.parent
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                elif node.parent.bf > 0:  # 原来node.parent.bf = 1 ,更新之后 0
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent.bf = 0 ,更新之后 -1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:  # 传递是从右子树来的，右子树更沉
                # 更新node.parent.bf +=1
                if node.parent.bf > 0:
                    g = node.parent.parent
                    x = node.parent
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                elif node.parent.bf < 0:
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = 1
                    node = node.parent
                    continue
            # 链接旋转后的子树
            n.parent = g
            if g:  # g不是空
                if x == g.l_child:
                    g.l_child = n
                else:
                    g.r_child = n
                break
            else:
                self.root = n
                break


li = [9, 8, 7, 6, 5, 4, 3, 2, 1]
tree = AVLTree()
for val in li:
    tree.insert_no_rec(val)
pre_oder(tree.root)
print("")
in_oder(tree.root)
print("")
tree.query(tree.root, 3)

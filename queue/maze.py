#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/8/27
from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dires = [
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1),
    lambda x, y: (x - 1, y),
    lambda x, y: (x + 1, y)
]


def depth_first(x1, y1, x2, y2):
    if maze[x1][y1] == 1:
        return False
    path = []
    path.append((x1, y1))
    while len(path) > 0:
        cur_node = path[-1]
        for dire in dires:
            next_node = dire(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                maze[next_node[0]][next_node[1]] = 2
                path.append(next_node)
                if next_node[0] == x2 and next_node[1] == y2:
                    for node in path:
                        maze[node[0]][node[1]] = 8
                    return True
                break
        else:
            # maze[next_node[0]][next_node[1]] = 2
            path.pop()
    return False


def printPath(path):
    node = path[-1]
    maze[node[0]][node[1]] = 8
    index = node[2]
    while index >= 0:
        node = path[index]
        index = node[2]
        maze[node[0]][node[1]] = 8


def breadth_first(x1, y1, x2, y2):
    if maze[x1][y1] == 1:
        return False
    queue = deque()
    path = []
    queue.append((x1, y1, -1))
    while len(queue) > 0:
        cur_node = queue.popleft()
        path.append(cur_node)
        if cur_node[0] == x2 and cur_node[1] == y2:
            printPath(path)
            return True
        for dire in dires:
            next_node = dire(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                maze[next_node[0]][next_node[1]] = 2
                # queue.append((next_node[0], next_node[1], path.index(cur_node)))
                queue.append((next_node[0], next_node[1], len(path) - 1))
    return False


# print(depth_first(2, 2, 12, 16))
print(breadth_first(2, 2, 12, 16))
for m in maze:
    print(m)

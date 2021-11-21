#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/21
# project = leetcdoe559-N叉树的最大深度


# Definition for a Node.
from collections import deque
from functools import lru_cache


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    @lru_cache(None)
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        ret = 1
        for child in root.children:
            ret = max(ret, 1 + self.maxDepth(child))
        return ret

    def maxDepth2(self, root):
        if not root:
            return 0
        q = deque()
        q.append(root)
        ret = 0
        while q:
            size = len(q)
            for _ in range(size):
                children = q.popleft().children
                if not children:
                    continue
                for child in children:
                    q.append(child)
            ret += 1
        return ret


solution = Solution()
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(solution.maxDepth2(root))

#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/23
# project = 剑指offerII45
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        ret = 0
        nodes = deque()
        nodes.append(root)
        while nodes:
            size = len(nodes)
            for i in range(size):
                node = nodes.popleft()
                if i == 0:
                    ret = node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
        return ret

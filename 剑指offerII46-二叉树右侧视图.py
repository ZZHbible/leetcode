#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/23
# project = 剑指offerII46-二叉树右侧视图
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.depth = -1

        def digui(root, depth, l):
            if not root:
                return
            if depth > self.depth:
                l.append(root.val)
                self.depth = depth
            digui(root.right, depth + 1, l)
            digui(root.left, depth + 1, l)

        ret = []
        digui(root, 0, ret)
        return ret

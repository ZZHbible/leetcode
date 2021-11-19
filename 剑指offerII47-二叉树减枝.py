#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/19
# project = 剑指offerII47-二叉树减枝

# Definition for a binary tree node.
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        @lru_cache(None)
        def digui(root):
            if not root:
                return None
            root.left = digui(root.left)
            root.right = digui(root.right)
            if not root.left and not root.right and root.val == 0:
                return None
            return root

        return digui(root)

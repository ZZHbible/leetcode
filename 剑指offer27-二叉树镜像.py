#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/19
# project = 剑指offer27-二叉树镜像

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from functools import lru_cache


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        @lru_cache(None)  # 记忆化
        def digui(root):  # 左右子树镜像
            if not root:
                return None
            root_copy = TreeNode(root.val)
            root_copy.left = digui(root.right)
            root_copy.right = digui(root.left)
            return root_copy

        return digui(root)

#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/21
# project = leetcode814-二叉树剪枝
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def digui(root):
            if not root: return False
            ret = True if root.val == 1 else False
            if digui(root.left) == False:
                root.left = None
                ret = ret | False
            else:
                ret |= True
            if digui(root.right) == False:
                root.right = None
                ret = ret | False
            else:
                ret |= True
            return ret

        if digui(root) == False:
            return None
        return root

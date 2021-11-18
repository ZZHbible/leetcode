#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/18
# project = leetcode863-二叉树坡度

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def digui(self, root):
        if not root:
            return 0
        left = self.digui(root.left)
        right = self.digui(root.right)
        self.sum += abs(left - right)
        return left + right + root.val

    def findTilt(self, root) -> int:
        self.digui(root)
        return self.sum

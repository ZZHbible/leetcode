#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/10
# project = leetcode98-验证二叉搜索树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.node_val = []

        def inOrder(root):
            if not root:
                return
            if root.left:
                inOrder(root.left)
            self.node_val.append(root.val)
            if root.right:
                inOrder(root.right)

        inOrder(root)
        for i in range(1, len(self.node_val)):
            if self.node_val[i] <= self.node_val[i - 1]:
                return False
        return True

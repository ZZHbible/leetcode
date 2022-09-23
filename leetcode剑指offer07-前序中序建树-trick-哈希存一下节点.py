#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/9/23
# project = leetcode剑指offer07-前序中序建树-trick-哈希存一下节点
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = 0
        while index < len(inorder):
            if inorder[index] == preorder[0]:
                break
            index += 1
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root

    def buildTree_trick(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(begin_p, end_p, begin_i, end_i):
            if begin_p > end_p or begin_i > end_i:
                return None
            root = TreeNode(preorder[begin_p])
            index = nodes[preorder[begin_p]] - begin_i
            root.left = build(begin_p + 1, begin_p + index, begin_i, begin_i + index - 1)
            root.right = build(begin_p + index + 1, end_p, begin_i + index + 1, end_i)
            return root

        n = len(preorder)
        nodes = {val: i for i, val in enumerate(inorder)}
        return build(0, n - 1, 0, n - 1)

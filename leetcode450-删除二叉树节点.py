#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/19
# project = leetcode450-删除二叉树节点

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from functools import lru_cache


class Solution:
    @lru_cache(None)  # 记忆化
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:  # 递归出口，若为空返回None
            return None

        def delete(root):  # 找到该节点后删除操作
            right = root.right  # 右子节点
            left = root.left  # 左子节点
            if not right:  # 如果右节点为空则返回左节点
                return left
            if not left:  # 如果左节点为空返回右节点
                return right
            temp = right  # 拿到右节点的副本
            while temp.left:  # 沿左子树找到最左子节点
                temp = temp.left
            temp.left = left  # 最左子节点.left=删除节点的左子节点
            return right

        if root.val == key:
            root = delete(root)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

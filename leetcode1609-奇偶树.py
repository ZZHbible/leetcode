#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/25
# project = leetcode1609


# Definition for a binary tree node.
import queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # 树的层次遍历
        q = queue.Queue()
        even_odd = True
        q.put(root)
        while not q.empty():
            num = q.qsize()
            last = 0 if even_odd else 1e6
            for _ in range(num):
                node = q.get()
                if even_odd:  # 一开始递增
                    if last < node.val and node.val % 2:
                        last = node.val
                    else:
                        return False
                else:
                    if last > node.val and not node.val % 2:
                        last = node.val
                    else:
                        return False
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            even_odd = not even_odd
        return True


solution = Solution()
print(solution.isEvenOddTree(TreeNode(5, TreeNode(9, TreeNode(3), TreeNode(5)), TreeNode(1, TreeNode(7)))))

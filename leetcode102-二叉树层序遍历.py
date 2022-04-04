#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/4
# project = leetcode102-二叉树层序遍历
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from queue import Queue
        q = Queue()
        ans = []
        if not root:
            return []
        q.put(root)
        while not q.empty():
            temp = []
            num = q.qsize()
            for _ in range(num):
                node = q.get()
                temp.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            ans.append(temp)
        return ans

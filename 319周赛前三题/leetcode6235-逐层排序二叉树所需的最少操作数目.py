#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/11/13
# project = leetcode6235-逐层排序二叉树所需的最少操作数目
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        ans = 0

        def min_swap(arr):
            pair = [(val, i) for i, val in enumerate(arr)]
            pair = sorted(pair)
            vis = [0] * len(arr)
            ans = 0
            for i in range(len(arr)):
                if vis[i] or pair[i][1] == i:
                    continue
                cycle_size = 0
                j = i
                while not vis[j]:
                    vis[j] = 1
                    j = pair[j][1]
                    cycle_size += 1
                if cycle_size > 0:
                    ans += (cycle_size - 1)
            return ans

        while len(q):
            l = []
            for _ in range(len(q)):
                node = q.popleft()
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans += min_swap(l)

        return ans

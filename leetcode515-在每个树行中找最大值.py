#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/24
# project = leetcode515-在每个树行中找最大值
# Definition for a binary tree node.
from collections import deque
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque()
        q.append(root)
        ans=[]
        while len(q):
            len_=len(q)
            max_=-2**31
            for _ in range(len_):
                node=q.popleft()
                if node.val > max_:
                    max_=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(max_)
        return ans

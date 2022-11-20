#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/11/20
# project = leetcode6242-二叉搜索树最近节点查询
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
        中序遍历二叉搜索树，获得递增序列
        求query的lower_bound和upper_bound
    '''

    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def lower_bound(nums, target):
            low, high = 0, len(nums)
            pos = len(nums) - 1
            while low < high:
                mid = low + ((high - low) >> 1)
                if nums[mid] <= target:
                    low = mid + 1
                    pos = mid
                else:  # >=
                    high = mid
            if (pos == 0 and nums[pos] > target) or (pos == len(nums) - 1 and nums[pos] > target):
                return -1
            return nums[pos]

        def upper_bound(nums, target):
            low, high = 0, len(nums)
            pos = len(nums) - 1
            while low < high:
                mid = low + ((high - low) >> 1)
                if nums[mid] < target:
                    low = mid + 1
                else:  # >
                    high = mid
                    pos = high
            if pos == len(nums) - 1 and nums[pos] < target:
                return -1
            return nums[pos]

        ans = []
        node_num = []

        def digui(root):
            if not root:
                return
            digui(root.left)
            node_num.append(root.val)
            digui(root.right)

        digui(root)
        for query in queries:
            num = query

            left = lower_bound(node_num, num)
            right = upper_bound(node_num, num)
            ans.append([left, right])
        return ans

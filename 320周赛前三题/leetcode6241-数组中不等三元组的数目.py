#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/11/20
# project = leetcode6241-数组中不等三元组的数目
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        ans += 1
        return ans

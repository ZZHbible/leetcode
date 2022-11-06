#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/11/6
# project = leetcode6229-对数组执行操作
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        ans = []
        for num in nums:
            if num != 0:
                ans.append(num)
        return ans + [0] * (len(nums) - len(ans))

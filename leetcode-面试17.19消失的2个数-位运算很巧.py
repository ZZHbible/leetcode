#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/9/26
# project = leetcode-面试17.19消失的2个数-位运算很巧
from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        begin = 1
        index = 0
        while index < len(nums):
            if nums[index] == begin:
                index += 1
            else:
                ans.append(begin)
            begin += 1
        while len(ans) < 2:
            ans.append(begin)
            begin += 1
        return ans

    def missingTwo_ans(self, nums: List[int]) -> List[int]:
        xorsum = 0
        n = len(nums) + 2
        for num in nums:
            xorsum ^= num
        for i in range(1, n + 1):
            xorsum ^= i

        lsb = xorsum & (-xorsum)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num
        for i in range(1, n + 1):
            if i & lsb:
                type1 ^= i
            else:
                type2 ^= i

        return [type1, type2]

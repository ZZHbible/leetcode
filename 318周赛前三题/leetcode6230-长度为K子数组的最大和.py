#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/11/6
# project = leetcode6230-长度为K子数组的最大和
from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        same = set()
        ans = 0
        mm = 0
        for i in range(k - 1):
            dic[nums[i]] += 1
            mm += nums[i]
            if dic[nums[i]] > 1:
                same.add(nums[i])
        for i in range(k - 1, len(nums)):
            dic[nums[i]] += 1
            mm += nums[i]
            if dic[nums[i]] > 1:
                same.add(nums[i])
            if not len(same):
                ans = max(ans, mm)
            mm -= nums[i - k + 1]
            dic[nums[i - k + 1]] -= 1
            if nums[i - k + 1] in same and dic[nums[i - k + 1]] <= 1:
                same.remove(nums[i - k + 1])
        return ans

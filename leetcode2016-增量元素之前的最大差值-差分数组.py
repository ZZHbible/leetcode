#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/2/26
# project = leetcode2016-增量元素之前的最大差值-差分数组
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        num_cha = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        ans = max(num_cha)
        print(ans)
        if ans <= 0:
            return -1
        temp = 0
        for num in num_cha:
            temp += num
            if temp < 0:
                temp = 0
            else:
                if temp > ans:
                    ans = temp
        return ans

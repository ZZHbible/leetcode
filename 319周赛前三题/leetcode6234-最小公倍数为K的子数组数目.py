#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/11/13
# project = leetcode6234-最小公倍数为K的子数组数目
import math
from typing import List


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            for j in range(i, len(nums)):
                if num % nums[j] != 0:
                    num = math.lcm(num, nums[j])
                if num == k:
                    ans += 1
                if num > k:
                    break
        return ans

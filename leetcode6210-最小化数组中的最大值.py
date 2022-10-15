#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/10/15
# project = leetcode6210-最小化数组中的最大值
from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        _min,_max=nums[0],max(nums)
        while _min < _max:
            mid=_min+((_max-_min)>>1)
            temp=0
            for num in nums:
                temp+=(mid-num)
                if temp < 0:
                    break
            if temp < 0:
                _min=mid+1
            else:
                _max=mid
        return _max
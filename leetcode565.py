#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/17
# project = leetcode565
from typing import List
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans=0
        visited=[0]*len(nums)
        i=0
        while i<len(visited):
            if not visited[i]:
                temp={nums[i]}
                last=nums[i]
                visited[i]=1
                while nums[last] not in temp:
                    visited[last]=1
                    temp.add(nums[last])
                    last=nums[last]
                ans=max(ans,len(temp))
            i+=1
        return ans

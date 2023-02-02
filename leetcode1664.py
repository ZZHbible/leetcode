#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/1/28
# project = leetcode1664
from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        l_list=[0]*(len(nums)+2)
        r_list=[0]*(len(nums)+2)
        ans=0
        for i in range(len(nums)):
            l_list[i+2]=nums[i]+l_list[i]
        for i in range(len(nums)-1,-1,-1):
            r_list[i]=nums[i]+r_list[i+2]
        for i in range(len(nums)):
            if l_list[i]+r_list[i+1]==l_list[i+1]+r_list[i+2]:
                ans+=1
        return ans

solution=Solution()
print(solution.waysToMakeFair([2, 1, 6, 4]))




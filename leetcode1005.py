#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/3
# project = leetcode1005
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        from queue import PriorityQueue
        q=PriorityQueue()
        for i in nums:
            q.put(i)
        for _ in range(k):
            q.put(-q.get())
        ret=0
        while not q.empty():
            ret+=q.get()
        return ret
    def largestSumAfterKNegations1(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        while (k):
            if i<len(nums) and  nums[i]<0:
                nums[i]=-nums[i]
                i+=1
            else:
                break
            k-=1
        if k%2:
            return sum(nums)-2*min(nums)
        return sum(nums)

solution=Solution()
nums=[4,2,3]
print(solution.largestSumAfterKNegations1(nums,1))
#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/25
# project = leetcode398
import random
from typing import List


class Solution:
    def random(self,arr):
        index=random.randint(0,len(arr)-1)
        return arr[index]

    def __init__(self, nums: List[int]):
        self.dic={}
        for i,num in enumerate(nums):
            if num in self.dic:
                self.dic[num].append(i)
            else:
                self.dic[num]=[i]
    def pick(self, target: int) -> int:
        return self.random(self.dic[target])



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/22
# project = leetcode384-打乱数组
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.copy = nums[:]
        self.len = len(nums)

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(self.len):
            index = random.randint(0, self.len - 1)
            self.copy[index], self.copy[i] = self.copy[i], self.copy[index]
        return self.copy


nums = [1, 2, 3]
solution = Solution(nums)
print(solution.shuffle())

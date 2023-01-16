#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/1/16
# project = 剑指offer56-I-分组异或，取最低为1做分组
from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        s = 0
        for i in nums:
            s ^= i
        lower_one = 1
        while not (s & lower_one): lower_one = lower_one << 1
        left, right = [], []
        for i in nums:
            if i & lower_one:
                left.append(i)
            else:
                right.append(i)
        l, r = 0, 0
        for i in left:
            l ^= i
        for i in right:
            r ^= i
        return [l, r]

#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/26
# project = leetcode710-黑名单中的随机数
import random
from collections import defaultdict
from typing import List


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.end_num=n-1
        self.mmap={}
        blacklist.sort(reverse=True)
        for black in blacklist:
            self.mmap[black]=self.end_num
            if self.end_num in self.mmap:
                self.mmap[black]=self.mmap[self.end_num]
            self.end_num-=1

    def pick(self) -> int:
        index=random.randint(0,self.end_num)
        return index if index not in self.mmap else self.mmap[index]

obj = Solution(7, [2,3,5,6])
for _ in range(20):
    param_1 = obj.pick()
    print(param_1)

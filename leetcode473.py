#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/1
# project = leetcode473
from functools import lru_cache
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum_= sum(matchsticks)
        if sum_%4 or len(matchsticks) < 4:
            return False
        k=4
        l=[0 for _ in range(k)]
        avg=sum_//4
        matchsticks.sort(reverse=True)
        def digui(idx):
            if idx==len(matchsticks):
                return True

            for i in range(k):
                l[i] += matchsticks[idx]
                if l[i] <=avg and digui(idx+1):
                    return True
                l[i]-=matchsticks[idx]
            return False
        return digui(0)

solution=Solution()
print(solution.makesquare( [5,5,5,5,4,4,4,4,3,3,3,3]))
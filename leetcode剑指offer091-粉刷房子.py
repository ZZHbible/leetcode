#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/25
# project = leetcode剑指offer091-粉刷房子
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[-1])


solution = Solution()
print(solution.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))

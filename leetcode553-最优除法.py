#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/2/27
# project = leetcode553-最优除法
from typing import List


class node:
    def __init__(self):
        self.max = 0
        self.min = 1e3
        self.max_str = ""
        self.min_str = ""


class Solution:

    def optimalDivision(self, nums: List[int]) -> str:
        len_ = len(nums)
        dp = [[node() for j in range(len_)] for i in range(len_)]
        for i in range(len_):
            dp[i][i].max = nums[i]
            dp[i][i].min = nums[i]
            dp[i][i].max_str = str(nums[i])
            dp[i][i].min_str = str(nums[i])
        for i in range(1, len_):
            for j in range(len_ - i):
                for k in range(i):
                    if dp[j][j + i].max < dp[j][j + k].max / dp[j + k + 1][j + i].min:
                        dp[j][j + i].max = dp[j][j + k].max / dp[j + k + 1][j + i].min
                        if i - k > 1:
                            dp[j][j + i].max_str = dp[j][j + k].max_str + '/(' + dp[j + k + 1][j + i].min_str + ')'
                        else:
                            dp[j][j + i].max_str = dp[j][j + k].max_str + '/' + dp[j + k + 1][j + i].min_str
                    if dp[j][j + i].min > dp[j][j + k].min / dp[j + k + 1][j + i].max:
                        dp[j][j + i].min = dp[j][j + k].min / dp[j + k + 1][j + i].max
                        if i - k > 1:
                            dp[j][j + i].min_str = dp[j][j + k].min_str + '/(' + dp[j + k + 1][j + i].max_str + ')'
                        else:
                            dp[j][j + i].min_str = dp[j][j + k].min_str + '/' + dp[j + k + 1][j + i].max_str
        return dp[0][len_ - 1].max_str


solution = Solution()
print(solution.optimalDivision([1000, 100, 10, 2]))

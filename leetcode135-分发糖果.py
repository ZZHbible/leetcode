#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/10
# project = leetcode135-分发糖果
from typing import List


class Solution:
    # 暴力判断
    def candy(self, ratings: List[int]) -> int:
        dp = [1] * len(ratings)

        def digui(i, dp):
            if i >= len(dp):
                return
            left = 0 if i - 1 < 0 else ratings[i - 1]
            right = 0 if i + 1 == len(dp) else ratings[i + 1]
            if ratings[i] <= left and ratings[i] <= right:
                dp[i] = 1
                digui(i + 1, dp)
            elif ratings[i] > left and ratings[i] <= right:
                dp[i] = dp[i - 1] + 1 if i - 1 >= 0 else 1
                digui(i + 1, dp)
            elif ratings[i] > left and ratings[i] > right:
                digui(i + 1, dp)
                l = dp[i - 1] if i - 1 >= 0 else 0
                r = dp[i + 1] if i + 1 < len(dp) else 0
                dp[i] = max(l, r) + 1
            elif ratings[i] <= left and ratings[i] > right:
                digui(i + 1, dp)
                dp[i] = dp[i + 1] + 1 if i + 1 < len(dp) else 1

        digui(0, dp)
        print(dp)
        return sum(dp)

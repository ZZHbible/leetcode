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
        return sum(dp)

    # 左右 两遍遍历
    def candy_ans(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1

        right = ret = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            ret += max(left[i], right)

        return ret


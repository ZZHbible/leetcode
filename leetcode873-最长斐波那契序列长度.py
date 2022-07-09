#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/9
# project = leetcode873-最长斐波那契序列长度
from typing import List


class Solution:
    # dp
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        indices = {x: i for i, x in enumerate(arr)}
        ans = 0
        dp = [[0] * len(arr) for _ in range(len(arr))]
        for i in range(len(arr)):
            for j in range(i - 1, -1, -1):
                if arr[j] * 2 <= arr[i]: # arr strictly increasing
                    break
                if arr[i] - arr[j] in indices:
                    dp[j][i] = max(dp[indices[arr[i] - arr[j]]][j] + 1, 3)
                    ans = max(ans, dp[j][i])
        return ans


solution = Solution()
print(solution.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))

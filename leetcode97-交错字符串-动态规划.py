#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/12/28
# project = leetcode97-交错字符串-动态规划
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if dp[i][j] == 1 and j<len(s2) and s3[i + j] == s2[j]:
                    dp[i][j + 1] = True
                if dp[i][j] == 1 and i<len(s1) and s3[i + j] == s1[i]:
                    dp[i + 1][j] = True

        return dp[len(s1)][len(s2)]
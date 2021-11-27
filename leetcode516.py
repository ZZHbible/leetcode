#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/27
# project = leetcode516
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l=len(s)
        dp=[[0]*(l) for _ in range(l)]
        for i in range(l):
            dp[i][i]=1
        for i in range(1,l):
            for j in range(l-i):
                begin=j
                end=j+i
                if s[begin]==s[end]:
                    dp[begin][end]=2 if begin+1>end-1 else dp[begin+1][end-1]+2
                else:
                    dp[begin][end]=max(dp[begin+1][end],dp[begin][end-1])
        return dp[0][l-1]

solution=Solution()
s="bbbab"
print(solution.longestPalindromeSubseq(s))
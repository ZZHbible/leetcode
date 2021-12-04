#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/3
# project = 剑指offer14-剪绳子
import math


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n<=3:
            if n==2:
                return 1
            if n==3:
                return 2
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=2
        dp[3]=3
        for i in range(4,n+1):
            max_=i
            for j in range(1,math.ceil(math.sqrt(i))+1):
                max_=max(max_,dp[j]*dp[i-j])
            dp[i]=max_
        return dp[n]

    def cuttingRope1(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)


#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/15
# project = leetcode375

#   猜数字最小的最小成本
def getMoneyAmount(n: int) -> int:
    dp=[[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n): #间隔
        for j in range(1,n-i+1):
            min_=float('inf')
            for t in range(j,j+i):
                temp=t
                tt=0
                if t+1< j+i:
                    tt=max(tt,dp[t+1][j+i]) #左值最大
                if t-1>j:
                    tt=max(tt,dp[j][t-1])   #右值最小
                min_=min(temp+tt,min_)      #当前错误成本加上左右值最大，取最小
            dp[j][j+i]=min_


    return dp[1][n]
# print(getMoneyAmount(10))
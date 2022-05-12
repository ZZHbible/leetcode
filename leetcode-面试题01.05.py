#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/5/13
# project = leetcode-面试题01.05
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if len(first)==0 or len(second)==0:
            return True if abs(len(first)-len(second))<=1 else False

        first_len=len(first)
        second_len=len(second)
        dp=[[-1]*first_len for _ in range(second_len)]
        for i in range(len(first)):
            if first[i]==second[0]:
                dp[0][i]=1-i
            else:
                dp[0][i]=0 if i==0 else dp[0][i-1]-1
        for i in range(len(second)):
            if second[i]==first[0]:
                dp[i][0]=1-i
            else:
                dp[i][0]=0 if i==0 else dp[i-1][0]-1
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if second[i]==first[j]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])-1
        return True if dp[second_len-1][first_len-1]>=0 else False

solution=Solution()
print(solution.oneEditAway("a", "ab"))
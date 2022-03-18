#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/3/18
# project = leetcode139-单词拆分-动规
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[[False]*len(s) for _ in range(len(s))]
        for k in range(1,len(s)+1):
            for i in range(len(s)):
                for word in wordDict:
                    if i+k <=len(s):
                        if s[i:i+k] == word:
                            dp[i][i+k-1]=True
                            break
        self.ans=False
        def digui(i):
            if i==len(s):
                self.ans=True
                return
            for j in range(i,len(s)):
                if dp[i][j]==True:
                    digui(j+1)
        digui(0)
        return self.ans

solution=Solution()
print(solution.wordBreak( "a", ["a"]))
#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/18
# project = leetcode386-排数DFS
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans=[0]*n
        num=1
        for i in range(n):
            ans[i]=num
            if num*10 <= n:
                num*=10
            else:
                while num+1>n or num%10==9:
                    num//=10
                num+=1
        return ans
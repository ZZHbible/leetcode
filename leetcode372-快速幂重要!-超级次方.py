#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/5
# project = leetcode372-超级次方
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def dfs(len_):
            if len_==-1:
                return 1
            return qpow(dfs(len_-1),10)*qpow(a,b[len_])%1337
        def qpow(a,b):
            a%=1337
            ans=1
            while(b):
                if b&1:
                    ans=(ans*a)%1337
                a=a*a%1337
                b>>=1
            return ans
        return dfs(len(b)-1)

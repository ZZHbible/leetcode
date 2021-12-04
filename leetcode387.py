#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/4
# project = leetcode387
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        mmap=defaultdict(int)
        for val in s:
            mmap[val]+=1
        ret=[]
        for key,val in mmap.items():
            if val == 1:
                ret.append(key)
        for i,val in enumerate(s):
            if val in ret:
              return i
        return -1
#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/2
# project = leetcode506
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score=[10,3,8,9,4]
        from queue import PriorityQueue
        q=PriorityQueue()
        for i,val in enumerate(score):
            q.put((-val,i))
        ret=[-1]*len(score)
        for i in range(len(score)):
            val,index=q.get()
            if i==0:
                ret[index]='Gold Medal'
            elif i==1:
                ret[index]='Silver Medal'
            elif i==2:
                ret[index]='Bronze Medal'
            else:
                ret[index]=str(i+1)
        return ret
solution=Solution()
print(solution.findRelativeRanks([1]))
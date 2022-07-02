#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/2
# project = leetcode871-最低加油次数
from typing import List
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        from queue import PriorityQueue
        ans,q=0,PriorityQueue()
        index,cur=0,0
        n=len(stations)
        while cur < target:
            cur+=startFuel
            if cur>=target:
                return ans
            while index < n and stations[index][0]<=cur:
                q.put(-stations[index][1])
                index+=1
            if not q.qsize():
                return -1
            startFuel=-q.get()
            ans+=1
        return ans

solution=Solution()
print(solution.minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]))
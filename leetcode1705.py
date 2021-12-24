#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/24
# project = leetcode1705
from queue import PriorityQueue
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        q = PriorityQueue()
        ret = 0
        now = 0
        for i in range(len(apples)):
            while not q.empty():
                l = q.get()
                if l[0] > now and l[1] > 0:
                    q.put(l)
                    break
            q.put([i + days[i], apples[i]])
            while not q.empty():
                l = q.get()
                if l[1] > 0 and l[0] > now:
                    l[1] -= 1
                    ret += 1
                    q.put(l)
                    break
            now += 1
        while not q.empty():
            l = q.get()
            if l[1] > 0:
                ret += min(l[1], l[0] - now)
                now += min(l[1], l[0] - now)
        return ret


solution = Solution()
print(solution.eatenApples([2, 1, 1, 4, 5], [10, 10, 6, 4, 2]))

# [2,1,1,4,5], [10,10,6,4,2] --8

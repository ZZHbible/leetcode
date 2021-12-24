#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/24
# project = leetcode1705
import heapq
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

    def eatenApples_ans(self, apples: List[int], days: List[int]) -> int:
        pq, i, ans = [], 0, 0
        while i < len(apples) or pq:
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if i < len(apples) and apples[i]:
                heapq.heappush(pq, [i + days[i], apples[i]])
            if pq:
                pq[0][1] -= 1
                ans += 1
                if not pq[0][1]:
                    heapq.heappop(pq)
            i += 1
        return ans


solution = Solution()
print(solution.eatenApples([2, 1, 1, 4, 5], [10, 10, 6, 4, 2]))

# [2,1,1,4,5], [10,10,6,4,2] --8

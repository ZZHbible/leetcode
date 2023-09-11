#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/9/11
# project = leetcode630-课程表II
from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1]) # 根据lastDay_i 升序排列
        q=list()
        total = 0
        for tx,dx in courses:
            if total+tx <= dx:
                heapq.heappush(q,-tx)
                total+=tx
            elif q and -q[0] > tx and total - (-q[0]-tx) <= dx:
                total -= (-q[0]-tx)
                heapq.heappop(q)
                heapq.heappush(q,-tx)
        return len(q)
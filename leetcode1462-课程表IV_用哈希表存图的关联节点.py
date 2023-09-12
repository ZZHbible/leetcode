#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/9/12
# project = leetcode1462-课程表IV_用哈希表存图的关联节点
from typing import List
from collections import defaultdict, deque


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        mmap = defaultdict(set)
        mmap_i2j = defaultdict(list)
        count = [0] * numCourses
        ans = []
        for p in prerequisites:
            mmap[p[1]].add(p[0])
            mmap_i2j[p[0]].append(p[1])
            count[p[1]] += 1
        q = deque([i for i in range(numCourses) if not count[i]])
        while q:
            node = q.popleft()
            for n in mmap_i2j[node]:
                count[n] -= 1
                mmap[n].update(mmap[node])
                if count[n] == 0:
                    q.append(n)

        for query in queries:
            if query[0] in mmap[query[1]]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

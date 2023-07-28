#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/7/28
# project = leetcode2050.并行课程
from collections import defaultdict
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        from queue import Queue
        mmap = defaultdict(list)
        cite = [0] * (n + 1)
        max_time = [0] * (n + 1)
        ret = 0
        for relation in relations:
            mmap[relation[0]].append(relation[1])
            cite[relation[1]] += 1
        q = Queue()
        for i in range(1, n + 1):
            if not cite[i]:
                q.put(i)

        while not q.empty():
            node = q.get()
            for n in mmap[node]:
                cite[n] -= 1
                if not cite[n]:
                    q.put(n)
                max_time[n] = max(max_time[n], max_time[node] + time[node - 1])
            ret = max(ret, max_time[node] + time[node - 1])
        return ret


solution = Solution()
print(solution.minimumTime(3, [[2, 3]], [3, 1, 1]))

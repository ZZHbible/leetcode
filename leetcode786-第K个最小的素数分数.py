#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/29
# project = leetcode786-第K个最小的素数分数
from queue import PriorityQueue
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        q=PriorityQueue()
        for i in range(len(arr)):
            for j in range(len(arr)-1,i,-1):
                q.put((arr[i]/arr[j],(arr[i],arr[j])))
        for _ in range(k-1):
            q.get()
        return list(q.get()[1])
solution=Solution()
arr=[1,2,3,5]
k=3
print(solution.kthSmallestPrimeFraction(arr, k))
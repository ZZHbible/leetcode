#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/23
# project = leetcode剑指offerII-拓扑排序
from typing import List
from collections import deque


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        degree = [0] * len(nums)
        links = [[] for _ in range(len(nums))]
        for sequence in sequences:
            for i in range(len(sequence) - 1):
                links[sequence[i] - 1].append(sequence[i + 1] - 1)
                degree[sequence[i + 1] - 1] += 1
        q = deque(i for i in degree if i == 0)
        while q:
            if len(q) > 1:
                return False
            num = q.popleft()
            for i in links[num]:
                degree[i] -= 1
                if degree[i] == 0:
                    q.append(i)
        return True

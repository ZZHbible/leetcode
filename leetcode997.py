#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/19
# project = leetcode997
from collections import Counter
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_degree = Counter(i for i, _ in trust)
        in_degree = Counter(i for _, i in trust)
        for i in range(1, n + 1):
            if out_degree[i] == 0 and in_degree[i] == n - 1:
                return i
        return -1

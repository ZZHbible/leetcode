#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/11/11
# project = leetcode765-并查集
from typing import List
from collections import Counter


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        f = [i for i in range(n // 2)]

        def getf(i):
            if f[i] == i:
                return i
            f[i] = getf(f[i])
            return f[i]

        def add(i, j):
            fi = getf(i)
            fj = getf(j)
            f[fi] = fj

        for i in range(0, len(row), 2):
            add(row[i] // 2, row[i + 1] // 2)
        for i in range(len(f)):
            getf(i)
        dic = Counter(f)
        ans = 0
        for val in dic.values():
            ans += (val - 1)
        return ans

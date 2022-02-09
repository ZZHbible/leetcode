#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/2/10
# project = leetcode1447-最简分数-辗转相除法
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def Euclidean(i, j):
            while j % i != 0:
                temp = j
                j = i
                i = temp % i
            return True if i != 1 else False

        ans = []
        for j in range(2, n + 1):
            for i in range(1, j):
                if not Euclidean(i, j):
                    ans.append(str(i) + '/' + str(j))
        return ans

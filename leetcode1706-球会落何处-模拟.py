#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/2/24
# project = leetcode1706-球会落何处-模拟
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(grid), len(grid[0])
        for k in range(n):
            j = k
            flag = True
            for i in range(m):
                if grid[i][j] == 1:
                    if j + 1 >= n or grid[i][j + 1] == -1:
                        ans.append(-1)
                        flag = False
                        break
                    j += 1
                else:
                    if j - 1 < 0 or grid[i][j - 1] == 1:
                        ans.append(-1)
                        flag = False
                        break
                    j -= 1
            if flag:
                ans.append(j)
        return ans

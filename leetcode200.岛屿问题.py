#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/9
# project = leetcode200.岛屿问题
from functools import lru_cache
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = [[0] * len(grid[0]) for _ in range(len(grid))]
        n = len(grid)
        m = len(grid[0])
        ans = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        @lru_cache(None)
        def digui(i, j):
            if visit[i][j]:
                return
            if grid[i][j] == '0':
                return
            visit[i][j] = 1
            for direction in directions:
                if i + direction[0] >= 0 and i + direction[0] < n and j + direction[1] >= 0 and j + direction[1] < m:
                    digui(i + direction[0], j + direction[1])

        for i in range(n):
            for j in range(m):
                if not visit[i][j] and grid[i][j] == '1':
                    ans += 1
                    digui(i, j)
        return ans


solution = Solution()
print(solution.numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))

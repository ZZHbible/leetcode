#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/9/18
# project = leetcode827-最大人工岛-标记BFS
from collections import defaultdict
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        island = defaultdict(int)  # 存每个编号为index的island的面积
        zero_grid = []
        n = m = len(grid)
        visited = [[0] * m for _ in range(n)]  # 每个index编号的island 赋值
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        index = 1
        ans = 0

        def digui(i, j, index):
            if visited[i][j] > 0 or grid[i][j] == 0:
                return
            nonlocal temp
            temp += 1
            visited[i][j] = index
            for direction in directions:
                if i + direction[0] >= 0 and i + direction[0] < n and j + direction[1] >= 0 and j + direction[1] < m:
                    digui(i + direction[0], j + direction[1], index)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    zero_grid.append((i, j))
                else:
                    temp = 0
                    digui(i, j, index)
                    if temp:
                        island[index] = temp
                        index += 1

        if not zero_grid:
            return n * n

        for i, j in zero_grid:
            area = set()
            for direction in directions:
                if i + direction[0] >= 0 and i + direction[0] < n and j + direction[1] >= 0 and j + direction[1] < m:
                    index = visited[i + direction[0]][j + direction[1]]
                    area.add((index, island[index]))
            ans = max(ans, 1 + sum([val for i, val in area]))

        return ans


solution = Solution()
print(solution.largestIsland([[0, 0, 0, 0, 0, 0, 0],
                              [0, 1, 1, 1, 1, 0, 0],
                              [0, 1, 0, 0, 1, 0, 0],
                              [1, 0, 1, 0, 1, 0, 0],
                              [0, 1, 0, 0, 1, 0, 0],
                              [0, 1, 0, 0, 1, 0, 0],
                              [0, 1, 1, 1, 1, 0, 0]]))

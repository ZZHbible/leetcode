#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/27
# project = leetcode417-太平洋大西洋水流问题
from typing import List, Tuple, Set


class Solution:
    # 辣鸡方法
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visit = [[0] * len(heights[0]) for _ in range(len(heights))]
        Pac = [[0] * len(heights[0]) for _ in range(len(heights))]
        Atl = [[0] * len(heights[0]) for _ in range(len(heights))]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def digui(i, j):
            if visit[i][j]:
                return
            visit[i][j] = 1
            for direction in directions:
                if i + direction[0] < 0 or j + direction[1] < 0:
                    Pac[i][j] = 1
                if i + direction[0] >= len(heights) or j + direction[1] >= len(heights[0]):
                    Atl[i][j] = 1
                if i + direction[0] >= 0 and i + direction[0] < len(heights) and j + direction[1] >= 0 and j + \
                        direction[1] < len(heights[0]):
                    digui(i + direction[0], j + direction[1])
                    if heights[i][j] >= heights[i + direction[0]][j + direction[1]]:
                        Pac[i][j] = Pac[i][j] | Pac[i + direction[0]][j + direction[1]]
                        Atl[i][j] = Atl[i][j] | Atl[i + direction[0]][j + direction[1]]

        digui(0, 0)
        flag = True
        while flag:
            flag = False
            for i in range(len(heights)):
                for j in range(len(heights[0])):
                    for direction in directions:
                        if i + direction[0] >= 0 and i + direction[0] < len(heights) and j + direction[1] >= 0 and j + \
                                direction[1] < len(heights[0]) and heights[i][j] >= heights[i + direction[0]][
                            j + direction[1]]:
                            if Pac[i + direction[0]][j + direction[1]] > Pac[i][j] or Atl[i + direction[0]][
                                j + direction[1]] > Atl[i][j]:
                                flag = True
                                Pac[i][j] = Pac[i][j] | Pac[i + direction[0]][j + direction[1]]
                                Atl[i][j] = Atl[i][j] | Atl[i + direction[0]][j + direction[1]]

        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if Pac[i][j] and Atl[i][j]:
                    ans.append([i, j])
        return ans

    def pacificAtlantic_ans(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def search(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = set()

            def dfs(x: int, y: int):
                if (x, y) in visited:
                    return
                visited.add((x, y))
                for nx, ny in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)):
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
                        dfs(nx, ny)

            for x, y in starts:
                dfs(x, y)
            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(map(list, search(pacific) & search(atlantic)))


solution = Solution()
print(solution.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))

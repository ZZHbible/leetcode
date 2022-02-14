from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(i, j, grid, visited):
            if grid[i][j] == 0 or visited[i][j] == 1:
                return
            else:
                visited[i][j] = 1
                for direction in directions:
                    if i + direction[0] >= 0 and i + direction[0] < len(grid) and j + direction[1] >= 0 and j + \
                            direction[1] < len(grid[0]):
                        dfs(i + direction[0], j + direction[1], grid, visited)

        for i in [0, len(grid) - 1]:
            for j in range(len(grid[0])):
                dfs(i, j, grid, visited)
        for j in [0, len(grid[0]) - 1]:
            for i in range(len(grid)):
                dfs(i, j, grid, visited)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    ans += 1

        return ans


solution = Solution()
print(solution.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = [[0] * n for _ in range(m)]
        ret = 0

        def dfs(board, visited, i, j):
            if board[i][j] == '.' or visited[i][j]:
                return
            visited[i][j] = 1
            for direction in directions:
                if direction[0] + i >= 0 and direction[0] + i < m and direction[1] + j >= 0 and direction[1] + j < n:
                    dfs(board, visited, i + direction[0], j + direction[1])

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and board[i][j] == 'X':
                    dfs(board, visited, i, j)
                    ret += 1

        return ret

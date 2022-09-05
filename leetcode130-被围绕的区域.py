from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        ans = []
        visited = [[0] * n for _ in range(m)]

        def digui(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] == 'X':
                return True
            if board[i][j] == 'O' and visited[i][j] == 0:
                visited[i][j] = 1
                temp.append((i, j))
                for direction in directions:
                    nonlocal flag
                    flag = digui(i + direction[0], j + direction[1]) and flag
            return True

        for i in range(m):
            for j in range(n):
                flag = True
                temp = []
                if board[i][j] == 'O':
                    digui(i, j)
                if flag and temp:
                    ans.extend(temp)
        for i, j in ans:
            board[i][j] = 'X'

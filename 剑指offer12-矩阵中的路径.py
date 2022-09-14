#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/9/14
# project = 剑指offer12-矩阵中的路径
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def digui(i, j, index, visited):
            if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or index >= len(word) or board[i][j] != word[index]:
                return False
            visited[i][j] = 1
            ret = False
            if index == len(word) - 1:
                return True
            for direction in directions:
                ret |= digui(i + direction[0], j + direction[1], index + 1, visited)
            visited[i][j] = 0  # 回溯
            return ret

        for i in range(n):
            for j in range(m):
                visited = [[0] * m for _ in range(n)]
                flag = digui(i, j, 0, visited)
                if flag:
                    return True
        return False

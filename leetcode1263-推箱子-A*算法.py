#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/5/8
# project = leetcode1263-推箱子
import queue
from queue import PriorityQueue
from typing import List

# 状态为set(箱子位置和人位置)
class Solution:
    def __init__(self):
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 下，上，左，右
        self.ans = 500

    def check(self, i, j, p_i, p_j, b_i, b_j, grid) -> bool:  # i,j表示到达的地方，p_i,p_j 表示所处的位置,b_i,b_j 表示箱子的位置
        if p_i == i and p_j == j: return True
        visited = [[0 for _ in range(self.n)] for _ in range(self.m)]
        q = queue.PriorityQueue()
        q.put((abs(i - p_i) + abs(j - p_j), p_i, p_j))
        visited[p_i][p_j] = 1
        while not q.empty():
            for _ in range(q.qsize()):
                _, node_i, node_j = q.get()
                for direction in self.directions:
                    next_i, next_j = node_i + direction[0], node_j + direction[1]
                    if next_i >= 0 and next_i < self.m and next_j >= 0 and next_j < self.n and \
                            not visited[next_i][next_j] and \
                            grid[next_i][next_j] != '#' and \
                            not (next_i == b_i and next_j == b_j):
                        if next_i == i and next_j == j: return True

                        q.put((abs(i - (next_i)) + abs(j - (next_j)), next_i, next_j))
                        visited[next_i][next_j] = 1
        return False

    def minPushBox(self, grid: List[List[str]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        people_i, people_j, begin_i, begin_j, target_i, target_j = -1, -1, -1, -1, -1, -1
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 'B':
                    begin_i = i
                    begin_j = j
                if grid[i][j] == 'T':
                    target_i = i
                    target_j = j
                if grid[i][j] == 'S':
                    people_i = i
                    people_j = j
        visited = set()
        q = PriorityQueue()
        q.put((0 + abs(target_i - begin_i) + abs(target_j - begin_j), (0, begin_i, begin_j, people_i, people_j)))
        while q.qsize():
            _, (step, i, j, people_i, people_j) = q.get()
            if step >= self.ans: continue
            if grid[i][j] == 'T':
                self.ans = min(self.ans, step)
                continue
            for direction in self.directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if next_i >= 0 and next_i < self.m and next_j >= 0 and next_j < self.n and grid[next_i][next_j] != '#' and \
                        (next_i, next_j, i, j) not in visited and \
                        self.check(i - direction[0], j - direction[1], people_i, people_j, i, j, grid):
                    q.put(
                        (step + 1 + abs(target_i - next_i) + abs(target_j - next_j), (step + 1, next_i, next_j, i, j))
                    )
                    visited.add((next_i, next_j, i, j))
        return self.ans if self.ans != 500 else -1

#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/5/23
# project = leetcode675
from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        from queue import PriorityQueue
        cut_list = PriorityQueue()
        m = len(forest)
        n = len(forest[0])
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    cut_list.put((forest[i][j], (i, j)))
        begin = (0, 0)
        ans = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def depth(begin, end):
            q = deque([(0, begin[0], begin[1])])
            vis = {begin}
            while q:
                d,x,y= q.popleft()
                if x == end[0] and y == end[1]:
                    return d
                for direction in directions:
                    if x + direction[0] >= 0 and x + direction[0] < m and y + direction[1] >= 0 and y + direction[
                        1] < n and forest[x + direction[0]][y + direction[1]] != 0 and (
                    x + direction[0], y + direction[1]) not in vis:
                        vis.add((x+direction[0],y+direction[1]))
                        q.append((1+d,x+direction[0],y+direction[1]))
            return -1
        while not cut_list.empty():
            num, (i, j) = cut_list.get()
            d = depth(begin, (i, j))
            if d==-1:
                return -1
            ans += d
            begin = (i, j)
        return ans


solution = Solution()
print(solution.cutOffTree([[54581641, 64080174, 24346381, 69107959],
                           [86374198, 61363882, 68783324, 79706116],
                           [668150, 92178815, 89819108, 94701471],
                           [83920491, 22724204, 46281641, 47531096],
                           [89078499, 18904913, 25462145, 60813308]]))

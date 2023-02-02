#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/2/2
# project = leetcode1129-颜色交替的最短路径

from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        node_edge = [[[], []] for _ in range(n)]
        for edge in redEdges:
            node_edge[edge[0]][0].append(edge[1])
        for edge in blueEdges:
            node_edge[edge[0]][1].append(edge[1])
        # print(node_edge)
        visit = {(0, 0), (0, 1)}
        q = [[0, 0], [0, 1]]
        ans = [-1] * n
        level = 0
        while q:
            temp = []
            for node, color in q:
                near_node = node_edge[node][1 - color]
                for n in near_node:
                    if (n, 1 - color) not in visit:
                        visit.add((n, 1 - color))
                        temp.append([n, 1 - color])
                if ans[node] == -1:
                    ans[node] = level

            level += 1
            q = temp

        return ans


solution = Solution()
print(solution.shortestAlternatingPaths(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[1, 2], [2, 3], [3, 1]]))

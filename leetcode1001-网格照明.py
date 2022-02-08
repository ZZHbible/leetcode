#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/2/8
# project = leetcode1001-网格照明
from collections import Counter
from typing import List


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        point = set()
        row, col, diagonal, antiDiagonal = Counter(), Counter(), Counter(), Counter()
        for r, c in lamps:
            if (r, c) in point:
                continue
            point.add((r, c))
            row[r] += 1
            col[c] += 1
            diagonal[r - c] += 1
            antiDiagonal[r + c] += 1
        ans = []
        for i, [r, c] in enumerate(queries):
            if row[r] > 0 or col[c] > 0 or diagonal[r - c] > 0 or antiDiagonal[r + c] > 0:
                ans.append(1)
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if i >= 0 and i < n and j >= 0 and j < n:
                            if (i, j) in point:
                                point.discard((i, j))
                                row[i] -= 1
                                col[j] -= 1
                                diagonal[i - j] -= 1
                                antiDiagonal[i + j] -= 1
            else:
                ans.append(0)

        return ans


n = 5
lamps = [[0, 0], [0, 4]]
queries = [[0, 4], [0, 1], [1, 4]]
solution = Solution()
print(solution.gridIllumination(n, lamps, queries))

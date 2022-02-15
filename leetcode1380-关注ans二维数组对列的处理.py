from typing import List

import numpy as np


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        print(list(zip(*matrix)))
        np_matrix = np.array(matrix)
        row_min = []
        ans = []
        for i in range(len(np_matrix)):
            row_min.append(min(np_matrix[i]))
        for i in range(len(np_matrix[0])):
            col_max = max(np_matrix[:, i])
            if col_max in row_min:
                ans.append(int(col_max))
        return ans

    def luckyNumbers_ans(self, matrix: List[List[int]]) -> List[int]:
        minRow = [min(row) for row in matrix]
        maxCol = [max(col) for col in zip(*matrix)]  # 重要！
        ans = []
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == minRow[i] == maxCol[j]:
                    ans.append(x)
        return ans


solution = Solution()
print(solution.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))

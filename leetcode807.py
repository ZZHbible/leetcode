from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max=[]
        col_max=[]
        for i in grid:
            row_max.append(max(i))
        for j in range(len(grid[0])):
            max_col=0
            for i in range(len(grid)):
                if grid[i][j] > max_col:
                    max_col=grid[i][j]
            col_max.append(max_col)
        gridNew=[]
        for i in range(len(row_max)):
            add=[]
            for j in range(len(col_max)):
                add.append(min(row_max[i],col_max[j]))
            gridNew.append(add)
        ret=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret+=gridNew[i][j]-grid[i][j]
        return ret

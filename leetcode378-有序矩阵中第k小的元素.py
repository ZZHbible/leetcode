#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/5/18
# project = leetcode378-有序矩阵中第k小的元素
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m,n=len(matrix),len(matrix[0])

        left,right=matrix[0][0],matrix[m-1][n-1]
        while left<right:
            mid=left+((right-left) >> 1)
            i,j,count=m-1,0,0
            while i>=0 and j<n:
                while i>=0 and matrix[i][j] > mid:
                    i-=1
                if i>=0 and matrix[i][j]<=mid:
                    count+=(i+1)
                j+=1
            if count < k:
                left=mid+1
            else:
                right=mid
        return left

solution=Solution()
print(solution.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
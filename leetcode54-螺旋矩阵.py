#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/5/8
# project = leetcode54-螺旋矩阵
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        begin_direction=0
        ans=[]
        i,j=0,0
        len_=len(matrix)*len(matrix[0])
        while len(ans)<len_:
            if not visited[i][j]:
                visited[i][j]=1
                ans.append(matrix[i][j])
            if i+directions[begin_direction][0]<0 or  i+directions[begin_direction][0]>=len(matrix) or j+directions[begin_direction][1]<0 or j+directions[begin_direction][1]>=len(matrix[0]) or visited[i+directions[begin_direction][0]][j+directions[begin_direction][1]]:
                begin_direction=(begin_direction+1)%4
            i=i+directions[begin_direction][0]
            j=j+directions[begin_direction][1]
        return ans
solution=Solution()
print(solution.spiralOrder(
[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
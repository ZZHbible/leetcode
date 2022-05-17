#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/5/15
# project = leetcode812
import math
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans=0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for k in range(j+1,len(points)):
                    # 若不在一条直线上
                    a=math.sqrt((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)
                    b=math.sqrt((points[i][0]-points[k][0])**2+(points[i][1]-points[k][1])**2)
                    c=math.sqrt((points[j][0]-points[k][0])**2+(points[j][1]-points[k][1])**2)
                    if a+c>b and a+b>c and b+c>a:
                        p=(a+b+c)/2
                        area=math.sqrt(p*(p-a)*(p-b)*(p-c))
                        if area>ans:
                            ans=area
        return ans

solution=Solution()
print(solution.largestTriangleArea(
    [[35, -23], [-12, -48], [-34, -40], [21, -25], [-35, -44], [24, 1], [16, -9], [41, 4], [-36, -49], [42, -49],
     [-37, -20], [-35, 11], [-2, -36], [18, 21], [18, 8], [-24, 14], [-23, -11], [-8, 44], [-19, -3], [0, -10],
     [-21, -4], [23, 18], [20, 11], [-42, 24], [6, -19]]))
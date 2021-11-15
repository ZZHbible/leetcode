#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/16
# project = leetcode391_矩阵重叠分离问题
from collections import defaultdict
class Solution:
    def __init__(self):
        self.min_x=1e5
        self.max_x=-1e5
        self.min_y=1e5
        self.max_y=-1e5
    def isRectangleCover(self, rectangles) -> bool: #rectangles: List[List[int]]
        # 1.要实现完美覆盖，除正方形顶点四个坐标外(四个坐标出现一次)，每个坐标出现2次或四次
        # 2.area_sum==(self.max_x-self.min_x)*(self.max_y-self.min_y)
        cnt=defaultdict(int)
        area_sum=0
        for i in rectangles:
            self.min_x=min(self.min_x,i[0],i[2])
            self.max_x=max(self.max_x,i[0],i[2])
            self.min_y=min(self.min_y,i[1],i[3])
            self.max_y=max(self.max_y,i[1],i[3])
            area_sum+=(i[2]-i[0])*(i[3]-i[1])   #计算总面积
            #将矩阵四个点加入dict
            cnt[(i[0],i[1])]+=1
            cnt[(i[2],i[3])]+=1
            cnt[(i[0],i[3])]+=1
            cnt[(i[2],i[1])]+=1
        for key,val in cnt.items():
            if key==(self.min_x,self.min_y) or key==(self.min_x,self.max_y) or key==(self.max_x,self.min_y) or key==(self.max_x,self.max_y):
                if val != 1:
                    return False
            else:
                if val!=2 and val!=4:
                    return False
        return area_sum==(self.max_x-self.min_x)*(self.max_y-self.min_y)
        # rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]] true
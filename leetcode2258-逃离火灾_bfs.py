#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/11/9
# project = leetcode2258-逃离火灾_bfs
from typing import List
from collections import deque
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        goal=[]
        m,n=len(grid),len(grid[0])
        goal.append((m-1,n-2))
        goal.append((m-2,n-1))
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        def get_min_len(begin_list):
            visited = [[0]*n for _ in range(m)]
            q=deque(begin_list)
            ret = 0
            ret_1= 1e9
            ret_2= 1e9
            while q:
                new_q = deque()
                for _ in range(len(q)):
                    i,j = q.popleft()
                    visited[i][j]=1
                    if (i,j) == goal[0]:
                        ret_1=ret
                    if (i,j) == goal[1]:
                        ret_2=ret
                        # return ret
                    for x,y in directions:
                        if i+x>=0 and i+x < m and j+y>=0 and j+y <n and grid[i+x][j+y] == 0 and not visited[i+x][j+y]:
                            visited[i + x][j + y] = 1
                            new_q.append([i+x,j+y])
                q=new_q
                ret+=1
            return ret_1,ret_2
        human_distance_1,human_distance_2 = get_min_len([[0,0]])
        fires=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fires.append([i,j])
        fire_distance_1,fire_distance_2 = get_min_len(fires)
        if min(fire_distance_1,fire_distance_2)==1e9 and min(human_distance_2,human_distance_1)!=1e9:
            return 1000000000
        if fire_distance_1-human_distance_1-1 >=0 or fire_distance_2-human_distance_2-1>=0:
            if human_distance_1 < human_distance_2:
                return min(fire_distance_1-human_distance_1-1,fire_distance_2-human_distance_1)
            if human_distance_1>human_distance_2:
                return min(fire_distance_2-human_distance_2-1,fire_distance_1-human_distance_2)
            else:
                if fire_distance_1!=fire_distance_2:
                    return min(fire_distance_1,fire_distance_2)-human_distance_1
                else:
                    return min(fire_distance_1,fire_distance_2)-human_distance_1-1
        return -1

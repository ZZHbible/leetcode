#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/10/21
# project = leetcode2316.统计无向图中无法互相到达点对数
from typing import List
from collections import defaultdict,deque

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        node_list=defaultdict(list)
        for [i,j] in edges:
            node_list[i].append(j)
            node_list[j].append(i)
        visited=[False]*n
        graph = defaultdict(int)
        for i in range(n):
            if visited[i]: continue
            q=deque()
            q.append(i)
            visited[i]=True
            num =0
            while q:
                node = q.popleft()
                num+=1
                for n in node_list[node]:
                    if not visited[n]:
                        q.append(n)
                        visited[n]=True
            graph[num]+=1
        ans = 0
        graph = [[k,v] for k,v in graph.items()]
        print(graph)

        for i in range(len(graph)):
            for j in range(i+1,len(graph)):
                ans+=graph[i][1]*graph[j][0]*graph[i][0]*graph[j][1]
        for k,v in graph:
            ans+=(k*k*v*(v-1)//2)
        return ans
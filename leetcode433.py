#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/5/7
# project = leetcode433
from queue import PriorityQueue
from typing import List

class Solution:
    # 猪鼻方法
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def dis(a,b):
            ret=0
            for i in range(8):
                if a[i]!=b[i]:
                    ret+=1
            return ret
        bank.insert(0,start)
        visited={}
        for i in bank:
            visited[i]=0
        nums=[dis(i,end) for i in bank]
        from queue import PriorityQueue
        q=PriorityQueue()
        q.put((nums[0],start,0))
        ans=10
        while not q.empty():
            node=q.get()
            cur,depth=node[1],node[2]
            visited[cur]=1
            if cur==end:
                ans=min(ans,depth)
                continue
            for index,b in enumerate(bank):
                if b != cur and dis(cur,b)==1 and not visited[b]:
                    q.put((nums[index],b,depth+1))
        return ans if ans!=10 else -1


solution=Solution()
print(solution.minMutation("AAAACCCC",
"CCCCCCCC",
["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]))



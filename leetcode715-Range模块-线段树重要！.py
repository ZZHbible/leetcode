#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/6/20
# project = leetcode715-Range模块-线段树重要！
from collections import defaultdict

class RangeModule:

    def __init__(self):
        self.tree=defaultdict(int)
    def push_down(self,idx):
        if self.tree[idx]:
            self.tree[idx<<1]=self.tree[idx]
            self.tree[idx<<1|1]=self.tree[idx]
    def update(self,v1:int,left,right,l,r,idx):
        if left>r or right<l:
            return
        if left<=l and right>=r:
            self.tree[idx]=v1
        else:
            mid=l+((r-l)>>1)
            self.push_down(idx)
            self.update(v1,left,right,l,mid,idx<<1)
            self.update(v1,left,right,mid+1,r,(idx<<1)|1)
            self.tree[idx]=self.tree[idx<<1]&self.tree[(idx<<1)|1]
    def query(self,left,right,l,r,idx):
        if r < left or right < l:
            return True

        if left <= l and right >=r:
            return self.tree[idx]==1
        else:
            mid=l+((r-l)>>1)
            self.push_down(idx)
            return self.query(left,right,l,mid,idx<<1) & self.query(left,right,mid+1,r,(idx<<1)|1)

    def addRange(self, left: int, right: int) -> None:
        self.update(1,left,right-1,1,10**9,1)


    def queryRange(self, left: int, right: int) -> bool:
        return self.query(left,right-1,1,10**9,1)

    def removeRange(self, left: int, right: int) -> None:
        self.update(2,left,right-1,1,10**9,1)


obj = RangeModule()
obj.addRange(10,20)
obj.removeRange(14,16)
print(obj.queryRange(10, 14))
print(obj.queryRange(13,15))
print(obj.queryRange(16,17))

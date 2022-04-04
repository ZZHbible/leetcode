#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/4
# project = leetcode307-单点修改，区间求和-线段树-非常重要！
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.seg = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, s, t):
        # s,t表示对区间[s,t]建树。p表示当前节点
        if s == t:
            self.seg[node] = nums[s]
            return
        mid = s + ((t - s) >> 1)
        self.build(nums, node * 2 + 1, s, mid)  # 左子树建树
        self.build(nums, node * 2 + 2, mid + 1, t)  # 右子树建树
        self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]

    def change(self, index, val, node, s, t):
        if s == t:
            self.seg[node] = val
            return
        mid = s + ((t - s) >> 1)
        if index <= mid:
            self.change(index, val, node * 2 + 1, s, mid)  # 修改左子树
        else:
            self.change(index, val, node * 2 + 2, mid + 1, t)  # 修改右子树
        self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]  # 递归更新

    def range(self, left, right, node, s, t):
        if left == s and right == t:
            return self.seg[node]
        mid = s + ((t - s) >> 1)
        if mid >= right:
            return self.range(left, right, node * 2 + 1, s, mid)  # 左子树
        elif mid < left:
            return self.range(left, right, node * 2 + 2, mid + 1, t)  # 右子树
        else:
            return self.range(left, mid, node * 2 + 1, s, mid) + self.range(mid + 1, right, node * 2 + 2, mid + 1,
                                                                            t)  # mid 在中间的情况，两边相加

    def update(self, index: int, val: int) -> None:
        self.change(index, val, 0, 0, self.n - 1)

    def sumRange(self, left: int, right: int) -> int:
        return self.range(left, right, 0, 0, self.n - 1)


# Your NumArray object will be instantiated and called as such:
obj = NumArray([9, 2, 7, 8, 6])
print(obj.sumRange(0, 3))

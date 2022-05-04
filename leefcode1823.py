#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/5/4
# project = leefcode1823
class node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        def build(n):
            mmap = {}
            for i in range(n):
                mmap[i + 1] = node(i + 1)
            for i in range(1, n + 1):
                mmap[i].right = mmap[(i) % n + 1]
                if i == 1:
                    mmap[i].left = mmap[n]
                else:
                    mmap[i].left = mmap[i - 1]
            return mmap[n]

        def delete(root):
            pre=root.left
            temp = root.right
            pre.right = temp
            temp.left = pre
            return pre

        root = build(n)
        while not (root.left == root and root.right == root):
            for i in range(k):
                root = root.right
            root = delete(root)
        return root.val

solution=Solution()
print(solution.findTheWinner(6, 5))






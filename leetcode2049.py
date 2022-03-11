#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/3/11
# project = leetcode2049
from typing import List


class Solution:

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        class Node():
            def __init__(self, left=None, right=None, parent=-1):
                self.left = left
                self.right = right
                self.parent = parent
                self.left_count = 0
                self.right_count = 0

        def count_child(root):
            if not root:
                return 0
            count_child(root.left)
            count_child(root.right)
            if root.left:
                root.left_count = 1 + root.left.left_count + root.left.right_count
            if root.right:
                root.right_count = 1 + root.right.left_count + root.right.right_count
            return 0

        nodes = {}
        len_=len(parents)
        for i in range(len_):
            nodes[i] = Node()
        for i, val in enumerate(parents):
            nodes[i].parent = val
            if val != -1:
                if not nodes[val].left:
                    nodes[val].left = nodes[i]
                else:
                    nodes[val].right = nodes[i]
        root = nodes[0]
        count_child(root)
        max=-1
        ans=0
        for i in range(len_):
            left=nodes[i].left_count if nodes[i].left_count!=0 else 1
            right=nodes[i].right_count if nodes[i].right_count!=0 else 1
            parent=len_-1-nodes[i].left_count -nodes[i].right_count if len_-1-nodes[i].left_count -nodes[i].right_count  else 1
            print(left,right,parent)
            mul=left*right*parent
            if mul > max:
                max=mul
                ans=0
            if mul == max:
                ans += 1
        return ans

    def countHighestScoreNodes_ans(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]
        for node, p in enumerate(parents):
            if p != -1:
                children[p].append(node)

        maxScore, cnt = 0, 0

        def dfs(node: int) -> int:
            score = 1
            size = n - 1
            for ch in children[node]:
                sz = dfs(ch)
                score *= sz
                size -= sz
            if node != 0:
                score *= size
            nonlocal maxScore, cnt
            if score == maxScore:
                cnt += 1
            elif score > maxScore:
                maxScore, cnt = score, 1
            return n - size

        dfs(0)
        return cnt



solution = Solution()
print(solution.countHighestScoreNodes([-1, 0]))

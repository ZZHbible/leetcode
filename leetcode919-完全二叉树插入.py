#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/25
# project = leetcode919-完全二叉树插入
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        from collections import deque
        self.q = deque()
        self.root = root
        self.q.append(root)
        while len(self.q):
            node = self.q.popleft()
            if node.left and node.right:
                self.q.append(node.left)
                self.q.append(node.right)
            else:
                if node.left:
                    self.q.append(node.left)
                self.q.appendleft(node)
                break

    def insert(self, val: int) -> int:
        node = self.q.popleft()
        if not node.left:
            node.left = TreeNode(val)
            self.q.appendleft(node)
            self.q.append(node.left)
        else:
            node.right = TreeNode(val)
            self.q.append(node.right)
        return node.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
obj = CBTInserter(TreeNode(1, TreeNode(2)))
param_1 = obj.insert(3)
param_2 = obj.insert(4)
param_2 = obj.get_root()

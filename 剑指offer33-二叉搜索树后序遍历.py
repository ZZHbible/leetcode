#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/1/9
# project = 剑指offer33-二叉搜索树后序遍历
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def check(postorder):
            if not postorder:
                return True
            root = postorder[-1]
            left = 0
            while postorder[left] < root:
                left += 1
            right = left
            while postorder[right] > root:
                right += 1
            if right != len(postorder) - 1:
                return False

            return check(postorder[:left]) and check(postorder[left:-1])

        return check(postorder)

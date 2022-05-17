#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/5/17
# project = leetcode953-自定义排序
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def cmp(str1, str2):
            index = 0
            while index < len(str1) and index < len(str2):
                if order.find(str1[index]) < order.find(str2[index]):
                    return -1
                if order.find(str1[index]) > order.find(str2[index]):
                    return 1
                index += 1
            if index < len(str1):
                return 1
            return -1

        from functools import cmp_to_key
        if words == sorted(words, key=cmp_to_key(cmp)):
            return True
        return False


solution = Solution()
print(solution.isAlienSorted(["worddd", "wordd"], "hlabcdefgijkmnopqrstuvwxyz"))

#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/2
# project = leetcode140-单词拆分2
from typing import List


class trieNode():
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
        self.val = ""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = trieNode()
        for word in wordDict:
            temp = root
            for ch in word:
                if not temp.children[ord(ch) - ord('a')]:
                    temp.children[ord(ch) - ord('a')] = trieNode()
                temp = temp.children[ord(ch) - ord('a')]
            temp.is_end = True
            temp.val = word
        ans = []

        def digui(root_copy, index, temp):
            if index == len(s):
                if root_copy.is_end:
                    temp.append(root_copy.val)
                    ans.append(" ".join(temp))
                    temp.pop()
                return
            if root_copy.children[ord(s[index]) - ord('a')]:
                digui(root_copy.children[ord(s[index]) - ord('a')], index + 1, temp)

            if root_copy.is_end:
                temp.append(root_copy.val)
                digui(root, index, temp)
                temp.pop()

        digui(root, 0, [])
        return ans


solution = Solution()
print(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))

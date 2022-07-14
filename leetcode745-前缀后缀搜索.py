#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/14
# project = leetcode745-前缀后缀搜索
from typing import List


class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.idxs=[]

class WordFilter:

    def __init__(self, words: List[str]):
        self.pre_root = TrieNode()
        self.suff_root = TrieNode()
        for i, word in enumerate(words):
            pre_temp = self.pre_root
            for ch in word:
                if not pre_temp.child[ord(ch) - ord('a')]:
                    pre_temp.child[ord(ch) - ord('a')] = TrieNode()
                pre_temp = pre_temp.child[ord(ch) - ord('a')]
                pre_temp.idxs.append(i)
            suff_temp = self.suff_root
            for ch in word[::-1]:
                if not suff_temp.child[ord(ch) - ord('a')]:
                    suff_temp.child[ord(ch) - ord('a')] = TrieNode()
                suff_temp = suff_temp.child[ord(ch) - ord('a')]
                suff_temp.idxs.append(i)

    def f(self, pref: str, suff: str) -> int:
        pre_temp = self.pre_root
        suff_temp = self.suff_root
        for ch in pref:
            if not pre_temp.child[ord(ch) - ord('a')]:
                return -1
            pre_temp = pre_temp.child[ord(ch) - ord('a')]
        pre_list = pre_temp.idxs
        for ch in suff[::-1]:
            if not suff_temp.child[ord(ch) - ord('a')]:
                return -1
            suff_temp = suff_temp.child[ord(ch) - ord('a')]
        suff_list = suff_temp.idxs
        pre_list.sort()
        suff_list.sort()
        i, j = len(pre_list) - 1, len(suff_list) - 1
        while i > -1 and j > -1:
            if pre_list[i] == suff_list[j]:
                return pre_list[i]
            if pre_list[i] > suff_list[j]:
                i -= 1
            else:
                j -= 1
        return -1

# Your WordFilter object will be instantiated and called as such:
obj = WordFilter(["abbba","abba"])
param_1 = obj.f("ab","ba")
print(param_1)
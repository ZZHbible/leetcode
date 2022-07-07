#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/7/7
# project = leetcode648-单词替换
from typing import List
class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isleaf = False
        self.value = ""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for dic in dictionary:
            temp = root
            for ch in dic:
                if not temp.child[ord(ch) - ord('a')]:
                    temp.child[ord(ch) - ord('a')] = TrieNode()
                temp = temp.child[ord(ch) - ord('a')]
            temp.isleaf = True
            temp.value = dic
        sentences = sentence.split()
        for i in range(len(sentences)):
            word = sentences[i]
            temp = root
            for ch in word:
                if not temp.child[ord(ch) - ord('a')]:
                    break
                temp = temp.child[ord(ch) - ord('a')]
                if temp.isleaf:
                    sentences[i] = temp.value
                    break
        return " ".join(sentences)




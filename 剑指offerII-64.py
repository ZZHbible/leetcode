#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/1/5
# project = 剑指offerII-64
from typing import List


class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isend = False


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for ch in word:
            if not node.child[ord(ch) - ord('a')]:
                node.child[ord(ch) - ord('a')] = TrieNode()
            node = node.child[ord(ch) - ord('a')]
        node.isend = True

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.add(word)

    def search(self, searchWord: str) -> bool:
        def check(node, word):
            for ch in word:
                if not node.child[ord(ch) - ord('a')]:
                    return False
                node = node.child[ord(ch) - ord('a')]
            return True if node.isend else False

        root = self.root
        for w, ch in enumerate(searchWord):
            for i, child in enumerate(root.child):
                if i != ord(ch) - ord('a') and child:
                    if check(root.child[i], searchWord[w + 1:]):
                        return True
            if not root.child[ord(ch) - ord('a')]:
                return False
            root = root.child[ord(ch) - ord('a')]
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

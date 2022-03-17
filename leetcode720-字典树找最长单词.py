#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/3/17
# project = leetcode720-字典树找最长单词
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        class TrieNode():
            def __init__(self,flag=0):
                self.flag=flag
                self.children=[None]*26
                self.val=""
        root=TrieNode(flag=1)
        ans=""
        max_=0
        for word in words:
            temp=root
            for ch in word:
                if not temp.children[ord(ch)-ord('a')]:
                    temp.children[ord(ch)-ord('a')]=TrieNode()
                temp=temp.children[ord(ch)-ord('a')]
            temp.flag=1
            temp.val=word
        def digui(root,step):
            nonlocal ans,max_
            if not root or root.flag==0:
                return
            if step>max_:
                max_=step
                ans=root.val
            for child in root.children:
                digui(child,step+1)
        digui(root,0)
        return ans

    def longestWord_ans(self, words: List[str]) -> str:
        words.sort(key=lambda x: (-len(x), x), reverse=True)
        longest = ""
        candidates = {""}
        for word in words:
            if word[:-1] in candidates:
                longest = word
                candidates.add(word)
        return longest



solution=Solution()
print(solution.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
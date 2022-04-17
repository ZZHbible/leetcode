#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/4/17
# project = leetcode819
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.replace(","," ").lower()
        list=['!','?',';','.','\'']
        for ch in list:
            paragraph=paragraph.replace(ch," ")
        words=paragraph.split()
        print(words)
        words=Counter(words)
        for ban in banned:
            if ban in words:
                words.pop(ban)
        max_=0
        ans=""
        for key,val in words.items():
            if val > max_:
                max_=val
                ans=key

        return ans


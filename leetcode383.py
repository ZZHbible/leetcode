#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/12/4
# project = leetcode383
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = defaultdict(int)
        magazine_dict = defaultdict(int)
        for i in ransomNote:
            ransomNote_dict[i] += 1
        for i in magazine:
            magazine_dict[i] += 1
        for key, val in ransomNote_dict.items():
            if magazine_dict[key] < val:
                return False
        return True

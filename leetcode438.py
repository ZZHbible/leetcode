#!/usr/bin/env python
# author = 'ZZH'
# time = 2021/11/28
# project = leetcode438
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dic = defaultdict(int)
        s_dic = defaultdict(int)
        l = len(p)
        if l > len(s):
            return []
        for i in p:  # 初始化
            p_dic[i] += 1
        for i in range(l - 1):  # 初始化
            s_dic[s[i]] += 1
        begin = 0
        ret = []
        for i in range(len(s) - l + 1):
            s_dic[s[i + l - 1]] += 1
            flag = True
            for key, val in p_dic.items():
                if s_dic[key] != val:
                    flag = False
                    break
            if flag:
                ret.append(i)
            s_dic[s[i]] -= 1
        return ret

#!/usr/bin/env python
# author = 'ZZH'
# time = 2023/10/11
# project = leetcode76-最小覆盖子串
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_dict = Counter(s)
        t_dict = Counter(t)
        ans=defaultdict(int)
        ret = s
        for key,val in t_dict.items():
            if s_dict[key] < val: return ""
            ans[key]=val
        l,r=0,0
        def check(ans)->bool:
            for v in ans.values():
                if v>0:return False
            return True

        while r<len(s):
            ch = s[r]
            r+=1
            if ch in ans:
                ans[ch]-=1
                if ans[ch] <= 0:
                    if check(ans):
                        while l<r:
                            if s[l] not in ans:
                                l+=1
                            else:
                                if ans[s[l]] == 0:break
                                else:
                                    ans[s[l]]+=1
                                    l+=1

                        if len(ret) > r-l: ret=s[l:r]

        return ret

solution=Solution()
print(solution.minWindow("ab"*50000,  "ab"))
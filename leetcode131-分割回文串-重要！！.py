from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        len_ = len(s)
        dp = [[0] * len_ for _ in range(len_)]  # 预处理动态规划求回文串-重要！
        for i in range(len_):
            dp[i][i] = 1
        for k in range(1, len_):
            for i in range(len(s) - k):
                if k == 1:
                    dp[i][i + k] = s[i] == s[i + k]
                else:
                    dp[i][i + k] = dp[i + 1][i + k - 1] if s[i] == s[i + k] else 0
        ans = []

        def digui(begin, len_, temp):  # 回溯
            if begin == len_:
                ans.append(temp.copy())
                return
            for i in range(begin, len_):
                if dp[begin][i] == 1:
                    temp.append(s[begin:i + 1])
                    digui(i + 1, len_, temp)
                    temp.pop()

        digui(0, len_, [])
        return ans

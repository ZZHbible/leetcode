from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = defaultdict(int)
        for i in text:
            dic[i] += 1
        balloon_dict = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        ans = 1e10
        for key, val in balloon_dict.items():
            if ans > dic[key] // val:
                ans = dic[key] // val
        return ans
